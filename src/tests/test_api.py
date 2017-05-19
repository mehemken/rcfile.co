import pytest
import requests

from threading import Thread
from server import server

@pytest.fixture
def server(request):
    """Run the falcon server in a new thread"""
    def run_server():
        rcfile.interface.get()

    t = Thread(target=run_server)
    t.daemon = True
    t.start()
    return server


def test_server(server):
    response = requests.get('http://localhost:8000/rcfile')
    assert response.status_code == 200
