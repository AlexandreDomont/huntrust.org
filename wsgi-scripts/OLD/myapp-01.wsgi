#!/usr/bin/python

import cgitb
cgitb.enable()

print 'Content-type: text/html'
print

try:
    fichier = open('/var/www/wsgi-scripts/compteur','r')
    nbr_visiteurs = int(fichier.read())
except Exception:
    nbr_visiteurs = 0
    fichier = open('/var/www/wsgi-scripts/compteur','w')
fichier.write(str(nbr_visiteurs+1))
print nbr_visiteurs+1,'visites \o/'

def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
