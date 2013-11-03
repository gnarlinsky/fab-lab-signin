from flask import render_template, flash, redirect, session, url_for, request#, g
from app import app, db #, login_manager, oid
from forms import SignInForm, SignUpForm
from models import Visit, User #, ROLE_USER, ROLE_ADMIN
from datetime import datetime


@app.route('/index')
@app.route('/')
def index():
    """ docstring """
    return render_template('base.html', anchor='signin',
                           signin_form=SignInForm(),
                           signup_form=SignUpForm(),
                           signed_in_users=get_signed_in_users())

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """
    Note: Using 'signin' rather than 'login' to emphasize that users use this
    app to sign in to a space (currently without authentication) rather than
    log in to a system.
    """
    signin_form = SignInForm()
    # validate and store form data
    if signin_form.validate_on_submit():
        # find this user in db
        # TODO:  find by either user_name OR email - currently just user name,
        # but changing the name of the field in this form because otherwise
        # would have two fields called user_name in the template, filled in
        # with same thing
        user = User.query.filter_by(user_name=signin_form.user_name_or_email.data).first()
        # TODO: log in with either email or user_name
        if user is None:
            # TODO: account for user name OR email
            # right now, just for the sake of this working, setting:
            messg = 'User {} not found, pls try again or [insert link to sign up/create account tab]'.format(
                signin_form.user_name_or_email.data)
            flash(messg, category='error')
        else:
            if user.is_signed_in():
                # TODO: account for user name OR email..
                # if already signed in, tell them so
                messg = 'User {} already signed in on {}'.format(user.user_name,
                    user.get_time_in())
                flash(messg, category='warning')
            else:
                # determine which project(s) exactly, if one was chosen
                # TODO: a more elegant way to do that
                chosen_projects = []
                if signin_form.project.data:
                    for project in [signin_form.project_art,
                                    signin_form.project_business,
                                    signin_form.project_research,
                                    signin_form.project_other
                                   ]:
                        if project.data: # if was checked or filled out
                            chosen_projects.append(str(project.data))
                chosen_proj_str = '; '.join(chosen_projects)
                # if not already signed, create and save Visit instance
                new_visit = Visit(signin_timestamp=datetime.now(),
                                  user_id=user.id,
                                  hangout=signin_form.hangout.data,
                                  get_help=signin_form.get_help.data,
                                  computer=signin_form.computer.data,
                                  volunteer=signin_form.volunteer.data,
                                  dont_know=signin_form.dont_know.data,
                                  electronics_room=signin_form.electronics_room.data,
                                  laser_engraver=signin_form.laser_engraver.data,
                                  milling_machine=signin_form.milling_machine.data,
                                  three_d_printing=signin_form.three_d_printing.data,
                                  tour=signin_form.tour.data,
                                  vinyl_cutter=signin_form.vinyl_cutter.data,
                                  project = signin_form.project.data,
                                  project_art = signin_form.project_art.data,
                                  project_business = signin_form.project_business.data,
                                  project_research = signin_form.project_research.data,
                                  project_other = signin_form.project_other.data,
                                  projects = chosen_proj_str,
                                  for_class=signin_form.for_class.data,
                                  which_class=signin_form.which_class.data,
                                  other=signin_form.other.data,
                                  other_text=signin_form.other_text.data,
                                  )
                db.session.add(new_visit)
                db.session.commit()

                messg = '{} is signed in'.format(user.user_name)
                flash(messg, category='info')

    # did not validate, so return with the same signin form (otherwise won't be
    # able to see the errors)
    else:
        return render_template('base.html', anchor='signin',
                               signin_form=signin_form,
                               signup_form=SignUpForm(),
                               signed_in_users=get_signed_in_users())

    return redirect(url_for('.index'))


@app.route('/signout/<user_id>', methods=['GET', 'POST'])
def signout(user_id=None):
    """ description go here """
    ###########################################################################
    # Set signout timestamp for this user's current visit, and display message
    ###########################################################################
    # get this user, or send error messg if no user with this id
    user = User.query.get(user_id)
    if not user:
        messg = 'No such user'
        flash(messg, category='error')
    else:
        # Add signout_timestamp to this Visit, unless there is no current visit
        # (e.g. there may be no signout_timestamp -- which is involved in
        # get_current_visit() -- meaning that this user has already signed out or
        # never signed in.)
        try:
            # TODO: double check that try/except makes sense with
            # get_current_visit() possible return values
            #this_visit = user.get_current_visit()
            curr_visits = user.get_current_visits()
            for visit in curr_visits:
                visit.signout_timestamp = datetime.now()
                db.session.commit()

            messg = user.user_name + ' signed out.'
            flash(messg, category='info')
        except:
            messg = '{} was not signed in, and so cannot be signed out'.format(user.user_name)
            flash(messg, category='error')
    return redirect(url_for('.index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """ description go here """
    signup_form = SignUpForm()
    # process form - validate and store form data
    if signup_form.validate_on_submit():
        # TODO: checking for uniques before db.session.commit... does that make
        # sense?

        #######################################################################
        # Check that user with same username or same email does not already
        # exist
        #######################################################################
        # Make sure a user with the same user name does not already exist
        # (TODO: see various todo's about validation at this point vs when
        # adding to db)
        user_with_this_username = User.query.filter_by(user_name=signup_form.user_name.data).first()
        if signup_form.email.data == '':
            # user did not input an email address
            email = None
        else:
            # user IS signing up in with an email address
            email = signup_form.email.data;

        # TODO; logic flow at first glance seems screwed up in a silly way...
        # but it's actually screwed up in a complicated way. See Issue __
        if email:  # i.e. if email is not blank
            # if user did enter an email, check that noone else has the same
            # email
            # TODO: or just if User.query.filter_by(email=email) is not empty
            user_with_this_email = User.query.filter_by(email=email).first()
        else:
            # if user did not enter an email, she effectively does not share an
            # email with anyone else
            user_with_this_email = False

        if user_with_this_username:
            messg = 'User {} already exists'.format(signup_form.user_name.data)
            flash(messg, category='error')
            anchor = 'signup'  # remain on this tab, since there was an error
        # does this email already exist?
        elif (user_with_this_email != None and user_with_this_email):
            # TODO: more specific message, is it email or username that exists
            messg = 'User with email {} already exists'.format(email)
            flash(messg, category='error')
            anchor = 'signup'  # remain on this tab, since there was an error
        else:
            new_user = User(user_name=signup_form.user_name.data,
                            first_name=signup_form.first_name.data,
                            last_name=signup_form.last_name.data,
                            #email=signup_form.email.data,
                            email=email,
                            add_to_announce_list=signup_form.add_to_announce_list.data,
                            add_to_volunt_list=signup_form.add_to_volunt_list.data,
                            is_uiuc_student=signup_form.is_uiuc_student.data,
                            who_i_am=signup_form.who_are_you.data,
                            how_heard=signup_form.how_heard.data
                            )
            db.session.add(new_user)
            db.session.commit()

            messg = 'Created user {}'.format(signup_form.user_name.data)
            flash(messg, category='success')
            anchor = 'signin'  # return to signin tab after successful submit

    # Did not validate, i.e. we should remain on the sign up tab to show errors.
    else:
        anchor = 'signup'


    # If something went wrong, we need to remain on the sign up tab; otherwise
    # back to sign in tab.
    if anchor == 'signin':
        return redirect(url_for('.index'))
    else:
        return render_template('base.html', anchor=anchor,
                               signin_form=SignInForm(),
                               signup_form=signup_form,
                               signed_in_users=get_signed_in_users())


@app.route('/stats')
def stats():
    """ docstring """
    # TODO: sending keys is of course hacky......
    visit_keys = [key for key in Visit.__dict__.keys() if key[0] != '_']
    return render_template('stats.html', all_users=User.query.all(),
                           all_visits=Visit.query.all(),
                           visit_keys=visit_keys)


def get_signed_in_users():
    """ Return list of currently signed-in users by finding Visits that have
    signin timestamps, but no (auto)signout timestamps """

    # TODO: if no visits
    signed_in_visits = Visit.query.filter(Visit.signin_timestamp!=None,
                                          Visit.signout_timestamp==None,
                                          Visit.auto_signout_timestamp==None)
    signed_in_users = [v.visitor for v in signed_in_visits]
    return signed_in_users

