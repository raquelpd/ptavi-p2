#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import calcoo

fich = open('operaciones', 'r')
operaciones = fich.readlines()

if __name__ == "__main__":	

	calcplus = calcoohija.CalculadoraHija()
	
	for operacion in operaciones:
		operador = operacion.split(',')[0]
		numeros = operacion.split(',')[1:]
		result = int(numeros[0])
		if operador == "suma":
			print("Suma =") 
			for i in range(1,len(numeros)):			
				result = calcplus.suma(result, int(numeros[i]))
		elif operador == "resta":
			print("Resta =") 
			for i in range(1,len(numeros)):			
				result = calcplus.resta(result,int(numeros[i]))
		elif operador == "multiplica":
			print("Multiplicación =") 
			for i in range(1,len(numeros)):			
				result = calcplus.producto(result, int(numeros[i]))
		elif operador == "divide":
			print("División =") 
			for i in range(1,len(numeros)):
				if numeros[i] == "0":
					result = "division by zero is not allowed"
				else:
					result = calcplus.div(result, int(numeros[i]))
		else:
			result = "solo suma, resta, multiplica o divide"
		print(result)
		


