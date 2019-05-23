import json
import flask 
import flask_login 

from website import controller
from website import login_manager


mod = flask.Blueprint('account', __name__)

@mod.route("/accounts", methods=["GET"])
@flask_login.login_required
def _accounts():
    """
    Display the list of registered accounts.
    This page is only available for administrators
    """
    user = flask_login.current_user
    if user.category == "administrator":
        categories=["administrator", "define other categories..."]
        accounts = controller.accounts()
        return flask.render_template("accounts.html", accounts=accounts, categories=categories)
    return flask.redirect(flask.url_for('general.index'))

@mod.route("/register", methods=["POST"])
@flask_login.login_required
def register():
    """
    Register the current account by processing the form
    """
    user = flask_login.current_user
    if user.category == "administrator":
        data = json.loads(flask.request.values['data'])
        registation_response = controller.register(data)
        response = {"status": registation_response[0], "message": registation_response[1]}
        return flask.jsonify(response)
    return flask.jsonify({"status": False, "message": "This account has not permissions to make the selected operation"})
    
@mod.route("/remove", methods=["POST"])
@flask_login.login_required
def remove():
    """
    Remove the current account by processing the form
    """
    user = flask_login.current_user
    if user.category == "administrator":
        data = json.loads(flask.request.values['data'])
        registation_response = controller.remove(data["email"])
        response = {"status": registation_response[0], "message": registation_response[1]}
        return flask.jsonify(response)
    return flask.jsonify({"status": False, "message": "This account has not permissions to make the selected operation"})