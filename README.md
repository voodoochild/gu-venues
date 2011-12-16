Guardian Venues
===============

This is a 'fail fast' experiment to use the Press Association API to present information about venues and events on guardian.co.uk.

**To run the project locally with App Engine:**

_Extract the various python libs in lib/ to the document root, e.g._

  `$ tar xzf lib/Flask-0.8.tar.gz`
  
  `$ mv Flask-0.8/flask/ .`
  
  `$ rm -rf Flask-0.8/`

_Then run it:_

  `$ dev_appserver.py .`
