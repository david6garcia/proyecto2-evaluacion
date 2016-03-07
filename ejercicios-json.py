#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from pprint import pprint

lista=[]
fichero=open("/home/usuario/Descargas/asociaciones-deportivas.json","r")
datos=json.load(fichero)
opc=raw_input("\n\n 1. Listar los nombres de las asociaciones deportivas de la provincia de Lorca.\n 2. Contar las asociaciones deportivas cuya fecha de constitución sea anterior al 2006.\n 3. Listar las direcciones de las asociaciones deportivas que empiecen por una letra dada.\n 4. Mostrar el teléfono de contacto de una asociación buscada.\n 5. Listar los nombres y los correos electrónicos de aquellas asociaciones cuyo correo electrónico sea de gmail.\n Q  Para salir\n\nElige una opcion: ")
while opc!="q" and opc!="Q":
	if opc=="1":
		for d in datos:
			print d["nombre"]
	elif opc=="2":
		fechinsert=int(raw_input("Dime el año: "))
		fechas=[]
		fechasanterior=[]
		fechasinvalidas=[]
		for dat in datos:
			x=str(dat["fconstitucion"])
			f=x.split("T")
			f1=f[0].split("-")
			fechas.append(f1[0])
	elif opc=="3":
		print "3"
	elif opc=="4":
		print "4"
	elif opc=="5":
		print "5"	
	opc=raw_input("\n\n 1. Listar los nombres de las asociaciones deportivas de la provincia de Lorca.\n 2. Contar las asociaciones deportivas cuya fecha de constitución sea anterior al 2006.\n 3. Listar las direcciones de las asociaciones deportivas que empiecen por una letra dada.\n 4. Mostrar el teléfono de contacto de una asociación buscada.\n 5. Listar los nombres y los correos electrónicos de aquellas asociaciones cuyo correo electrónico sea de gmail.\n Q  Para salir\n\nElige una opcion: ")
print "\n\nHasta luego"
