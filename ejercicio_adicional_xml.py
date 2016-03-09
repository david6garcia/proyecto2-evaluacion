#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml import etree
datos=etree.parse('/bibliotecas.xml')
import sys
reload(sys)
sys.setdefaultencoding('utf8')

html=open("fichero.html", "w")
nombres=datos.xpath("//bibliotecas/biblioteca/nombre/text()")
direccion=datos.xpath("//bibliotecas/biblioteca/descripcion/text()")
latitud=datos.xpath("//bibliotecas/biblioteca/latitud/text()")
longitud=datos.xpath("//bibliotecas/biblioteca/longitud/text()")
contador=0

while contador<len(nombres):
	nom="<h1>"+nombres[contador]+"</h1>"
	descrip="<p>"+direccion[contador]+"</p>"
	mapa="<a href=\"http://www.openstreetmap.org/way/109089302#map=17/"+latitud[contador]+"/"+longitud[contador]+"\">Mapa</a>"
	html.write(nom+"\n")
	html.write(descrip+"\n")
	html.write(mapa+"\n")
	html.write("\n")
	contador=contador+1
html.close()
print nombres
