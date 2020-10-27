import requests
import os
import sys

i = 0
a = 0
b = 0
c = 0

def Url(var1 = "0",var2 = "0",var3 = "0",var4 = "0"):
	urlf = "http://{}.{}.{}.{}"
	urlf= urlf.format(var1,var2,var3,var4)
	return urlf

def TestWeb(url):
	try:
		res = requests.get(url,timeout=0.1)
		print("webpage found")
	except:
		print("no webpage")
url = Url()


def stepone():
	for i in range(0,1000):
		url = Url(i)
		TestWeb(url)
	steptwo()

def steptwo():
	for i in range(0,1000):
		for a in range(0,1000):
			url = Url(i,a)
			TestWeb(url)
	stepthree()
def stepthree():
	for i in range(0,1000):
		for a in range(0,1000):
			for b in range(0,1000):
				url = Url(i,a,b)
				TestWeb(url)

def stepfour(i):
	for i in range(0,1000):
		for a in range(0,1000):
			for b in range(0,1000):
				for c in range(0,1000):
					url = Url(i,a,b,c)
					TestWeb(url)

stepone()