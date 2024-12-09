import customtkinter
import CTkMessagebox
from PIL import Image
from tkinter import ttk

def messageDialog():
    msg = CTkMessagebox.CTkMessagebox(title="Sair da aplicação", 
    icon="question", message="Deseja encerrar a aplicação?", option_3="Sim", option_2="Não", option_1="Cancelar")
    
    option = msg.get()

    if option == "Sim":
        app.destroy()
    else:
        return

def addTab():
    tabview.add("Administrador")

    return

def viewData():
    lista = readFile()

    for line in lista:
        campos= line.split(";")
        tree.insert("","end", values= (campos[0], campos[1], campos[2].strip("\n")))

def readFile():
    f = open("ficha_aula9_12_24/temperatura.txt", "r")

    lista = f.readlines()

    f.close()

    return lista

# Inicializar app
app = customtkinter.CTk()

# Configurações da janela
app.title("Demo com containers")
appWidth, appHeight = 400, 700
screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()
x = (screenWidth / 2) - (appWidth / 2)
y = (screenHeight / 2) - (appHeight / 2)
app.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

tabview = customtkinter.CTkTabview(app, width=400, height=430)
tabview.pack(padx=20, pady=20)

tab1 = tabview.add("Gestor de Presenças")
tab2 = tabview.add("Consultar")

tabview.set("Gestor de Presenças")

# Verificar se a imagem existe antes de carregá-la
imgImage = customtkinter.CTkImage(Image.open("ficha_aula9_12_24/images/medium.png"), size=(300,280))

#Mostrar imagem em label
imgLabel = customtkinter.CTkLabel(tab1, image=imgImage,
text="",
width=300,
height=280)

imgLabel.place(x=25, y=5)

exitButton = customtkinter.CTkButton(tab1, text="Sair da Aplicação", command=messageDialog,
width=300,
height=30)
exitButton.place(x=25, y=300)

adminButton = customtkinter.CTkButton(tab1, text="Ver Painel Admin", command=addTab,
width=300,
height=30)
adminButton.place(x=25, y=340)

consultarDados = customtkinter.CTkButton(tab2, text="Consultar Dados", command=viewData,
width=300,
height=30)
consultarDados.place(x=25, y=10)

vertScroll = ttk.Scrollbar()

tree = ttk.Treeview(tab2, height=15,
selectmode="browse",
columns=("Data","Hora","Temperatura"),
show="headings")

tree.column("Data", width=110, anchor="c")
tree.column("Hora", width=110, anchor="c")
tree.column("Temperatura", width=110, anchor="c")
tree.heading("Data", text="Data")
tree.heading("Hora", text="Hora")
tree.heading("Temperatura", text="Temperatura")

tree.place(x=10, y=50)


# Loop principal
app.mainloop()
