#!/usr/bin/env python

#from wsgiref.simple_server import make_server
from cgi import parse_qs, escape, os
import glob

html = """
<html>
<body>
   <form method="post" action="myapp">
      <p>
         Age: <input type="text" name="age">
         </p>
      <p>
         Hobbies:
         <input name="hobbies" type="checkbox" value="software"> Software
         <input name="hobbies" type="checkbox" value="tunning"> Auto Tunning
         </p>
      <p>
         <input type="submit" value="Submit">
         </p>
      </form>
   <p>
      Age: %s<br>
      Hobbies: %s<br>
	GG: %s<br>
	Liste of file : %s<br>
   </p>
   </body>
</html>
"""

def application(environ, start_response):

   # the environment variable CONTENT_LENGTH may be empty or missing
   try:
      request_body_size = int(environ.get('CONTENT_LENGTH', 0))
   except (ValueError):
      request_body_size = 0

   # When the method is POST the query string will be sent
   # in the HTTP request body which is passed by the WSGI server
   # in the file like wsgi.input environment variable.
   request_body = environ['wsgi.input'].read(request_body_size)
   d = parse_qs(request_body)

   age = d.get('age', [''])[0] # Returns the first age value.
   hobbies = d.get('hobbies', []) # Returns a list of hobbies.

   # Always escape user input to avoid script injection
   age = escape(age)
   hobbies = [escape(hobby) for hobby in hobbies]

   f = 'toto'
   n = 100
   sum = 0

   for counter in range(1,n+1):
	sum = sum + counter

#   for f in glob.iglob("/var/www/wsgi-scripts/*.txt"): # generator, search immediate subdirectories 
#	print f 

   out = []
   for f in glob.iglob("/var/www/wsgi-scripts/*.txt"): # generator, search immediate subdirectories 
   	out.append(f)

   response_body = html % (age or 'Empty',
               ', '.join(hobbies or ['No Hobbies']), sum, out)

   status = '200 OK'

   response_headers = [('Content-Type', 'text/html'),
                  ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)

   return [response_body]
