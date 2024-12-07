
import customtkinter
import os
path = "fichaexerciciosn9/files/"

if not os.path.exists(path):
    os.mkdir(path)

def saveNotes():
    f=open(path+"texto.txt", "w")

    f.write(notas.get("0.0", "end-1c"))
    
    f.close()
    print("Ficheiro salvo")

def clearNotes():
    notas.delete("0.0", "end")

    print("Text box foi limpa")

def readNotes():
    f=open(path+"texto.txt", "r")

    notas.delete("0.0", "end")
    lines = f.readlines()
    for line in lines:
        notas.insert("end",line)


    f.close()

# Inicializar app
app = customtkinter.CTk()

# Titulo da app
app.title("My Notepad")

# Define a dimensão da app
appWidth = 300
appHeight = 600

# Obtém a dimensão do ecrã
screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()

# Obtém o centro da imagem
x = (screenWidth/2)-(appWidth/2)
y = (screenHeight/2)-(appHeight/2)

# Define o tamanho da app e começa no centro da tela
app.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

# Inicializar label
labelNotas = customtkinter.CTkLabel(app,
text="Indique as suas notas")

# Colocar label nas coordenadas
labelNotas.place(x=80, y=10)

# Inicializar caixa de texto
notas = customtkinter.CTkTextbox(app,
width=250,
height=300)

notas.place(x=25,y=40)

#Button
btnGuardarNotas = customtkinter.CTkButton(app, text='Guardar Notas',
command=saveNotes,
width=250,
height=50)
#Posicionar Botão
btnGuardarNotas.place(x=25, y=350)

#Button limpar notas
btnLimpar = customtkinter.CTkButton(app, text='Limpar Notas',
command=clearNotes,
width=250,
height=50)
#Posicionar Botão
btnLimpar.place(x=25, y=410)

#Button ler bloco
btnLerFicheiro = customtkinter.CTkButton(app, text='Ler Bloco de Notas',
command=readNotes,
width=250,
height=50)
#Posicionar Botão
btnLerFicheiro.place(x=25, y=470)

# Loop de event listening
app.mainloop()