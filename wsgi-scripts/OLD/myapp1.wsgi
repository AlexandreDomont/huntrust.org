#!/usr/bin/env python
"""
A simple WSGI test application.

Its main purpose is to show that WSGI support works (meaning that the
web server and the WSGI adaptor / support module are configured correctly).

As a nice plus, it outputs some interesting system / WSGI values as a nice
HTML table.

The main use of this script will be using the WSGI "application" defined
below within your production WSGI environment. You will use some code similar
to what you see at the end of this script to use the application from that
environment. For the special case of apache2/mod_wsgi, it shoud be possible
to directly use this file.

If you start this script from the commandline either with python2.5 or with
and older python + wsgiref module installed, it will serve the content on
http://localhost:8000/ - this is mainly for debugging THIS script.

@copyright: 2008 by MoinMoin:ThomasWaldmann
@license: Python License, see LICENSE.Python for details.
"""

import os.path, os, sys, glob

try:
    __file__
except NameError:
    __file__ = '?'

html_template = """\
<html>
<head>
 <title>WSGI Test Script</title>
</head>
<body>
 <h1>WSGI test script is working!</h1>
 <table border=1>
  <tr><th colspan=2>1. System Information</th></tr>
  <tr><td>Python</td><td>%(python_version)s</td></tr>
  <tr><td>Python Path</td><td>%(python_path)s</td></tr>
  <tr><td>Platform</td><td>%(platform)s</td></tr>
  <tr><td>Absolute path of this script</td><td>%(abs_path)s</td></tr>
  <tr><td>Filename</td><td>%(filename)s</td></tr>
  <tr><th colspan=2>2. WSGI Environment</th></tr>
%(wsgi_env)s
  <tr><th colspan=2>3. Search</th></tr>
%(search)s
 </table>
</body>
</html>
"""

row_template = "  <tr><td>%s</td><td>%r</td></tr>"


def application(environ, start_response):
    """ The WSGI test application """
    # emit status / headers
    status = "200 OK"
    headers = [('Content-Type', 'text/html'), ]
    start_response(status, headers)

    out = []
    for f in glob.iglob("/var/www/wsgi-scripts/*.txt"): # generator, search immediate subdirectories 
    	out.append(f)

    # assemble and return content
    content = html_template % {
        'python_version': sys.version,
        'platform': sys.platform,
        'abs_path': os.path.abspath('.'),
        'filename': __file__,
        'python_path': repr(sys.path),
        'wsgi_env': '\n'.join([row_template % item for item in environ.items()]),
	'search': '\n <br>'.join(out),
    }
    return [content]

