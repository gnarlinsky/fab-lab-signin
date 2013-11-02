from app import db
from app.models import Visit, User
from datetime import datetime

###########################
# create a person
###########################
u = User(user_name='jdoe1', first_name='Jane', last_name='Doe')
db.session.add(u)
db.session.commit()

###########################
# create visits for that person
###########################
# haven't signed out yet
v1 = Visit(signin_timestamp=datetime.now(), vinyl_cutter=True, visitor=u)
# 20-minute visit
v2 = Visit(signin_timestamp=datetime(2013, 11, 2, 16, 34, 41, 874421), 
           signout_timestamp=datetime(2013, 11, 2, 16, 54, 41, 874421),
           visitor=u)
db.session.add_all([v1, v2])
db.session.commit()
