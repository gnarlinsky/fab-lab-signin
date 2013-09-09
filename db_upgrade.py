#!/usr/bin/env python

"""
Lightly tweaked version of Miguel Grinberg's script to upgrade database.
 (http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
"""

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
curr_db_version = str(api.db_version(SQLALCHEMY_DATABASE_URI,
                                     SQLALCHEMY_MIGRATE_REPO))
print 'Current database version: ' + curr_db_version
