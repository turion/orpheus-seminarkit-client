#! /usr/bin/python
# -*- coding: utf-8 -*-

import cPickle
try:
	with open("lokale_berechnungen.pickle") as lokale_berechnungen_datei:
		lokale_berechnungen = cPickle.load(lokale_berechnungen_datei)
except IOError as IOError_instanz:
	if IOError_instanz.errno == 2: # errno 2 bedeutet dass die Datei nicht vorhanden ist. Dann wird sie neu erstellt.
		print "lokale_berechnungen.pickle existiert nicht, wird neu erstellt werden"
		lokale_berechnungen = {}
	else:
		handlung = ""
		while handlung not in ("e", "n"):
			raw_input("Warnung: lokale_berechnungen.pickle war unlesbar. Durch leere Datei ersetzen (e) oder nichts tun (n)?")
		if handlung == "e":
			lokale_berechnungen = {}
		if handlung == "n":
			exit("Nichts wird getan")

import xml.dom.minidom
anfrage_dokument = xml.dom.minidom.Document()
zahl = anfrage_dokument.createElement("zahl")
anfrage_dokument.appendChild(zahl)
zahl.appendChild(anfrage_dokument.createTextNode("23"))

import httplib, urllib
connection = httplib.HTTPConnection("www.orpheus-verein.de")
connection.request("POST", "/posttest.py", urllib.urlencode({"bla": "blub", "format": "xml", "xml": d.toxml()}))
print connection.getresponse().read()

TODO: cPickle save
