
import sys
import csv
import calcplus
import calcoohija

#sys.argv[1] = fichero
fich = open(sys.argv[1], 'r')

if __name__ == "__main__":	
	
	calcplusplus = calcoohija.CalculadoraHija()	
	sys.argv[1] = fich

	with open('operaciones.csv') as mifichero:		
		for operacion in mifichero:
			operador = operacion.split(',')[0]
			numeros = operacion.split(',')[1:]
			result = int(numeros[0])
			operaciones = csv.reader(mifichero)
			if operador == "suma":
				print("Suma =") 
				for i in range(1,len(numeros)):			
					result = calcplusplus.suma(result, int(numeros[i]))
			elif operador == "resta":
				print("Resta =") 
				for i in range(1,len(numeros)):			
					result = calcplusplus.resta(result,int(numeros[i]))
			elif operador == "multiplica":
				print("Multiplicación =") 
				for i in range(1,len(numeros)):			
					result = calcplusplus.producto(result, int(numeros[i]))
			elif operador == "divide":
				print("División =") 
				for i in range(1,len(numeros)):
					if numeros[i] == "0":
						result = "division by zero is not allowed"
					else:
						result = calcplusplus.div(result, int(numeros[i]))
			else:
				result = "solo suma, resta, multiplica o divide"
			print(result)
		


