
def test_development_config(app):
    """ Test Development Configuration """

    app.config.from_object('config.settings')
    assert app.config['DEBUG']
