
import customtkinter

# Inicializar app
app = customtkinter.CTk()

# Titulo da app
app.title("Países do Mundo!")

# Define a dimensão da app
appWidth = 600
appHeight = 300

# Obtém a dimensão do ecrã
screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()

# Obtém o centro da imagem
x = (screenWidth/2)-(appWidth/2)
y = (screenHeight/2)-(appHeight/2)

# Define o tamanho da app e começa no centro da tela
app.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

# Cor de fundo 
#app.configure(fg_color = 'blue')

# App deixa de ser redimensionável
#app.resizable(False, False)

# Inicializar label
labelPais = customtkinter.CTkLabel(app, text='País',
fg_color='transparent',
text_color='white',
font=('Helvetica',14))

# Colocar label nas coordenadas
labelPais.place(x=15, y=40)

# Inicializar label
labelContinente = customtkinter.CTkLabel(app, text='Continente',
fg_color='transparent',
text_color='white',
font=('Helvetica',14))

# Colocar label nas coordenadas
labelContinente.place(x=15, y=80)

# Inicializar caixa de texto
entryPais = customtkinter.CTkEntry(app, placeholder_text='Indique um país',
width=150)

# Posicionar à frente da label
entryPais.place(x=100,y=40)

# Inicializar combobox
continentes = ['África','Ásia','América','Europa','Oceania']
comboContinente = customtkinter.CTkComboBox(app, values=continentes,
width=150,
command='')

# Posicionar à frente da label
comboContinente.place(x=100,y=80)

# Valor por defeito
comboContinente.set("Europa")

# Inicializar label
labelHemisferio = customtkinter.CTkLabel(app, text='Hemisfério',
fg_color='transparent',
text_color='white',
font=('Helvetica',14))

# Colocar label nas coordenadas
labelHemisferio.place(x=15, y=120)

radioVariable = customtkinter.StringVar(value='Norte')

radiobutton1 = customtkinter.CTkRadioButton(app, text='Norte',
variable=radioVariable,
value='Norte')
radiobutton1.place(x=100, y=130)

radiobutton2 = customtkinter.CTkRadioButton(app, text='Sul',
variable=radioVariable,
value='Sul')
radiobutton2.place(x=100, y=170)

# Inicializar label
labelIdioma = customtkinter.CTkLabel(app, text='Hemisfério',
fg_color='transparent',
text_color='white',
font=('Helvetica',14))

# Colocar label nas coordenadas
labelIdioma.place(x=400, y=40)

checkVar1 = customtkinter.StringVar(value="off")
checkVar2 = customtkinter.StringVar(value="off")
checkVar3 = customtkinter.StringVar(value="on")
checkVar4 = customtkinter.StringVar(value="off")

checkboxEN = customtkinter.CTkCheckBox(app, text="Inglês",
variable=checkVar1,
onvalue="on",
offvalue="off")

checkboxFR = customtkinter.CTkCheckBox(app, text="Françês",
variable=checkVar2,
onvalue="on",
offvalue="off") 

checkboxPT = customtkinter.CTkCheckBox(app, text="Português",
variable=checkVar3,
onvalue="on",
offvalue="off")

checkboxOT = customtkinter.CTkCheckBox(app, text="Outro",
variable=checkVar4,
onvalue="on",
offvalue="off")

checkboxEN.place(x=360, y= 80)
checkboxFR. place(x=360, y= 110)
checkboxPT. place(x=460, y= 80)
checkboxOT. place(x=460, y= 110)

#Button
btnGuardar = customtkinter.CTkButton(app, text='Guardar',
command='',
width=100,
height=40)
#Posicionar Botão
btnGuardar.place(x=380, y=250)

#Button
btnLimpar = customtkinter.CTkButton(app, text='Limpar',
command='',
width=100,
height=40,
state='disabled')
#Posicionar Botão
btnLimpar.place(x=490, y=250)

# Loop de event listening
app.mainloop()