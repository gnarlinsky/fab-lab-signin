#!/usr/bin/env
import unittest
import os
from import app, db
from config import basedir
from app.models import User, Visit

# TODO: isolate relev to fablab....
# TODO: additional learning comments (interim until into docs)
class FabLabTests(unittest.TestCase):
    """ class docstring """

    def setUp(self):
        """ docstring placeholder """
        app.config['TESTING'] = True
        # TODO: this was already set in config, but redo here?
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        """ docstring placeholder """
       db.session.remove()
       db.drop_all()

    def test_create_visit(self):
        """ Can we create and save a User object successfully? """
        # creating and save a User object; check that made it into db
        u = User(user_name='test_user_name', first_name='Jane', last_name='Doe')
        db.session.add(u)
        db.session.commit()
        # now retrieve users from db and check that this one is the current
        # latest one

        # creating a user object without defaults
        # TODO/to answer: should fail at this level?)
        # blah
