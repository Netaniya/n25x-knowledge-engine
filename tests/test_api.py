import pytest
from fastapi.testclient import TestClient
from app.main import create_app, chunks

@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.delenv('LLM_API_KEY',raising=False)
    monkeypatch.delenv('LLM_MODEL',raising=False)
    return TestClient(create_app(tmp_path/'test.db'))

def add(client, text='Die Supportzeit ist Montag bis Freitag von 09:00 bis 17:00 Uhr.',name='manual.txt'):
    return client.post('/api/documents',files={'file':(name,text.encode(),'text/plain')})

def test_health(client): assert client.get('/api/health').json()['status']=='ok'
def test_upload_retrieve_delete(client):
    r=add(client); assert r.status_code==201; ident=r.json()['id']
    assert len(client.get('/api/documents').json())==1
    res=client.post('/api/ask',json={'question':'Was ist die Supportzeit?'}).json()
    assert res['mode']=='retrieval' and '[S1]' in res['answer'] and '17:00' in res['answer']
    assert res['sources'][0]['document_id']==ident
    assert client.delete('/api/documents/'+ident).status_code==200
    assert client.get('/api/documents').json()==[]
    assert client.post('/api/ask',json={'question':'Supportzeit'}).json()['mode']=='no_match'
def test_ranking(client):
    add(client,'Katzen schlafen auf dem Sofa.','cats.txt');add(client,'Kubernetes verwaltet Container und Pods.','ops.txt')
    r=client.post('/api/ask',json={'question':'Kubernetes Container'}).json()
    assert r['sources'][0]['name']=='ops.txt'
def test_missing_match(client):
    add(client); assert client.post('/api/ask',json={'question':'Quantenmechanik'}).json()['sources']==[]
def test_bad_upload(client):
    assert add(client,'','empty.txt').status_code==422
    assert add(client,'abc','bad.exe').status_code==422
    assert client.post('/api/documents',files={'file':('big.txt',b'a'*(5*1024*1024+1))}).status_code==413
def test_missing_llm(client):
    add(client); r=client.post('/api/ask',json={'question':'Supportzeit','generate':True}).json()
    assert r['mode']=='retrieval' and 'not configured' in r['warning']
def test_validation(client):
    assert client.post('/api/ask',json={'question':'a','top_k':99}).status_code==422
    assert client.delete('/api/documents/nope').status_code==404
def test_chunking():
    parts=list(chunks('word '*500)); assert len(parts)>1 and all(0<len(p)<=850 for p in parts)
def test_persistence(tmp_path):
    p=tmp_path/'persist.db'; c=TestClient(create_app(p)); add(c)
    assert len(TestClient(create_app(p)).get('/api/documents').json())==1

def test_pdf_page_metadata(client):
    from pypdf import PdfWriter
    from pypdf.generic import DecodedStreamObject, DictionaryObject, NameObject
    from io import BytesIO
    w=PdfWriter(); p=w.add_blank_page(width=300,height=200)
    font=DictionaryObject({NameObject('/Type'):NameObject('/Font'),NameObject('/Subtype'):NameObject('/Type1'),NameObject('/BaseFont'):NameObject('/Helvetica')})
    p[NameObject('/Resources')]=DictionaryObject({NameObject('/Font'):DictionaryObject({NameObject('/F1'):font})})
    stream=DecodedStreamObject();stream.set_data(b'BT /F1 12 Tf 20 100 Td (Kubernetes runs containers.) Tj ET')
    p[NameObject('/Contents')]=w._add_object(stream)
    out=BytesIO();w.write(out)
    assert client.post('/api/documents',files={'file':('test.pdf',out.getvalue(),'application/pdf')}).status_code==201
    assert client.post('/api/ask',json={'question':'Kubernetes'}).json()['sources'][0]['page']==1

def test_generated_citation_validation(client,monkeypatch):
    import httpx
    monkeypatch.setenv('LLM_API_KEY','test-key');monkeypatch.setenv('LLM_MODEL','test-model')
    add(client)
    answer={'value':'Supportzeit ist 09:00 bis 17:00 [S1].'}
    class MockClient:
        def __init__(self,*args,**kwargs): pass
        async def __aenter__(self): return self
        async def __aexit__(self,*args): pass
        async def post(self,url,**kwargs):
            return httpx.Response(200,json={'choices':[{'message':{'content':answer['value']}}]},request=httpx.Request('POST',url))
    monkeypatch.setattr(httpx,'AsyncClient',MockClient)
    q={'question':'Supportzeit','generate':True}
    assert client.post('/api/ask',json=q).json()['mode']=='generated'
    answer['value']='Unsupported [S99]'
    assert client.post('/api/ask',json=q).json()['mode']=='retrieval'


def test_theme_selector(client):
    html=client.get("/").text
    assert all(f'value="{theme}"' in html for theme in ("navy","ocean","light"))
    assert "n25x-knowledge-theme" in html


def test_bilingual_ui(client):
    html=client.get('/').text
    assert 'id="language"' in html
    assert 'n25x-knowledge-language' in html
    assert 'Document library' in html and 'Dokumentenbibliothek' in html
    assert 'id="demo"' in html
    assert '#source-' in html
    assert client.get('/api/health').json()['version']=='0.1.3'


def test_source_scope_and_depth(client):
    a=add(client,'Support hours are 09:00 to 17:00.','a.txt').json()['id']
    b=add(client,'Support hours are 10:00 to 18:00.','b.txt').json()['id']
    q={'question':'support hours','document_ids':[b],'top_k':1}
    result=client.post('/api/ask',json=q).json()
    assert len(result['sources'])==1 and result['sources'][0]['document_id']==b
    assert '18:00' in result['answer'] and '17:00' not in result['answer']
    q['document_ids']=[]
    assert client.post('/api/ask',json=q).json()['mode']=='no_match'
    q['document_ids']=[a,b]
    assert len(client.post('/api/ask',json=q).json()['sources'])==1

def test_russian_and_controls(client):
    html=client.get('/').text
    assert 'value="ru"' in html and 'Библиотека документов' in html
    assert '<html lang="de">' in html
    assert all(f'id="{x}"' in html for x in ('all','none','depth','export'))
    assert 'document_ids:' in html and 'URL.createObjectURL' in html
    add(client,'Время поддержки с 09:00 до 17:00.','ru.txt')
    assert '17:00' in client.post('/api/ask',json={'question':'Время поддержки'}).json()['answer']
