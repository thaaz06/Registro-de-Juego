from tkinter import *
from tkinter.font import Font
import operator
from puntaje import Puntaje1, Puntaje2, Puntaje3




#Guardado de informacion
def Enviar_datos():
	nCompleto_data = nCompleto.get()
	correo_data = str(correo.get())
	telefono_data = str(telefono.get())
	puntaje_data = str(puntaje.get())
	
	#Guardado en documento 
	registroFile = open("Registro.csv", "a")
	registroFile.write("\t")
	registroFile.write(f'Nombre: {nCompleto_data}')
	registroFile.write("\t")
	registroFile.write(f'Correo: {correo_data}')
	registroFile.write("\t")
	registroFile.write(f'Telefono: {telefono_data}')
	registroFile.write("\t")
	registroFile.write(f'Puntaje: {puntaje_data}')
	registroFile.write("\n")
	registroFile.close()


	#Guardado de puntaje en diccionario
	top [nCompleto_data] = int(puntaje_data)
	#ordenar diccionario descendente por valor
	top1 = sorted(top.items(), key=operator.itemgetter(1), reverse=True)
	#conversion de tuplas a diccionario
	d = dict((n, p) for n, p in top1)
	nombres = list(d.keys())
	puntajes = list(d.values())
	#limpiado de datos
	nCompleto_entry.delete(0, END)
	correo_entry.delete(0, END)
	telefono_entry.delete(0, END)
	puntaje_entry.delete(0, END)

	#Top de puntajes
	if int(puntajes[2]) > int(tercerPuntaje[1]):
		tercerL.config(text="Tercer Lugar: " + str(nombres[2])+" con "+str(puntajes[2])+" pts.")
	else:
		primerL.config(text="Tercer Lugar: " + str(tercerPuntaje[0])+" con "+str(tercerPuntaje[1])+" pts.")
	if int(puntajes[1]) > int(segundoPuntaje[1]):
		segundoL.config(text="Segundo Lugar: " + str(nombres[1])+" con "+str(puntajes[1])+" pts.")
	else:
		primerL.config(text="Segundo Lugar: " + str(segundoPuntaje[0])+" con "+str(segundoPuntaje[1])+" pts.")
	if int(puntajes[0]) > int(primerPuntaje[1]):
		primerL.config(text="Primer Lugar: " + str(nombres[0])+" con "+str(puntajes[0])+" pts.")
	else:
		primerL.config(text="Primer Lugar: " + str(primerPuntaje[0])+" con "+str(primerPuntaje[1])+" pts.")
	
	#Guardado de Top
	puntajeFile = open('puntaje.txt', 'w')
	puntajeFile.write(f'{nombres[0]}-{puntajes[0]}-{nombres[1]}-{puntajes[1]}-{nombres[2]}-{puntajes[2]}')
	puntajeFile.close()

#Configuracíon de la ventana
registro = Tk()

#fuentes de textos
titulosTexto = Font(
	family = "Helvetica",
	size   = 20,
	weight = "bold",
	)
entradasTexto = Font(
	family = "Arial",
	size   = 15,
	weight = "normal",
	)
puntajeTexto = Font(
	family="Helvetica",
	size=15,
	weight="normal",
	)
#Configuracíon de la ventana
registro.geometry("750x570")
registro.title("Registro de Torneo VR")
registro.resizable(False, False)
registro.iconbitmap("logokaizen.ico")
registro.config(background ="#000")
titulo = Label(text="Ingresa tus datos de juego", font=(titulosTexto, 22), bg="#d39000", fg = "white", width = "300", height = "2")
titulo.pack()


#campos
nCompleto_label = Label(text='Nombre Completo:', fg="white", bg='black', font=titulosTexto)
nCompleto_label.place(x=150, y=90)
correo_label = Label(text='Correo Electrónico:', fg="white", bg='black', font=titulosTexto)
correo_label.place(x=150, y=150)
telefono_label = Label(text='Teléfono:', fg="white", bg='black', font=titulosTexto)
telefono_label.place(x=150, y=210)
puntaje_label = Label(text='Puntaje:', fg="white", bg='black', font=titulosTexto)
puntaje_label.place(x=150, y=270)

#variables
nCompleto = StringVar()
correo = StringVar()
telefono = IntVar()
puntaje = IntVar()
primerPuntaje = list(Puntaje1())
segundoPuntaje = list(Puntaje2())
tercerPuntaje = list(Puntaje3())
top = {primerPuntaje[0]: int(primerPuntaje[1]), segundoPuntaje[0]: int(segundoPuntaje[1]), tercerPuntaje[0]: int(tercerPuntaje[1])}


#entradas
nCompleto_entry = Entry(textvariable=nCompleto, width='40', font=entradasTexto)
correo_entry = Entry(textvariable=correo, width='40', font=entradasTexto)
telefono_entry = Entry(textvariable=telefono, width='40', font=entradasTexto)
puntaje_entry = Entry(textvariable=puntaje, width='40', font=entradasTexto)

nCompleto_entry.place(x=150, y=120.5)
correo_entry.place(x=150, y=180.5)
telefono_entry.place(x=150, y=240.5)
puntaje_entry.place(x=150, y=300.5)

#buton
enviar = Button(registro, text='Enviar', command=Enviar_datos, width='30', height='2', bg='#d39000', fg='white')
enviar.place(x=250, y=360)

#puntaje
primerL = Label(text="Primer Lugar: " + str(primerPuntaje[0])+" con "+str(primerPuntaje[1])+" pts.", fg="white", bg='black', font=puntajeTexto) 
primerL.place(x=10, y=450)

segundoL = Label(text="Segundo Lugar: " + str(segundoPuntaje[0])+" con "+str(segundoPuntaje[1])+" pts.", fg="white", bg='black', font=puntajeTexto) 
segundoL.place(x=10, y=490)

tercerL = Label(text="Tercer Lugar: " + str(tercerPuntaje[0])+" con "+str(tercerPuntaje[1])+" pts.", fg="white", bg='black', font=puntajeTexto) 
tercerL.place(x=10, y=530)
#ejecucion del programa

registro.mainloop()

