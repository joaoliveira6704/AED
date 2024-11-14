from PIL import Image
import random

newSize = (400,400)

pathImages = "fichatrabalho6/images/"

def ImageArt(newSize):
    """
    Creates a image with random color for each pixel in its size(h & w)
    """
    imagem = Image.new(size=newSize, mode= "RGB", color="white")

    pixelMap = imagem.load()
    
    for i in range(imagem.width):
        for j in range(imagem.height):
            pixelMap[i,j] = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) # Adds a random color RGB to pixel [i][j]

    imagem.show()
    imagem.save(pathImages+'teste1.jpg')

ImageArt(newSize)
