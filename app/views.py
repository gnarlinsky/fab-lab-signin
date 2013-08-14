from flask import render_template, flash, redirect
from app import app
from forms import SigninForm

@app.route('/')
# TODO: double check on methods argument below, esp need for 'POST'
@app.route('/signin', methods = ['GET', 'POST'])
def signin():
    # define var template variables
    title = 'Fab Lab Sign-in'
    user = {'nickname': 'Jane'}  # test user
    # just to illustrate looping
    stuff = [ {'key1': 'value1', 'key2': 'value2'},
              {'key1': 'bar', 'key2': 'foo'} ]

    # instantiate a Form object
    form = SigninForm()
    # process form - validate and store form data
    if form.validate_on_submit():
        # if validate_on_submit is called when the form is actually being
        # submitted, this will return True - if it successfully gathered and
        # validated the data

        # flash(): quick way to show a message after form submission
        #  currently just displays submitted data
        # (see 'with messages = get_flashed_messages()' in template
        messg = 'User: {}; checked boxes: {}.'.format(form.user_name.data,
                                                      '(not implem)')
        flash(messg)
        # but we're just one page/template...
        #return redirect('/somewhere')


    # else - if validate_on_submit is being called AS the form is being presented
    # to user, *before* the user has entered any data, it will return
    # False. This indicates that we have to render the template.
    # validate_on_submit could also have returned False if something went wrong
    # during form processing, which means we go back to the form, i.e. render
    # the template
    return render_template('signin.html', title=title, user=user, form=form,
                            stuff=stuff)
