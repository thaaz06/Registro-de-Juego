
def Puntaje1():
	archivo = open('puntaje.txt', 'r')
	puntaje1 = archivo.read()
	archivo.close()
	top1 = puntaje1.split('-')
	return top1[0], top1[1]

def Puntaje2():
	archivo = open('puntaje.txt', 'r')
	puntaje1 = archivo.read()
	archivo.close()
	top2 = puntaje1.split('-')
	return top2[2], top2[3]

def Puntaje3():
	archivo = open('puntaje.txt', 'r')
	puntaje1 = archivo.read()
	archivo.close()
	top3 = puntaje1.split('-')
	return top3[4], top3[5]

