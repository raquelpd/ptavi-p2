#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo 

class CalculadoraHija(calcoo.Calculadora):
	
	def producto(self, op1, op2):
		"""función multiplicación"""
		return op1 * op2

	def div(self, op1, op2):
		"""función divisíon"""
		return op1 / op2

if __name__ == "__main__":	

	try:
		operando1 = int(sys.argv[1])
		operando2 = int(sys.argv[3])

	except ValueError:
		sys.exit("Error: Non numerical parameters")

	calculadorahija = CalculadoraHija()

	if sys.argv[2] == "multiplicacion":
		result = calculadorahija.producto(operando1, operando2)
	elif sys.argv[2] == "division":
		result = calculadorahija.div(operando1, operando2)
	elif sys.argv[2] == "suma":
		result = calculadorahija.suma(operando1, operando2)
	elif sys.argv[2] == "resta":
		result = calculadorahija.resta(operando1, operando2)
	else:
		sys.exit('Operación sólo puede ser sumar, restar, dividir y multiplicar')
	
	print(result)
