import customtkinter
import os
from PIL import ImageTk, Image

# Função para calcular o IMC
def calcularIMC():
    try:
        peso = float(pesoEntry.get())
        altura = float(alturaEntry.get()) / 100  # Converter cm para metros
        imc = peso / (altura ** 2)
        resultadoLabel.configure(text=f"O Seu IMC é: {imc:.2f}")
    except ValueError:
        resultadoLabel.configure(text="Erro: Insira valores válidos!")

def sair_app():
    app.destroy()

# Inicializar app
app = customtkinter.CTk()

# Configurações da janela
app.title("Simulador de IMC")
appWidth, appHeight = 325, 670
screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()
x = (screenWidth / 2) - (appWidth / 2)
y = (screenHeight / 2) - (appHeight / 2)
app.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

# Frame para inputs
frameValues = customtkinter.CTkFrame(app, width=300, height=150)
frameValues.place(x=12.5, y=20)

# Label e entrada para peso
pesoLabel = customtkinter.CTkLabel(frameValues, text="Peso (kg):")
pesoLabel.place(x=20, y = 30)
pesoEntry = customtkinter.CTkEntry(frameValues)
pesoEntry.place(x=110, y= 30)

# Label e entrada para altura
alturaLabel = customtkinter.CTkLabel(frameValues, text="Altura (cm):")
alturaLabel.place(x=20, y= 80)
alturaEntry = customtkinter.CTkEntry(frameValues)
alturaEntry.place(x=110, y= 80)

# Botão para calcular IMC
calcularButton = customtkinter.CTkButton(app, text="Calcular IMC",
command=calcularIMC,
width=300,
height=60)

calcularButton.place(x=12.5, y=190)

# Botão para sair
sairButton = customtkinter.CTkButton(app, text="Sair",
command=sair_app,
width=300,
height=60)

sairButton.place(x=12.5, y=270)

# Frame para resultado
frameValues = customtkinter.CTkFrame(app, width=300, height=100)
frameValues.place(x=12.5, y=350)

#Label print
imcLabel = customtkinter.CTkLabel(frameValues, text="Índice de Massa Corporal")
imcLabel.place(x=70, y=10)

# Label para o resultado
resultadoLabel = customtkinter.CTkLabel(frameValues, text="")
resultadoLabel.place(x=90, y=50)

# Verificar se a imagem existe antes de carregá-la
imcImage = ImageTk.PhotoImage(Image.open("fichaexerciciosn9/IMC.gif"))

#Mostrar imagem em button
imcButton = customtkinter.CTkButton(app, image=imcImage,
text="",
width=280,
height=160,
fg_color="transparent",
state="disabled")

imcButton.place(x=15, y=470)

# Loop principal
app.mainloop()
