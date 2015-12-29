# Auteur: yanis.r
# Se script contient des fonctions permettant de résoudre les challanges proposé par le site http://www.pythonchallenge.com

from collections import Counter
import urllib.request
from re import *
import time
import pickle
import zipfile


# url de départ: http://www.pythonchallenge.com/pc/def/0.html
# réultat: www.pythonchallenge.com/pc/def/274877906944.html
# puissance
def zero():
	print(str(2**38))

# url de départ: http://www.pythonchallenge.com/pc/def/map.html
# réultat: http://www.pythonchallenge.com/pc/def/ocr.html
# chiffrement de césar
def un(text, incr):
	ret = ""
	for c in range(len(text)):
		if text[c].isalpha(): 
			ret = ret + chr((ord(text[c])-96 + incr)%26 + 96)
		else:
			ret = ret + text[c]
	print(ret)

# url de départ: http://www.pythonchallenge.com/pc/def/ocr.html
# réultat: http://www.pythonchallenge.com/pc/def/equality.html
# charactere les plus rare: etyluqia anagramme de "equality"
def deux(textPath):
	print(Counter(open(textPath, "r").read()))

# url de départ: http://www.pythonchallenge.com/pc/def/equality.html
# réultat: http://www.pythonchallenge.com/pc/def/linkedlist.html
# retourne le caractere entourés d'éxactement 3 majuscules à droit et à gauche
def trois(textPath):
	text = open(textPath, "r").read()
	tab = findall("[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}", open("res/trois.res","r").read())
	for c in tab:
		print(c[4])

# url de départ: http://www.pythonchallenge.com/pc/def/linkedlist.php
# réultat: http://www.pythonchallenge.com/pc/def/peak.html
# cherche le prochain numéro de page à passer en parametre jusqu'a trouver une autre graine
def quatre(seed):
	while(len(seed)>0):
		content = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + seed).read()
		print(seed + ": " + str(content))
		seed = str(sub("[^0-9]*", "", str(content)))

# url de départ: http://www.pythonchallenge.com/pc/def/peak.html
# réultat: http://www.pythonchallenge.com/pc/def/channel.html
# réconstitu le fichier pickle et le caractere au nombre de fois qu'il doit s'afficher.
def cinq(pathPickleFile):
	data = pickle.loads(open(pathPickleFile, "rb").read()) # on récupere les données
	ret = ""
	for line in data:
		l = ""
		for elmt in line:
			l = l + elmt[0] * elmt[1]
		ret = ret + l + "\n"
		print(ret)

# url de départ: http://www.pythonchallenge.com/pc/def/channel.html
# réultat: http://www.pythonchallenge.com/pc/def/oxygen.html
# ressource: d'apres le README, on prend comme graine 90052
def six(zipPath, seed):
	zipFile = zipfile.ZipFile(zipPath)
	while(True):
		contenu = zipFile.read(seed + ".txt")
		commentaire = zipFile.getinfo(seed + ".txt").comment
		print(seed + "\t" + str(contenu) + "\t" + str(commentaire))
		seed = str(sub("[^0-9]*", "", str(contenu)))
		if len(seed) == 0: break;
		#dans les commentaires, on voit que ca ecrit oxygen