import glob, os, re, fnmatch

print "++++++++++++++++++++++++++++++++++++++++"

for file in glob.iglob("/var/www/huntrust/blog/articles/*.html"):
	print file
	article = file[32:]
	print article
	hand = open(file)
        for line in hand:
                line = line.rstrip()
                if re.search('name="description"', line) :
                        print line
			dsc=line.strip()
                        dsc = dsc[34:len(dsc)-2]
                        print dsc
		if re.search('<title>', line) :
                        print line
			title=line.strip()
                        title =  title[7:len(title)-8]
                        print title
	print '##########'		
print "++++++++++++++++++++++++++++++++++++++++"

