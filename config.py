import os
basedir = os.path.abspath(os.path.dirname(__file__))

# path to database file
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# path to dir that stores the SQLAlchemy-migrate data files
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = False
# Though set CSRF_ENABLED to False, still error if no SECRET_KEY....
SECRET_KEY = 'foobar'
