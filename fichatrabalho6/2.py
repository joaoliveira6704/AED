from PIL import Image
pathImages = "fichatrabalho6/images/"

newSize = (240, 240) 
imagem = Image.new(size=newSize, mode = "RGB", color= "white")
# Nova imagem
pixelMap= imagem.load( )
for i in range (imagem.height):
    for j in range (imagem.width):
        if j <80:
            pixelMap[j,i] = (0, 9, 255)
        elif j< 160:
            pixelMap[j,i] = (255, 255, 255)
        else:
            # "loads" the pixel para uma lista bidimensional
            # Cor?
            # Cor?
            pixelMap[j,i] = (255, 0, 0)
imagem. show()
imagem. save(pathImages+'teste2.jpg')