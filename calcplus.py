#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

fich = open('operaciones', 'r')
operaciones = fich.readlines()

if __name__ == "__main__":	

	for operacion in operaciones:
		operador = operacion.split(',')[0]
		numeros = operacion.split(',')[1:]
		result = int(numeros[0])
		if operador == "suma":
			print("Suma =") 
			for i in range(1,len(numeros)):			
				result = result + int(numeros[i])	
		elif operador == "resta":
			print("Resta =") 
			for i in range(1,len(numeros)):			
				result = result - int(numeros[i])
		elif operador == "multiplica":
			print("Multiplicación =") 
			for i in range(1,len(numeros)):			
				result = result * int(numeros[i])
		elif operador == "divide":
			print("División =") 
			for i in range(1,len(numeros)):
				if numeros[i] == 0:
					result = "division by zero is not allowed"
				else:
					result = result / int(numeros[i])
		else:
			result = "solo suma, resta, multiplica o divide"
		print(result)
		


