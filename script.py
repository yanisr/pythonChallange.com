# Auteur: yanis.r
# Se script contient des fonctions permettant de résoudre les challanges proposé par le site http://www.pythonchallenge.com

import urllib.request
from re import sub
import time
import pickle
import zipfile


# url de départ: http://www.pythonchallenge.com/pc/def/0.html
# réultat: 
def un():
	print(str(2**38))

# url de départ: 
# réultat: 
def quatre():
	s = "37278"
	while(len(s)>0):
		content = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + s).read()
		print(s + ": " + str(content))
		s = str(sub("[^0-9]*", "", str(content)))

# url de départ: 
# réultat: 
def cinq():
	data = pickle.loads(urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read())
	for line in data:
   		print (''.join(elmt[0] * elmt[1] for elmt in line))
   		# ca écrit "channel"

# url de départ: 
# réultat: 
def six():
	s = "90052"
	zipFile = zipfile.ZipFile("channel.zip")
	while(True):
		contenu = zipFile.read(s + ".txt")
		print(s + ": " + str(contenu) + ": " + str(zipFile.getinfo(s+".txt").comment))
		s = str(sub("[^0-9]*", "", str(contenu)))
		#dans les commentaires, on voit que ca ecrit oxygen
		#http://www.pythonchallenge.com/pc/def/oxygen.html