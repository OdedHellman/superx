"""
import app and routing modules
"""

from app import app
from routes import home, signup
from flask import session, request, render_template


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    main page route
    """
    return home.home()


@app.route("/livesearch", methods=["POST", "GET"])
def livesearch():
    """
    search route that does not reroute using jquery+ajax
    """
    return home.livesearch()


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    logging in route
    """
    return signup.login()


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    registering route
    """
    return signup.register()


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    """
    landing page for cart comparisons
    """
    return home.cart()


@app.route("/addItem", methods=['GET', 'POST'])
def add_item():
    """
    add an item route that does not reroute using jquery+ajax
    """
    return home.add_item()


@app.route("/removeItem", methods=['GET', 'POST'])
def remove_item():
    """
    remove an item route that does not reroute using jquery+ajax
    """
    return home.remove_item()


@app.route("/logout")
def logout():
    """
    logout route
    """
    return signup.logout()


@app.route('/city', methods=['GET', 'POST'])
def city():
    """
    adds city that was chosen, using jquery to get the data and ajax so not to redirect
    """
    # gets the city name from the user
    session['city'] = request.form.get('city')

    signup.save_branches()
    return ''


@app.route('/city_search', methods=['GET', 'POST'])
def city_search():
    """
    city serch route
    """
    return home.city_search()


@app.route('/update_num_items', methods=['GET', 'POST'])
def update_num_items():
    """
    update num of items chosen
    """
    return home.update_num_items()


@app.errorhandler(404)
def page_not_found():
    """
    route for 404 error handler
    """
    return render_template('404.html', title='404'), 404
