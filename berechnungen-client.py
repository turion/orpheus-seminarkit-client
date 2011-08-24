#! /usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
class Berechnung(object):
	def test(self):
		raise NotImplementedError
	def rechne(self, daten):
		raise NotImplementedError
	def verschicke(self): #TODO: Vielleicht doch Multipartupload => eher Funktion
		raise NotImplementedError
	def status(self):
		raise NotImplementedError

class TexBerechnung(Berechnung):
	"""TODO: muss feststellen ob tex vorhanden ist, ansonsten ImportError erzeugen
	TODO: hochladen mit:
		! https://github.com/seisen/urllib2_file/ (Jemand behauptet dass das veraltete Bibliotheken verwendet)
		http://code.activestate.com/recipes/146306-http-client-to-post-using-multipartform-data/
		! http://uthcode.sarovar.org/pythonsnippets.html
		!! http://www.2maomao.com/blog/python-http-post-a-binary-file-using-urllib2/"""
	def test(self):
		try:
			self.prozess = subprocess.Popen("pdflatex", stdout=subprocess.PIPE)
		except OSError as fehler:
			if fehler.errno == 2:
				return False
			else:
				raise
		else:
			self.prozess.terminate()


class StundenplanBerechnung(Berechnung):
	pass

berechnungen = {"tex" : TexBerechnung, "stundenplan": StundenplanBerechnung}
for typ in berechnungen:
	if not berechnungen[typ].test(): # Der Test schlägt fehl: Wahrscheinlich fehlt eine Voraussetzung. In diesen Fällen kann eine Berechnung dieses Typs nicht durchgeführt werden, daher wird der entsprechende Eintrag in berechnungen gelöscht.
		del berechnungen[typ]

import shelve
lokale_berechnungen = shelve.open("lokale_berechnungen.shelve", writeback=True)
foreach key in ["zu rechnen", "zu verschicken", "fertig"]:
	if key not in lokale_berechnungen:
		lokale_berechnungen[key] = []

import xml.dom.minidom
anfrage_dokument = xml.dom.minidom.Document()
zahl = anfrage_dokument.createElement("zahl")
anfrage_dokument.appendChild(zahl)
zahl.appendChild(anfrage_dokument.createTextNode("23"))

import httplib, urllib
connection = httplib.HTTPConnection("www.orpheus-verein.de")
connection.request("POST", "/posttest.py", urllib.urlencode({"bla": "blub", "format": "xml", "xml": d.toxml()}))
print connection.getresponse().read()
