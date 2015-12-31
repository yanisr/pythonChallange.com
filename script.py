#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur: yanis.r
# Se script contient des fonctions permettant de résoudre les challanges proposé par le site http://www.pythonchallenge.com

from collections import Counter
#import urllib.request
from re import *
import time
import pickle
import zipfile
import Image
import bz2

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
def six(seed):
	zipFile = zipfile.ZipFile("res/channel.zip")
	while(True):
		contenu = zipFile.read(seed + ".txt")
		commentaire = zipFile.getinfo(seed + ".txt").comment
		print(seed + "\t" + str(contenu) + "\t" + str(commentaire))
		seed = str(sub("[^0-9]*", "", str(contenu)))
		if len(seed) == 0: break;
		#dans les commentaires, on voit que ca ecrit oxygen

# url de départ: http://www.pythonchallenge.com/pc/def/oxygen.html
# réultat: http://www.pythonchallenge.com/pc/def/integrity.html
# list(map(chr,[105,110,116, 101, 103, 114, 105, 116, 121])) = integrity
def sept():
	img = Image.open("res/oxygen.png")
	tabGris = [img.getpixel((x,45))[0] for x in range(0, 607, 7)]
	tabChar = list(map(chr, tabGris))
	print("".join(tabChar))


# url de départ: http://www.pythonchallenge.com/pc/def/integrity.html
# réultat: un = "huge", px = "file"
def huit():
	print(bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))
	print(bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'))


# url de départ: http://www.pythonchallenge.com/pc/return/good.html
# résultat: http://www.pythonchallenge.com/pc/return/bull.html
# les pixels déssinent un taureau
def neuf():
	first = open("res/first.txt", "r").read().split(",")
	second = open("res/second.txt", "r").read().split(",")
	l = [int(a)+int(b) for a, b in zip(first, second + [0]*(len(first)-len(second)))]
	coo = []
	for c in range(0,len(l)-1, 2):
		coo.append((l[c], l[c+1]))
	
	img = Image.open("res/good.jpg")
	newImg = Image.new(img.mode, img.size)

	for y,x in coo:
		newImg.putpixel((x,y), (255,255,255))

	newImg.save("res/newImg.jpg")

# url de départ: http://www.pythonchallenge.com/pc/return/bull.html
# résultat: http://www.pythonchallenge.com/pc/return/5808.html
# affiche la taille des termes de la suite de conway
def dix():
	table = {
		'1': '11',
		'11': '21',
		'111': '31',
		'2': '12',
		'22': '22',
		'222': '32',
		'3': '13',
		'33': '23',
		'333': '33'
	}
	val = '1'
	ret = [1]
	for i in range(30):
		newVal = sep(val)
		for j in range(len(newVal)):
			newVal[j] = table[newVal[j]]
		val = "".join(newVal)
		ret.append(len(val))
	print(ret)

# sépare une chaine de caractere lors d'un changement de caractere
# sep('11211122')retourne ['11', '2', '111', '22']
def sep(suite):
	tab = [c for c in suite]
	ret = [suite[:1]]
	for cour in range(1,len(tab)):
		if tab[cour] == ret[len(ret)-1][-1:]:
			ret[len(ret)-1] = ret[len(ret)-1] + tab[cour]
		else :
			ret.append(tab[cour])
	return ret


# url de départ: http://www.pythonchallenge.com/pc/return/5808.html
# résultat: http://www.pythonchallenge.com/pc/return/evil.html
# applique un filtre (damier de pixel) su la photo
def onze():
	img = Image.open("res/cave.jpg")
	newImg = Image.new(img.mode, img.size)
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			if (x%2 == 0 and y%2 == 0) or (y%2 == 1 and x%2 ==1):
				newImg.putpixel((x,y), img.getpixel((x,y)))
			else:
				newImg.putpixel((x,y), (255,255,255))
	newImg.save("res/newOnze.jpg")

