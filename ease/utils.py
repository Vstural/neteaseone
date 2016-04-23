
import urllib2
import socket
import time

log_path = 'log.txt'

def downloadImg(abs_path,url,name):
	i = 0
	while(downloader(abs_path, url, name) != 0 and i < 3):
		i = i+1
		



def downloader(abs_path,url,name):
	path = abs_path+name

	try:
		data = urllib2.urlopen(url,timeout=5).read()

		with open(path,'wb') as f:
			f.write(data)

		return 0
	except Exception,e:
		print("image download error")
		print(e)

		with open(log_path,'a') as log:
			log.write(str(time.asctime(time.localtime(time.time())))+":"+e+"\n")
		return 1

	except socket.timeout,e:
		print("download image timeout")
		
		with open(log_path,'a') as log:
			log.write(str(time.asctime(time.localtime(time.time())))+":"+e+"\n")
		return 1
