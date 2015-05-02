import glob, os, re, fnmatch

out = []
for f in glob.iglob("/var/www/bootstrap/articles/*.html"): # generator, search immediate subdirectories 
	out.append(f[27:])

print out
print '\n'.join(out)

#res = [f for f in os.listdir() if res.search(r'(abc|123|a1b).*\.txt$', f)]
#for f in res:
#    print f


n = 100

sum = 0
for counter in range(1,n+1):
    sum = sum + counter

print sum

def reglob(path, exp, invert=False):
    """glob.glob() style searching which uses regex

    :param exp: Regex expression for filename
    :param invert: Invert match to non matching files
    """

    m = re.compile(exp)

    if invert is False:
        res = [f for f in os.listdir(path) if m.search(f)]
    else:
        res = [f for f in os.listdir(path) if not m.search(f)]

    res = map(lambda x: "%s/%s" % ( path, x, ), res)
    return res

#reglob('/var/www/bootstrap/articles/','host')

for file in os.listdir('/var/www/bootstrap/articles/'):
    if fnmatch.fnmatch(file, '\S+*and\S+host*'):
        print file

keyword_list = ['motorcycle', 'bike', 'cycle', 'dirtbike', "long"]
all_text = 'some rather long string'
if set(keyword_list).intersection(all_text.split()):
     print "Found One"

print "++++++++++++++++++++++++++++++++++++++++"
import re
for file in os.listdir('/var/www/bootstrap/articles/'):
	hand = open('/var/www/bootstrap/articles/'+file)
	for line in hand:
    		line = line.rstrip()
    		if re.search('name="description"', line) :
			print line
        		res = line[38:]
			res.translate(None, '">')
                        print res

