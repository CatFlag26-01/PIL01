from PIL import Image
with Image.open('gato.jpg') as pic_original:
    print('Tamaño:', pic_original.size)
    print('Formato:', pic_original.format)
    print('Tipo:', pic_original.mode)
    pic_original.show()