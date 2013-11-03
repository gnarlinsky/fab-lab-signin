from flask.ext.wtf import Form, TextField, TextAreaField, BooleanField, Email,\
                          Length, Optional, Required

class SignUpForm(Form):
    """ description go here """    # TODO
    user_name = TextField(label='User Name',
        validators=[Length(min=1, max=25),
        Required('Please provide a user name.')]
        )
    first_name = TextField(label='First Name',
        validators=[Required('Please provide your first name.')]
        )
    last_name = TextField(label='Last Name',
        validators=[Required('Please provide your last name.')]
        )
    # TODO: make note in docs:  The Optional validator must be there;
    # otherwise, it seems that the presence of the Email validator implies
    # Required validator.
    # TODO: if this user did not provide an email, we'll think that every other
    # user who did not provide an email is the same -- because the
    # Optional() validator in forms.py apparently does not account for
    # empty things not actually being unique.  And setting default=None did
    # not help.
    # (see similar comment in views.py)
    email = TextField(label='Email',
        validators=[Optional(strip_whitespace=True),
                    Email('Please provide a valid email address.'),
                   ]
        )
    add_to_announce_list = BooleanField(
        label='Can we add you to the announcement listserv?',
        default=False)
    add_to_volunt_list = BooleanField(
        label='Can we add you to the volunteer listserv?',
        default=False)
    is_uiuc_student = BooleanField(label='Are you a student at UIUC?')
    who_are_you = TextField(label='If not, please tell us what you do')
    how_heard = TextField(label='How did you hear about us?')


class SignInForm(Form):
    """ description go here """    # TODO
    # TODO: is there a parameter for ``autocomplete='off'``?
    user_name_or_email = TextField(label='User Name or Email',
        validators=[Required('Please provide your user name or email address.')]
        )

    # Lab use checkboxes
    dont_know = BooleanField(label="Don't Know")
    volunteer = BooleanField(label='Volunteer')
    get_help = BooleanField(label='Get help')
    hangout = BooleanField(label='Hangout')
    computer = BooleanField(label='Computer')
    electronics_room = BooleanField(label='Electronics Room')
    laser_engraver = BooleanField(label='Laser Engraver')
    milling_machine = BooleanField(label='Milling Machine')
    three_d_printing = BooleanField(label='3D Printing')
    tour = BooleanField(label='Tour')
    vinyl_cutter = BooleanField(label='Vinyl Cutter')
    project = BooleanField(label='Project')
    project_art = BooleanField(label='Art')
    project_business = BooleanField(label='Business')
    project_research = BooleanField(label='Research')
    project_other = TextField(label='Other')
    for_class = BooleanField(label='For a class')
    which_class = TextField(label='Which class?')
    other = BooleanField(label='Other')
    other_text = TextField(label='Please describe:')
