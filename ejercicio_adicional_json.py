#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

fichero=open("/asociaciones-deportivas.json","r")
datos=json.load(fichero)
html=open("fichero.html", "w")
for dato in datos:
	nom="<h1>"+dato["nombre"]+"</h1>"
	direc="<p>"+dato["direccion"]+"</p>"
	email="<a href=\"mailto:email del club\">"+dato["email"]+"</a>"
	html.write(nom+"\n")
	html.write(direc+"\n")
	html.write(email+"\n")
	html.write("\n")
html.close()
