fab-lab-signin
==============

Sign in to the Fab Lab space and other things, powered by Flask/SQLite.
Extending and porting from PHP/MySQL.


Installing and Running
--------------------------
* Clone this repository
* ```$ git checkout develop``` (make sure you're in the "develop" branch)
* Set up and activate a virtual environment
* ```$ pip install -r requirements.txt```
* ```$ python db_create.py```
* optional: ```$python make_fakes.py``` (create initial data)
* ```$ python run.py```
*  Go to http://127.0.0.1:5000/signin
