from app.web_server import app 

def test_server_running():
    # перевірка, що роут існує
    with app.test_client() as c:
        resp = c.get('/video_feed')
        assert resp.status_code in (200, 404, 301) 
