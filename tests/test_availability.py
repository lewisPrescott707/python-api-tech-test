import pytest
import requests

def test_request(flask_port):
    response = requests.get(f"http://localhost:{flask_port}/?year=2022&month=07&day=10")
    try:
        print("Response " + str(response.ok))
        assert response.ok == 200
    except:
        raise Exception("not a working day")

    assert dict(workingDay=True) == response.json()

# def negative_test(flask_port):
