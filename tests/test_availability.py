import pytest
import requests

def test_request(flask_port):
    response = requests.get(f"http://localhost:{flask_port}/?year=2021&month=12&day=4")
    try:
        print(response.ok)
        assert response.ok == 200
    except:
        raise Exception("not a working day")

    assert dict(workingDay=True) == response.json()

# def negative_test(flask_port):
