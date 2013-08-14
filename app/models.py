from app import db

# we will have admin users and regular users
ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # TODO: so user_name in form/view should be first_name + ' ' + last_name?
    # Gross
    #first_name = db.Column(db.String(30), index=True, unique=True)
    #last_name = db.Column(db.String(30), index =True, unique=True)
    full_name = db.Column(db.String(60), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)

    def __repr__(self):
        return '<User {}>'.format(self.full_name)
