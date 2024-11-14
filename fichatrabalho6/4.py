from PIL import Image

pathImages = "fichatrabalho6/images/"
imagem1 = Image.open(pathImages+'leopard.jpg')

def imageGrayScale(imagem1):
    """
    Converts a image to grayscale
    """
    pixelMap = imagem1.load()
    
    for i in range(imagem1.width):
        for j in range(imagem1.height):
            p = pixelMap[i,j]
            red = p[0]
            green = p[1]
            blue = p[2]
            red = green = blue = int(0.299 * red + 0.587 * green + 0.114 * blue )
            pixelMap[i,j] = (red, green, blue)

    imagem1.show()
    imagem1.save(pathImages+'teste4.jpg')

imageGrayScale(imagem1)
