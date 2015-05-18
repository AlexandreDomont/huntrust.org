#!/usr/bin/env python

import os.path, sys, glob, re, os

NomFichier = 'blog/sitemap.xml'
Fichier = open(NomFichier,'w')

Fichier.write('<?xml version="1.0" encoding="UTF-8"?>')
Fichier.write('\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
Fichier.write('\n<url>')
Fichier.write('\n<loc>http://huntrust.org/</loc>')
Fichier.write('\n</url>')
Fichier.write('\n<url>')
Fichier.write('\n<loc>http://huntrust.org/about-alexandre-domont.html</loc>')
Fichier.write('\n</url>')

for file in glob.iglob("/var/www/huntrust/blog/articles/*.html"):
        	article = file[32:]
		Fichier.write('\n<url>')
		Fichier.write('\n<loc>http://huntrust.org/articles/'+ article + '</loc>')
		Fichier.write('\n</url>')

Fichier.write('\n</urlset>')

Fichier.close()

