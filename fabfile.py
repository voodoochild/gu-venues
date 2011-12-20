import functools
import os

from fabric.api import local as _local

_local = functools.partial(_local, capture=False)

def install_requirements():
    """Installs the python requirements from lib."""
    # Remove any existing versions.
    _local('rm -rf flask jinja2 werkzeug simplejson')
    
    # Extract the tar files.
    _local('tar xzf lib/Flask-0.8.tar.gz')
    _local('tar xf lib/Jinja2-2.6.tar')
    _local('tar xf lib/Werkzeug-0.8.1.tar')
    _local('tar xzf lib/simplejson-2.3.0.tar.gz')
    
    # Move the relevant files to the directory root.
    _local('mv Flask-0.8/flask .')
    _local('mv Jinja2-2.6/jinja2 .')
    _local('mv Werkzeug-0.8.1/werkzeug .')
    _local('mv simplejson-2.3.0/simplejson .')
    
    # Clean up after ourselves!
    _local('rm -rf Flask-0.8')
    _local('rm -rf Jinja2-2.6')
    _local('rm -rf Werkzeug-0.8.1')
    _local('rm -rf simplejson-2.3.0')
