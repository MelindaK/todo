from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def _returnUser(self):
        """Private method to convert a user model into a dictionary.

        Args:
            user - A user model.
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
