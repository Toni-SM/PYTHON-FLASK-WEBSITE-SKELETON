from werkzeug import security 
from . import db


# Models for authentication

class User(db.Model):
    """
    Model of the user for authentication
    """
    __tablename__ = 'user'

    email = db.Column(db.String, primary_key=True, unique=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    category = db.Column(db.String)     # administrator, define other categories...
    
    password_hash = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        """
        Retun True if the user is active
        """
        return True

    def get_id(self):
        """
        Return the email to satisfy Flask-Login's requirements
        """
        return self.email

    def is_authenticated(self):
        """
        Return True if the user is authenticated
        """
        return self.authenticated

    def is_anonymous(self):
        """
        False, as anonymous users aren't supported
        """
        return False
            
    def generate_password_hash(self, password):
        return security.generate_password_hash(password)

    def check_password_hash(self, password):
        return security.check_password_hash(self.password_hash, password)

    @property
    def __repr__(self):
        return '<%r>' % self.email
