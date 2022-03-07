#pruebas de ventana de calculo de fuel

from tkinter import * #Tk, Label, Entry, Button, Canvas

from PIL import Image, ImageTk

from winsound import *

from random import randint

def transformar_tiempo_de_vuelta(mins=60):
    tiempo_de_vuelta=texto1.get()
    ''' lo paso todo a segundos '''
    
    tiempo_de_vuelta=tiempo_de_vuelta.strip()
    tiempo_de_vuelta=tiempo_de_vuelta.split(".")
    centesimas=int(tiempo_de_vuelta[2])/1000
    conversion=(int(tiempo_de_vuelta[0])*mins)+int(tiempo_de_vuelta[1])+centesimas
    print(f"tiempo de vuelta: {conversion}")
    return conversion

def transformar_tiempo_de_carrera(mins=60):
    
    ''' los mins de carrera a segundos'''
    tiempo_de_carrera=texto3.get()
    conversion=int(tiempo_de_carrera)*60
    print(f"tiempo de carrera: {conversion}")
    return conversion

def calculo_de_tiempo():
    '''en caso de que sea decimal el condicional lo pasa a un float, de lo contrario,
        empieza a hacer la regla de 3 simples basada en segundos para obtener fuel total y vueltas totales'''
    fuel_per_lap=texto2.get()
    if fuel_per_lap.count(".") > 0:
        fuel_per_lap=fuel_per_lap.strip()
        fuel_per_lap=fuel_per_lap.split(".")
        if len(fuel_per_lap[1]) == 1:
            fuel_per_lap_final=int(fuel_per_lap[0])+(float(fuel_per_lap[1])/10)
            print("fuel per lap .0 :", fuel_per_lap_final)
        if len(fuel_per_lap[1]) == 2:
            fuel_per_lap_final=int(fuel_per_lap[0])+(float(fuel_per_lap[1])/100)
            print("fuel per lap .00 :", fuel_per_lap_final)

                
    else:
        fuel_per_lap_final=int(fuel_per_lap)



    
    
    resultado_fuel=(((transformar_tiempo_de_carrera())*fuel_per_lap_final)/(transformar_tiempo_de_vuelta()))
    resultado_fuel_extra_lap=resultado_fuel+fuel_per_lap_final+1
    
    resultado_fuel=float("{:.2f}".format(resultado_fuel))
    resultado_fuel_extra_lap=float("{:.2f}".format(resultado_fuel_extra_lap))
    
    resultado_laps=(transformar_tiempo_de_carrera())/(transformar_tiempo_de_vuelta())
    resultado_laps_extra_lap=resultado_laps+1+(1/fuel_per_lap_final)
    
    resultado_laps=float("{:.2f}".format(resultado_laps))
    resultado_laps_extra_lap=float("{:.2f}".format(resultado_laps_extra_lap))


    texto4.configure(state='normal')
    texto5.configure(state='normal')
    texto4.delete(0,"end")
    texto4.insert(0,f"{resultado_fuel} Lts ({resultado_fuel_extra_lap} Lts)" )
    texto4.configure(state='disabled')
    texto5.delete(0,"end")
    texto5.insert(0,f"{resultado_laps} Laps ({resultado_laps_extra_lap} Lts) ")
    texto5.configure(state='disabled')

def sounds():
    sound=randint(1,2)
    if sound==1:
        PlaySound("boxes_1.wav", SND_FILENAME)
    if sound==2:
        PlaySound("boxes_2.wav", SND_FILENAME)

    

ventana=Tk()


ventana.title("Calculo de Fuel")
ventana.config(bg="black")
ventana.geometry("280x250")



#imagenes

imagen = Image.open('pitlaneBox.jpg')
imagen = imagen.resize((300,300))
imagen_convertida = ImageTk.PhotoImage(imagen)
(canvas_width, canvas_height) = imagen.size
canvas = Canvas(ventana, width=canvas_width,height=canvas_height,bg="black",highlightthickness=0, relief='ridge')
canvas.create_image(0,0, image=imagen_convertida,anchor=NW)
canvas.place(x=0,y=0)






#vetanas de inputs

label1 = Label(ventana,text="Lap time (0.00.000) :",bg="grey",borderwidth=2, relief="ridge")
label1.place(x=20,y=10, width=120, height=30)

texto1 = Entry(ventana,bg="white",borderwidth=2, relief="ridge")
texto1.place(x=140,y=10, width=120, height=30)

label2 = Label(ventana,text="Fuel p/ Lap (0.00) :", bg="grey",borderwidth=2, relief="ridge")
label2.place(x=20,y=50, width=120, height=30)

texto2 = Entry(ventana,bg="white",borderwidth=2, relief="ridge")
texto2.place(x=140,y=50, width=120, height=30)

label3 = Label(ventana,text="Race Duration (Mins): ", bg="grey",borderwidth=2, relief="ridge")
label3.place(x=20,y=90, width=120, height=30)

texto3 = Entry(ventana,bg="white",borderwidth=2, relief="ridge")
texto3.place(x=140,y=90, width=120, height=30)

#boton

boton=Button(ventana,text="Calculate",bg="red",borderwidth=2,cursor="hand2",command=lambda:[calculo_de_tiempo(),sounds()])
boton.place(x=80,y=125, width=120, height=30)


# ventanas de resultados

label4 = Label(ventana,text="Total Fuel (Extra Lap):", bg="grey",borderwidth=2, relief="ridge")
label4.place(x=20,y=160, width=120, height=30)

texto4 = Entry(ventana,bg="white",borderwidth=2, relief="ridge",state='disabled')
texto4.place(x=140,y=160, width=120, height=30)

label5 = Label(ventana,text="Total Laps (+1 Lap): ", bg="grey",borderwidth=2, relief="ridge")
label5.place(x=20,y=200, width=120, height=30)

texto5 = Entry(ventana,bg="white",borderwidth=2, relief="ridge",state='disabled')
texto5.place(x=140,y=200, width=120, height=30)

ventana.resizable(False, False)
ventana.iconbitmap("25.ico")
ventana.mainloop()
