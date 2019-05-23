import json
import flask 
import flask_login 

from website import controller
from website import login_manager


mod = flask.Blueprint('general', __name__)

@mod.route('/', methods=['GET'])
@mod.route('/index', methods=['GET'])
def index():
    return flask.render_template('index.html')


@mod.route("/login", methods=["GET", "POST"])
def login():
    """
    For GET requests, display the login form
    For POST, login the current user by processing the form
    """
    # POST request
    if flask.request.method == 'POST':
        data = json.loads(flask.request.values['data'])
        response = {"status": False, "message": "Wrong user or password"}
        # ckeck the username and password
        if controller.login(data["username"], data["password"]):
            response["status"]=True
            response["message"]=""
            return flask.jsonify(response)
        return flask.jsonify(response)
    # GET request
    return flask.render_template("login.html")


@mod.route("/logout", methods=["GET", "POST"])
def logout():
    controller.logout()
    return flask.redirect(flask.url_for('general.index'))

@mod.route('/route', methods=['GET'])
@flask_login.login_required
def route():
    return flask.render_template('route.html')
