#!/usr/bin/env python

import pytest
import requests
import subprocess
import time
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


@pytest.fixture(scope='module')
def server():
    """Run the falcon server in a new process"""
    # This should set up a fixture for use in all
    # the tests. It should also kill the process
    # when it finishes. Somehow the process won't
    # die. I've asked StackOverflow. Let's see
    # what they say.

    args = 'hug -f hugd.py'.split()
    hug_server = subprocess.Popen(args)
    time.sleep(0.2)

    yield hug_server

    hug_server.kill()
    status = hug_server.poll()
    logger.info(f'Process status: {status}')


def test_server(server):
    response = requests.get('http://localhost:8000/rcfile')
    assert response.status_code == 200
