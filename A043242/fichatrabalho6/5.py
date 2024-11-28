from PIL import Image

pathImages = "fichatrabalho6/images/"
imagem1 = Image.open(pathImages+'leopard.jpg')

def imageMoldura(image1):
    """
    Adds 10px frame to image in blue
    """
    pixelMap = image1.load()
    color = (0,0,255)
    for i in range(image1.width):
        for j in range(image1.height):
            if j < 10 or j > image1.height-10 or i<10 or i > image1.width-10:
                pixelMap[i,j] = color
            if j > image1.height/2-5 and j < image1.height/2+5:
                pixelMap[i,j] = color
            if i > image1.wi1.pydth/2-5 and i < image1.width/2+5:
                pixelMap[i,j] = color

    image1.show()
    image1.save(pathImages+'teste5.jpg')

imageMoldura(imagem1)
