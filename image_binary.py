from PIL import Image


def gambar_ke_biner_grayscale(path):
    img = Image.open(path).convert('L')
    widht, height = img.size

    for y in range(height):
        for x in range(widht):
            pixel = img.getpixel((x, y))
            biner = format(pixel, '08b')
            print(biner, end=' ')
        print()


gambar_ke_biner_grayscale('ucup.png')
