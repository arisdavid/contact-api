from flask import (Blueprint,
                   render_template)

page = Blueprint('pages', __name__, template_folder='templates')


@page.route("/")
def index():
    """
    Index / Main page
    :return: html
    """

    return render_template('index.html', title='Homepage')
