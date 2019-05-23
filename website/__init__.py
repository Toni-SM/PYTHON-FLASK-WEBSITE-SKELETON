from flask import Flask

import flask_login 
import flask_sqlalchemy

import config


# database object
db = flask_sqlalchemy.SQLAlchemy()

# login manager
login_manager = flask_login.LoginManager()


def create_app():
    """
    Create and return the Flask application
    
    Initialization of:
    - login manager
    - databases
    - blueprint mechanism
    """
    app = Flask(__name__)
    app.config.from_object(config.config)
    
    # init database
    db.init_app(app)
    
    # init login manager
    login_manager.init_app(app)
    login_manager.login_view = 'general.login'

    # register blueprints
    from website.views import general
    from website.views import account
    app.register_blueprint(general.mod)
    app.register_blueprint(account.mod)
    
    # create the tables of the database (if not exist)
    db.create_all(app=app)
    
    # register the default admin account (if not exist)
    from website import controller
    with app.app_context():
        try:
            if controller.register(config.config.ADMIN)[0]:
                print("[DEFAULT ACCOUNT]", config.config.ADMIN["email"])
        except AttributeError:
            print("[DEFAULT ACCOUNT] there is not a default account")
    return app


def run():
    app = create_app()
    app.run(host=config.host, port=config.port)