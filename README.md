fab-lab-signin
==============

Sign in to the Fab Lab space and other things, powered by Flask/SQLite.
Extending and porting from PHP/MySQL.


Installing and Running
--------------------------

The Quick Version
'''''''''''''''''''
* Clone this repository
* Set up and activate a virtual environment
* ```$ pip install -r requirements.txt```
* ```$ python db_create.py```
* optional: ```$ python make_fakes.py``` (create initial data)
* ```$ python run.py```
*  Go to http://127.0.0.1:5000/signin

The Long Version
----------------
* Clone this repository or download the zip file

* cd into the *fab-lab-signin* directory (if you download the zip file,
continue on into the *fab-lab-signin-master* directory) -- you should end up in
the same directory that has *requirements.txt* at that point

* Set up your virtualenv and activate it like this:
```
$ virtualenv ve
$ source ve/bin/activate
```

* At this point your prompt should show "(ve)" in front of it, like:
```
(ve) $
```

* ```pip-install``` all the requirements (the various libraries and things that
are needed to make the app work). It'll take a while, and the output will make
it  seem like there are tons of errors happening, but it's (probably) okay.
```
$ pip install -r requirements.txt
```

* Now you can create some fake data and run the site:
```
$ python make_fakes.py   #answer yes to the 'do you want to continue' question
$ python run.py
```

* now go to http://127.0.0.1:5000/  in your favorite browser (but note that this is meant to run in Chrome)

* To stop ``run.py``, type cntrl-C
