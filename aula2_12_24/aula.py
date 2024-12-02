
import customtkinter

# Inicializar app
app = customtkinter.CTk()

# Titulo da app
app.title("My first app")

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
font=('Helvetica',15))

# Colocar label nas coordenadas
labelPais.place(x=15, y=40)

# Inicializar label
labelContinente = customtkinter.CTkLabel(app, text='Continente',
fg_color='transparent',
text_color='white',
font=('Helvetica',15))

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
labelPass = customtkinter.CTkLabel(app, text='Password',
fg_color='transparent',
text_color='white',
font=('Helvetica',15))

# Colocar label nas coordenadas
labelPass.place(x=15, y=120)

# Inicializar caixa de texto com "*"
entryPass = customtkinter.CTkEntry(app, placeholder_text='Indique uma palavra-passe',
width=150,
show='*')

# Posicionar à frente da label
entryPass.place(x=100,y=120)

#Button
btnGuardar = customtkinter.CTkButton(app, text='Guardar',
command='',
width=100,
height=40)
#Posicionar Botão
btnGuardar.place(x=15, y=180)

#Button
btnLimpar = customtkinter.CTkButton(app, text='Limpar',
command='',
width=100,
height=40)
#Posicionar Botão
btnLimpar.place(x=130, y=180)

# Loop de event listening
app.mainloop()