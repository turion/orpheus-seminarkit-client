#! /usr/bin/python
# -*- coding: utf-8 -*-

import shelve

lokale_berechnungen = shelve.open("lokale_berechnungen.shelve", writeback=True)

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
