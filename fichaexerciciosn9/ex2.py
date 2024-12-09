
import customtkinter
import os
from PIL import ImageTk
path = "fichaexerciciosn9/images/"

if not os.path.exists(path):
    os.mkdir(path)

def calcularIMC():
    imc = (int(alturaCM.get())-100)-(int(alturaCM.get())-150)/int(k.get())
    labelPesoFinal.configure(text = str(imc) + " KG") 

# Inicializar app
app = customtkinter.CTk()

# Titulo da app
app.title("Simulador de Peso Ideal")

# Define a dimensão da app
appWidth = 370
appHeight = 430

# Obtém a dimensão do ecrã
screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()

# Obtém o centro da imagem
x = (screenWidth/2)-(appWidth/2)
y = (screenHeight/2)-(appHeight/2)

# Define o tamanho da app e começa no centro da tela
app.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

# Inicializar label
labelAltura = customtkinter.CTkLabel(app,
text="Indique a altura(cm):")

# Colocar label nas coordenadas
labelAltura.place(x=20, y=10)

alturaCM = customtkinter.StringVar()
# Inicializar caixa de texto
altura = customtkinter.CTkEntry(app,
textvariable= alturaCM)

altura.place(x=170,y=10)

# Inicializar label
labelGenero = customtkinter.CTkLabel(app,
text="Género:")

# Colocar label nas coordenadas
labelGenero.place(x=20, y=50)

k = customtkinter.StringVar(value=4)

radiobutton1 = customtkinter.CTkRadioButton(app, text='Masculino',
variable=k,
value=4)
radiobutton1.place(x=170, y=50)

radiobutton2 = customtkinter.CTkRadioButton(app, text='Feminino',
variable=k,
value=2)
radiobutton2.place(x=170, y=80)

#Button
img1Button = ImageTk.PhotoImage(file=path+"PesoIdeal.png")

btnCalcularIMC = customtkinter.CTkButton(app,image=img1Button,
 text='Calcular IMC',
command=calcularIMC,
width=250,
height=50)
#Posicionar Botão
btnCalcularIMC.place(x=25, y=150)

# Inicializar label
labelPeso = customtkinter.CTkLabel(app,
text="Peso Ideal em Kg")

# Colocar label nas coordenadas
labelPeso.place(x=70, y=230)

# Inicializar label
labelPesoFinal = customtkinter.CTkLabel(app,
text="")

# Colocar label nas coordenadas
labelPesoFinal.place(x=105, y=260)

# Loop de event listening
app.mainloop()