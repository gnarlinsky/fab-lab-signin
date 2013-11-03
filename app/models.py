from app import db
from sqlalchemy.sql import desc

# TODO
# we will have admin users and regular users
#ROLE_USER = 0
#ROLE_ADMIN = 1

class User(db.Model):
    """ Describe here, including lack of password issue """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    user_name = db.Column(db.String(30), index=True, unique=True)
    first_name = db.Column(db.String(30), index=True)
    last_name = db.Column(db.String(30), index=True)
    add_to_announce_list = db.Column(db.Boolean)
    add_to_volunt_list = db.Column(db.Boolean)
    is_uiuc_student = db.Column(db.Boolean)
    who_i_am = db.Column(db.Text)
    how_heard = db.Column(db.Text)
    visits = db.relationship('Visit', backref='visitor', lazy='dynamic')

    def get_current_visits(self):
        """ Return all current Visits (i.e. those that lack a signout_timestamp
        or autosignout_timestamp, because this theoretically indicates that the
        user is still in the lab.
        """
        # get all Visits from which user has not signed out
        signed_in_visits = self.visits.filter_by(signout_timestamp=None,
                                                 auto_signout_timestamp=None)
        return signed_in_visits

    def get_current_visit(self):
        """ Return latest Visit object, based on the last Visit associated with
        this User that lacks a signout_timestamp or autosignout_timestamp,
        because this theoretically indicates that the user is still in the lab.
        (Note that a Visit will never lack a signin_timestamp, by definition.)
        """
        # get all Visits from which user has not signed out
        signed_in_visits = self.visits.filter_by(signout_timestamp=None,
                                                 auto_signout_timestamp=None)
        # Order by date signed in, in reverse order (i.e. latest first)
        ordered_signed_in_visits = signed_in_visits.order_by(desc(Visit.signin_timestamp))
        # There may be multiple Visits when the user did not sign out, so just
        # get the latest by date
        return signed_in_visits.first()  # if no current visit, returns None

    def get_all_visits(self):
        """ Return nicely formatted str with all visits """
        all_visits = [str(visit) for visit in self.visits.all()]
        return '; '.join(all_visits)

    def get_time_in(self):
        """ Return time in of the current Visit, if any. """
        # based on get_current_visit
        current_visit = self.get_current_visit()
        # current_visit may be None, so:
        try:
            #e.g. '11:30 AM, Aug 28, 2013'
            return current_visit.signin_timestamp.strftime('%l:%M %p, %b %e, %Y')
        except:
            return None

    def is_signed_in(self):
        """ Check if user is signed into the lab by looking at Visit signin/out
        timestamps. I.e. if there is a current visit, the user is theoretically
        still in the lab.  """
        if self.get_current_visit():
            return True
        else:
            return False

    def __repr__(self):
        """ docstring pls """
        # TODO:  not guaranteed to be unique
        return '{} ({} {})'.format(self.user_name, self.first_name, self.last_name)


class Visit(db.Model):
    """ Docstring """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    signin_timestamp = db.Column(db.DateTime)
    signout_timestamp = db.Column(db.DateTime)
    # we will automatically sign out a user if it's the next day after signin_timestamp
    auto_signout_timestamp = db.Column(db.DateTime)

    # lab use for this visit
    dont_know = db.Column(db.Boolean)
    volunteer = db.Column(db.Boolean)
    get_help = db.Column(db.Boolean)
    hangout = db.Column(db.Boolean)
    computer = db.Column(db.Boolean)
    electronics_room = db.Column(db.Boolean)
    laser_engraver = db.Column(db.Boolean)
    milling_machine = db.Column(db.Boolean)
    three_d_printing = db.Column(db.Boolean)
    tour = db.Column(db.Boolean)
    vinyl_cutter = db.Column(db.Boolean)
    project = db.Column(db.Boolean)
    project_art= db.Column(db.Boolean)
    project_business= db.Column(db.Boolean)
    project_research = db.Column(db.Boolean)
    project_other = db.Column(db.String)
    projects = db.Column(db.String)
    for_class = db.Column(db.Boolean)
    which_class = db.Column(db.String)
    other = db.Column(db.Boolean)
    other_text = db.Column(db.Text)
    # TODO: question -- db.Text vs db.String

    def __repr__(self):
        """ Describe a Visit in terms of sign-in and sign-out time.
            E.g. 8/28/2013, 11:30 AM - 2:00 PM. """
        # TODO: indicate whether signout_timestamp or auto_signout_timestamp
        day_signin = self.signin_timestamp.strftime('%m/%e/%Y')
        time_signin = self.signin_timestamp.strftime('%l:%M %p')
        # TODO: Note, currently assuming that sign-in and sign-out on same day.
        #       Check for that.
        try:
            time_signout = self.signout_timestamp.strftime('%l:%M %p')
        except:
            time_signout = '?'
        return '{}, {} - {}'.format(day_signin, time_signin, time_signout)
