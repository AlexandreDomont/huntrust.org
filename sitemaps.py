#!/usr/bin/env python

from cgi import parse_qs, escape, os
import os.path, sys, glob, re, fnmatch

NomFichier = 'blog/sitemap.xml'
Fichier = open(NomFichier,'w')

Fichier.write('<?xml version="1.0" encoding="UTF-8"?>')
Fichier.write('\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
Fichier.write('\n<url>')
Fichier.write('\n<loc>http://hunstrust.org/</loc>')
Fichier.write('\n</url>')
Fichier.write('\n<url>')
Fichier.write('\n<loc>http://hunstrust.org/about.html</loc>')
Fichier.write('\n</url>')



for file in glob.iglob("/var/www/huntrust/blog/articles/*.html"):
	        print file
        	article = file[32:]
        	#out.append(article)
		print article
		Fichier.write('\n<url>')
		Fichier.write('\n<loc>http://hunstrust.org/'+ article + '</loc>')
		Fichier.write('\n</url>')

Fichier.write('\n</urlset>')

Fichier.close()

