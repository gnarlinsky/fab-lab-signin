from flask.ext.wtf import Form, TextField, BooleanField
from flask.ext.wtf import Required

class SigninForm(Form):
    # todo: remove password stuff -- login use case does not actually require a
    # password, but doing this just for fun right now. 
    user_name = TextField('user_name', validators = [Required()])
    # Required is a validator -- a function that gets attached to a field to
    # validate its data. The Required validator specifically checks that the
    # field is not empty.
