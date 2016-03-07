#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from pprint import pprint


fichero=open("/media/DAVID/asociaciones-deportivas.json","r")
datos=json.load(fichero)
opc=raw_input("\n\n 1. Listar los nombres de las asociaciones deportivas de la provincia de Lorca.\n 2. Contar las asociaciones deportivas cuya fecha de constitución sea anterior a un año dado.\n 3. Listar las direcciones de las asociaciones deportivas que empiecen por una letra dada.\n 4. Mostrar el teléfono de contacto de una asociación buscada.\n 5. Listar los nombres y los correos electrónicos de aquellas asociaciones cuyo correo electrónico sea de gmail.\n Q  Para salir\n\nElige una opcion: ")
print "\n"
while opc!="q" and opc!="Q":
	if opc=="1":
		for nomb in datos:
			print nomb["nombre"]
			
	elif opc=="2":
		fechinsert=int(raw_input("Dime el año: "))
		fechas=[]
		fechasanterior=[]
		for dat in datos:
			x=str(dat["fconstitucion"])
			f=x.split("T")
			f1=f[0].split("-")
			fechas.append(f1[0])
		for fec in fechas:
			if fec!="":
				if int(fec)<=fechinsert:
					fechasanterior.append(fec)					
		print "Existen %i asociaciones anteriores al año %i" % (len(fechasanterior),fechinsert)		
		
	elif opc=="3":
		comienzo=raw_input("Dime el comienzo del nombre de las asociaciones que quieres buscar: ")
		print "\n"
		for n in datos:
			if n["nombre"].startswith(comienzo)==True:
				print "%s se encuetra en %s \n" % (n["nombre"], n["direccion"])
				
	elif opc=="4":
		busca=raw_input("Dime la asociacion que buscas: ")
		for h in datos:
			if h["nombre"].count(busca)>=1:
				if h["telefono"]!="":
					print "%s tiene asociado el telefono %s \n" % (h["nombre"], h["telefono"])
					
	elif opc=="5":
		for d in datos:
			if d["email"].count("@gmail.com")==1:
				print "%s tiene asociado el correo electronico %s \n" % (d["nombre"], d["email"])
	opc=raw_input("\n 1. Listar los nombres de las asociaciones deportivas de la provincia de Lorca.\n 2. Contar las asociaciones deportivas cuya fecha de constitución sea anterior a un año dado.\n 3. Listar las direcciones de las asociaciones deportivas que empiecen por una letra dada.\n 4. Mostrar el teléfono de contacto de una asociación buscada.\n 5. Listar los nombres y los correos electrónicos de aquellas asociaciones cuyo correo electrónico sea de gmail.\n Q  Para salir\n\nElige una opcion: ")
	print "\n"
print "HASTA LUEGO\n"
