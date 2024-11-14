from PIL import Image

pathImages = "fichatrabalho6/images/"
imagem1 = Image.open(pathImages+'leopard.jpg')

def imageMoldura(image1):
    """
    Adds 20px frame to image in magenta
    """
    pixelMap = image1.load()
    
    for i in range(image1.width):
        for j in range(image1.height):
            if j < 20 or j > image1.height-20 or i<20 or i > image1.width-20:
                pixelMap[i,j] = (214,0,110)

    image1.show()
    image1.save(pathImages+'teste3.jpg')

imageMoldura(imagem1)
