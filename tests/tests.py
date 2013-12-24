#!/usr/bin/env

# we need the name of the parent dir to import our package since it's not on
# the path
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
import app

import unittest
import os
from app import app, db
from config import basedir
from app.models import User, Visit
from app import views  # will be testing all functions in views
from datetime import datetime, timedelta
from coverage import coverage


# TODO: additional tests; see several associated Issues

# create coverage instance, omitting the virtualenv directory and the tests
# file itself
cov = coverage(branch=True, omit=['flve/*', 'tests.py'])
cov.start()

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
        # TODO: delete test.db?


    ##########################################################################
    # app
    ##########################################################################
    # TODO: incomplete
    def test_create_visit(self):
        """ Can we create and save a User object successfully? """
        # creating and save a User object; check that made it into db
        u = User(user_name='test_user_name', first_name='Jane', last_name='Doe')
        db.session.add(u)
        db.session.commit()
        # now retrieve users from db and check that this one is the current
        # latest one

        # creating a user object without defaults
        # TODO/to answer: should fail at this level?
        self.assertEqual(0, 1)   # fail so know this test is incomplete

    ###########################################################################
    # views
    ###########################################################################
    # TODO; incomplete -- i.e. create a user that is not signed in, and so on
    def test_get_signed_in_users(self):
        """ docstring pls """
        # create a User and Visit
        u = User(user_name='test_user_name', first_name='Jane', last_name='Doe')
        db.session.add(u)
        v = Visit(signin_timestamp=datetime.now(), visitor=u)
        db.session.add(v)
        db.session.commit()

        # the just-created user should be the only signed-in user
        self.assertEqual(views.get_signed_in_users(), [u])

    ###########################################################################
    # models
    ###########################################################################
    # TODO: incomplete
    def test_get_current_visit(self):
        """ Make sure that returns the latest visit lacking a timestamp. """
        # create a User and two Visits -- one with signout_timestamp, one
        # without
        u = User(user_name='test_user_name', first_name='Jane', last_name='Doe')
        db.session.add(u)
        # previous visit -- signed in 2 hours ago, signed out 1 hour ago
        v1 = Visit(signin_timestamp=datetime.now() - timedelta(seconds=7200),
                   signout_timestamp=datetime.now() - timedelta(seconds=3600),
                   visitor=u)
        # current visit, just signed in, not signed out
        v2 = Visit(signin_timestamp=datetime.now(), visitor=u)
        db.session.add_all([v1, v2])
        db.session.commit()

        # Is the second visit returned?
        self.assertEqual(u.get_current_visit(), v2)

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass

    # ... and end coverage
    cov.stop()
    cov.save()
    # print results to console
    #print '\nCoverage Report\n===============', cov.report()
    # create and open the html file with coverage summary
    #cov.html_report(directory='./coverage')
    #os.system('open ./coverage/index.html')  # only on OS X


