from app import db
from app.models import Visit, User
from datetime import datetime, timedelta
from pprint import pprint
import random
import os


# TODO: as is, individual users could be signed in multiple times.
def create_fakes(num_visitors, num_visits):
    """
    Create ``num_visitors`` visitors and ``num_visits`` visits
    """

    #############################
    # Create some fake visitors
    #############################
    visitors = []
    for i in range(num_visitors):
        visitors.append(User(user_name='fake_user_' + str(i),
                             first_name='FakeFirstName',
                             last_name='FakeLastName')
                            )
    db.session.add_all(visitors)
    db.session.commit()
    print 'Created ' + str(len(visitors)) + ' visitors:'
    pprint(visitors)

    #############################
    # Create some fake visits
    #############################

    visits = []


    for i in range(num_visits):
        # determine type of signout
        type_signout = random.choice([0, 1, 2])
        if type_signout == 0:  # normal signout
            visit_duration = timedelta(seconds=random.randint(1, 179*60))  # less than 3 hours, in seconds
            signin_timestamp=datetime(year=2013,
                                      month=random.randint(1, 12),
                                      hour=random.randint(0, 23),
                                      minute=random.randint(0, 59), # let's just assume that all months have 28 days
                                      day=random.randint(1, 28)
                                     )
            v = Visit(signin_timestamp=signin_timestamp,
                      signout_timestamp=signin_timestamp + visit_duration,
                      vinyl_cutter=random.randint(0, 1),  # randomly pick true or false
                      # TODO: the other things (define outside of the
                      # if/elif/else
                      visitor=random.choice(visitors) # pick random visitor from list
                     )
            visits.append(v)
        elif type_signout == 1:  # autosignout
            pass
        else:  # no signout
            seconds = timedelta(seconds=random.randint(0, 3*60*60))
            # no more than 3 hours before now (see auto-signout considerations)
            visits.append(Visit(signin_timestamp=datetime.now() - seconds,
                                visitor=random.choice(visitors))
                                # TODO: the other things (define outside of the
                                # if/elif/else
                                )

    db.session.add_all(visits)
    db.session.commit()
    print '\nCreated ' + str(len(visits)) + ' visits:'
    pprint(visits)


if __name__ == '__main__':
    db_name = 'db_app.db'
    print 'This will delete the current database ' + db_name
    answer = raw_input('Do you want to continue? [y, n] ')
    if answer != 'y':
        print 'Aborting'
        exit()
    else:
        print 'Deleting old db and creating new one .......'
        os.system('rm -f ' + db_name)
        os.system('python db_create.py')


    print 'Creating visits and visitors....'
    create_fakes(num_visitors=10, num_visits=30)
