#!/usr/bin/python

from socket import *
import optparse
from threading import *

def connectScan(thost,tport):
	try:
		s=socket(AF_INET,SOCK_STREAM)
		s.connect((thost,tport))
		print '[+]%d/tcp Open' %tport
	except:
		print '[-]%d tcp closed' %tport
	finally:
		s.close() 

def portScan(thost,tport):
	try:
		tIp=gethostbyname(thost)
	except:
		print 'Unknown host %s ' %thost
	try:
		tname=gethostbyaddr(tIp)
		print '[+]Scan results for :' +tname[0]
	except:
		print '[+]Scan results for: '+tIp
	setdefaulttimeout(1)

	for tp in tport:
		t=Thread(target=connectScan,args=(thost,int(tp)))
		t.start()
def main():
	parser= optparse.OptionParser('Usageof program: '+'-H <target host> -p<target port>')
	parser.add_option('-H',dest='targethost',type='string',help='specify target host')
	parser.add_option('-p',dest='targetport',type='string',help='specify target port seperated by comma')
	(options,args)=parser.parse_args()
	targethost=options.targethost
	targetport=str(options.targetport).split(',')

	if (targethost==None) | (targetport[0]==None):
		print parser.usage
		exit(0)
	portScan(targethost,targetport)

if __name__=='__main__':
	main()
