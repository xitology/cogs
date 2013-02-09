
from cogs import task
import os

@task
def Hello(name=None):
    """greet someone (if not specified, the current user)"""
    if name is None:
        name = os.getlogin()
    print "Hello, %s!" % name.capitalize()

