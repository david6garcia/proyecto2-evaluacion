#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml import etree
doc=etree.parse('/media/DAVID/bibliotecas.xml')

opc=raw_input("\n\n1. Listar el nombre de todas las Bibliotecas de la provincia de Lorca.\n2. Contar las bibliotecas que abren los Sábados.\n3. Listar las bibliotecas que empiecen por una letra indicada.\n4. Mostrar el horario de una biblioteca buscada.\n5. Mostrar las coordenadas de una biblioteca buscada.\nQ Para salir\n\nElige una opcion: ")
print "\n"
while opc!="q" and opc!="Q":
	if opc=="1":
		nombres=doc.xpath("//bibliotecas/biblioteca/nombre/text()")
		for n in nombres:
			print n
		
	elif opc=="2":
		dia=raw_input("Dime un día de la semana: ")
		print "\n"
		c=doc.xpath("count(biblioteca/horario/"+dia+")")
		print "Existen %i bibliotecas que abren el %s." % (int(c),dia)
		
	elif opc=="3":
		letra=raw_input("Buscar: ")
		print "\n"
		empiezan=doc.xpath("//nombre[contains(text(),'"+letra+"')]/text()")
		for e in empiezan:
			print e
			
	elif opc=="4":
		busca=raw_input("Buscar: ")
		print "\n"
		biblio=doc.xpath("//nombre[contains(text(),'"+busca+"')]/text()")
		bibliotecas=doc.getroot()
		for b in bibliotecas:
			if b.find('nombre').text==biblio[0]:
				horario=b.find('horario')
				print "El horario de apertura de %s es:" % (biblio[0])
				for dia in horario:
					print "\t--> %s: %s" % (dia.tag, dia.text)
					
	elif opc=="5":
		letra=raw_input("Buscar: ")
		print "\n"
		biblio=doc.xpath("//nombre[contains(text(),'"+letra+"')]/text()")
		bibliotecas=doc.getroot()
		for b in bibliotecas:
			if b.find('nombre').text==biblio[0]:
				longitud=b.find('longitud')
				latitud=b.find('latitud')
				print "Longitud: %s \nLatitud: %s" % (longitud.text, latitud.text)
				#print "https://www.google.es/maps/@%s,-%sz" % (longitud.text, latitud.text)
	opc=raw_input("\n\n1. Listar el nombre de todas las Bibliotecas de la provincia de Lorca.\n2. Contar las bibliotecas que abren los Sábados.\n3. Listar las bibliotecas que empiecen por una letra indicada.\n4. Mostrar el horario de una biblioteca buscada.\n5. Mostrar las coordenadas de una biblioteca buscada.\nQ Para salir\n\nElige una opcion: ")
	print "\n"
print "HASTA LUEGO\n"
