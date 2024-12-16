# Biblioteca Tkinter: UI
import customtkinter
from PIL import Image, ImageTk
import CTkMessagebox
from tkinter import ttk # treeview
import os
from datetime import datetime

path = "./ex10/files/"

def renderWindow(appWidth, appHeight, appTitle):
    """
    Renderiza a window da app, com as dimensões e título dos argumentos
    """
    app.title(appTitle)
    # Obter as dimensões do meu screen (em pixeis)
    screenWidth = app.winfo_screenwidth()
    screenHeight = app.winfo_screenheight()
    # App centrada no screen, em função das suas dimensões# encontrar o 
    x = (screenWidth/2) - (appWidth/2)
    y= (screenHeight/2) - (appHeight/2)
    app.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    app.resizable(False, False)

def validarMov(numEstudante, movEntrada, movSaida):
    ficheiro = open(path+"presencas.txt", "r")

    validacao = []

    f = ficheiro.readlines()
    if f == []:
        msg = ""
        return True,msg
    for line in f:
        campos = line.split(";")
        if campos[0] == numEstudante:
            validacao.append(campos[2].strip("\n"))
    ficheiro.close()
    if movEntrada == 1 and movSaida == 0:
        if validacao[len(validacao)-1] == "Entrada":
            msg = f"O último movimento do estudante {numEstudante} foi Entrada.\nO movimento deve ser Saída"
        else:
            msg =""
            return True, msg
    elif movEntrada == 0 and movSaida == 1:
        if validacao[len(validacao)-1] == "Saída":
            msg = f"O último movimento do estudante {numEstudante} foi Saída.\nO movimento deve ser Entrada"
        else:
            msg =""
            return True, msg
    elif movEntrada == 1 and movSaida == 1:
        msg = f"Deve selecionar apenas um movimento!"
    
    else:
        msg = f"Deve selecionar no minimo um movimento!" 

    return False , msg
            

def salvarMovimento(numStud, movEntrada, movSaida):
    if not os.path.exists(path):
        os.mkdir(path)

    numEstudante = numStud.get()
    if numEstudante == " ":
        msg1 = CTkMessagebox.CTkMessagebox(title="Sair da aplicação", 
        icon="cancel", message=msg, option_1="Ok")
        
    validator, msg = validarMov(numEstudante,movEntrada,movSaida)

    if validator:
        ficheiro = open(path+"presencas.txt", "a")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y;%H:%M:%S")
        if movEntrada==1:
            line = numEstudante+";"+dt_string+";"+"Entrada\n"
        else:
            line = numEstudante+";"+dt_string+";"+"Entrada\n"
        ficheiro.write(line)
        ficheiro.close()
        print(True)
    else:
        msg1 = CTkMessagebox.CTkMessagebox(title="Sair da aplicação", 
        icon="cancel", message=msg, option_1="Ok")
    
    
    renderPresenca()

def lerFicheiro():
    if not os.path.exists(path):
        os.mkdir(path)

    ficheiro = open(path+"presencas.txt", "r")

    f = ficheiro.readlines()
    for line in f:
        campos = line.split(";")
        print(campos)
        print()

def viewData(histPres):
    with open(path+"presencas.txt", "r") as file:
        lista = file.readlines()
    
    histPres.delete("0.0", "end")
    histPres.insert("0.0", "Número\t  Data\t  Hora \t Movimento\n")
    for line in lista:
        line = line.replace(";", "   -   ")
        histPres.insert("end",line)


    file.close()

def renderPresenca():
    framePresenca = customtkinter.CTkFrame(app, width=750, height=500)
    framePresenca.place(x=250, y=0)

    labelNumStud = customtkinter.CTkLabel(framePresenca, text="Número de estudante")
    labelNumStud.place(x= 20, y=50)
    entryNumStud = customtkinter.CTkEntry(framePresenca, width=130)
    entryNumStud.place(x=160, y=50)

    labelMovType = customtkinter.CTkLabel(framePresenca, text="Tipo de Movimento")
    labelMovType.place(x= 20, y=90)

    checkvar1 = customtkinter.IntVar()
    checkvar2 = customtkinter.IntVar()

    checkboxEntrada = customtkinter.CTkCheckBox(framePresenca, text="Entrada",variable=checkvar1, onvalue=1, offvalue=0)
    checkboxSaida = customtkinter.CTkCheckBox(framePresenca, text="Saída", variable=checkvar2, onvalue=1, offvalue=0)
    checkboxEntrada.place(x = 160, y=90)
    checkboxSaida.place(x = 160, y=130)

    registmovBtn = customtkinter.CTkButton(framePresenca,command=lambda:salvarMovimento(entryNumStud, checkboxEntrada.get(), checkboxSaida.get()), text="Registar o Movimento em Ficheiro", width=250, height= 170)
    registmovBtn.place(x=30, y=280)

    histPres = customtkinter.CTkTextbox(framePresenca,width=320, height=300)
    histPres.place(x=400, y=50)

    lerFicheiroBtn = customtkinter.CTkButton(framePresenca,command=lambda:viewData(histPres), text="Registar o Movimento em Ficheiro", width=320, height= 70)
    lerFicheiroBtn.place(x=400, y=280)

def renderConsulta():
    print("Consulta")

def sairApp():
    msg = CTkMessagebox.CTkMessagebox(title="Sair da aplicação", 
    icon="question", message="Deseja sair da aplicação?", option_3="Sim", option_2="Não", option_1="Cancelar")
    
    option = msg.get()

    if option == "Sim":
        app.destroy()
    else:
        return

# Inicializar app
app = customtkinter.CTk()

title = "my new app"
width = 1000
height = 500

renderWindow(width,height,title)

frameButtons = customtkinter.CTkFrame(app, width=250, height=500)
frameButtons.place(x=0, y=0)

frameMainscreen = customtkinter.CTkFrame(app, width=750, height=500)
frameMainscreen.place(x=250, y=0)

imgMain = customtkinter.CTkImage(Image.open("./ex10/images/presencas.png"), size=(750,500))
imgMainPlace = customtkinter.CTkLabel(frameMainscreen, image=imgMain, text="")
imgMainPlace.place(x=0,y=0)

icnGerir = customtkinter.CTkImage(Image.open("./ex10/images/icoOp1.png"), size =(64,64))
icnConsultar = customtkinter.CTkImage(Image.open("./ex10/images/icoOp2.png"), size =(64,64))
icnSair = customtkinter.CTkImage(Image.open("./ex10/images/icoOp4.png"), size =(64,64))

gerirPresencasBtn = customtkinter.CTkButton(frameButtons, command=renderPresenca, width=230, height=120,image=icnGerir, text="Gerir Presenças", compound="top") 
consultarPresencasBtn = customtkinter.CTkButton(frameButtons, command=renderConsulta, width=230, height=120,image=icnConsultar, text="Consultar Presenças", compound="top") 
sairBtn = customtkinter.CTkButton(frameButtons, command=sairApp, width=230, height=120,image=icnSair, text="Sair App", compound="top") 

gerirPresencasBtn.place(x=10, y=40)
consultarPresencasBtn.place(x=10, y=180)
sairBtn.place(x=10, y=320)


app.mainloop()   # event listening loop by calling the mainloop()