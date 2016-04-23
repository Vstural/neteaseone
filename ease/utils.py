
import urllib

def downloadImg(abs_path,url,name):

	path = abs_path+name

	try:
		data = urllib.urlopen(url).read()

		with open(path,'wb') as f:
			f.write(data)

	except Exception,e:
		print "image download error"
		print e
		return