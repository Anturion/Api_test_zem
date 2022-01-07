from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_index_path():
    response = client.get("/")
    assert response.status_code == 200
    assert response.template.name == 'index.html'
    
def test_user_data_path():
    response = client.get('/user/data')
    assert response.status_code == 200
    assert response.template.name == 'user_data.html'
    assert "request" in response.context

def test_user_exist_in_context():
    response = client.get('/user/data')
    assert "user" in response.context

def test_updated_user_path():
    response = client.get("/user/update")
    assert response.status_code == 200
    assert response.template.name == 'user_update.html'
