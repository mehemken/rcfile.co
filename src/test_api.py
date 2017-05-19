import pytest
import requests
import subprocess
import time

from threading import Thread
from hugd import rcfile


@pytest.fixture
def server(request):
    """Run the falcon server in a new thread"""
    def run_server():
        p1 = 'hug -f hugd.py'.split()
        subprocess.Popen(p1)

    t = Thread(target=run_server)
    t.daemon = True
    t.start()
    time.sleep(.123)
    return server


def test_server(server):
    response = requests.get('http://localhost:8000/rcfile')
    assert response.status_code == 200
