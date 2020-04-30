from app import test_method
import pytest, requests, json

URL = "http://10.62.157.181:8888"

@pytest.mark.skip
def test_GET_API():
    pass

def test_False():
    assert test_method(True) == False, "test failed"

def test_GET_API():
    r = requests.get(url=URL)
    status_code = r.status_code
    assert status_code == 200, "test failed"

def test_POST_API():
    p = requests.get(url=URL+'/todo')
    status_code = p.status_code
    text = p.text
    assert status_code == 200, "test failed"