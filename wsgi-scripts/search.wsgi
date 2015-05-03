#!/usr/bin/env python

#from wsgiref.simple_server import make_server
from cgi import parse_qs, escape, os
import os.path, sys, glob, re, fnmatch

html = """

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>Blog Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="../css/bootstrap.css" rel="stylesheet">
    <link href="../css/hunt.css" rel="stylesheet">


    <!-- Custom styles for this template -->
    <link href="../css/blog.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="../../assets/js/ie-emulation-modes-warning.js"></script>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
  </head>

  <body>

	<div class="container">

		<div class="header clearfix">
		<div id="menu"></div>
                	<script>
                		$( "#menu" ).load( "../templates/menu.html" );
                	</script>
		</div>
      		</div>
	</div>

	<div class="container">
      	<div class="blog-header">
        	<h1 class="blog-title">Result search :  %(keys)s </h1>
      	</div>

      	<div class="row">
	<div class="col-sm-8 blog-main">
	   <p>
	      Keys: %(keys)s<br>
	      Artciles : <br>%(search)s
	   </p>
	</div>
	</div>

	</div><!-- /.container -->

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

   keys = d.get('keys', [''])[0] # Returns the first age value.

   # Always escape user input to avoid script injection
   keys = escape(keys)

##
   #keyword_list = ['motorcycle', 'bike', 'cycle', 'dirtbike', "long"]
   keyword_list = keys.lower()
   keyword_list = keyword_list.split()
#   all_text = 'DNS'
#   all_text = all_text.lower()
#   if set(keyword_list).intersection(all_text.split()):
#	oui = 'Oui'
#   else:
#	oui = 'Non'	
##
   out = []
#   for f in glob.iglob("/var/www/huntrust/blog/articles/*.html"):  
#   	out.append(f)
##

   for file in glob.iglob("/var/www/huntrust/blog/articles/*.html"):
	        #print file
        	article = file[32:]
        	#out.append(article)
        	hand = open(file)
        	for line in hand:
                	line = line.rstrip()
                	if re.search('name="description"', line) :
                        	#print line
                        	dsc=line.strip()
                        	dsc = dsc[34:len(dsc)-2]
                       # 	out.append(dsc)
                	if re.search('<title>', line) :
                        	#print line
                        	title=line.strip()
                        	title =  title[7:len(title)-8]
                        #	out.append(title)
		result = '<a href="articles/' + str(article) + '">' + str(title) +'</a>'
		all_text = dsc
   		all_text = all_text.lower()

		if set(keyword_list).intersection(all_text.split()):
			out.append(result)
			out.append('Description : ' + str(dsc) +'</br>')
			oui = 'Match'
##
   response_body = html % {
	'keys': keys or 'Empty', 
	'search': '\n <br>'.join(out),
	}

   status = '200 OK'

   response_headers = [('Content-Type', 'text/html'),
                  ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)

   return [response_body]
