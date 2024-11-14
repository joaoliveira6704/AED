from PIL import Image

pathImages = ".\\images\\"

newSize = (20,20)

imagem = Image.new(size=newSize, mode="RGB", color="white")#Nova Imagem

pixelMap= imagem.load()
for i in range(imagem.width):
    for j in range(imagem.height):
        red = i
        green = j
        blue = 255-i
        pixelMap[i,j] = (red, green, blue)
imagem.show()
imagem.save(pathImages+"teste.jpg")