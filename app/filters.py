#!/usr/bin/env python

from app import app
from datetime import datetime

@app.template_filter(nice_datetime)
def nice_datetime(date_time):
    """ Format datetime nicely
    NOTE: defunct - this has been supplanted by the User.get_time_in() function
    """
    return date_time.strftime('%l:%M %p, %b %e, %Y')

