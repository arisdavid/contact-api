from flask import url_for


def test_index_page(client):

    """ Test the index page responds with 200 """
    response = client.get(url_for('pages.index'))
    assert response.status_code == 200
