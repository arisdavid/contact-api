import pytest
from src.app import create_app


@pytest.yield_fixture(scope='session')
def app():
    """
    Setup flask test app
    :return: Flask app
    """

    params = {
        'DEBUG': False,
        'TESTING': True
    }

    _app = create_app(settings_override=params)

    # Create an application context before running the tests
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    """
    Setup an app client, this gets executed for each test function
    :param app: Pytest fixture
    :return: Flask app client
    """

    client = app.test_client()

    yield client
