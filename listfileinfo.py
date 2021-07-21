import os
import sys
from mobi import Mobi

os.chdir("..") # changes cwd to the folder above

def getInfo(file):
	book = Mobi(file);
	book.parse();
	t = ""
	a = ""
	try:
		t = book.title()
	except:
		t = "<Error>"
	try:
		a = book.author()
	except:
		a = "<Error>"
	return t + ";" + a

for f in os.listdir(os.getcwd()):
	if f.endswith(".mobi"):
		i = getInfo(f)
		print(i + ";" + f)
	else:
		continue
