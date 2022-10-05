import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image, ImageDraw
import math
import extcolors


# NOTES
# plt.imshow(img) - will show an image using matplotlib
# plt.show() - this statement will show the plot
# img.show() - shows image - same for PIL
# Image.fromarray(array, mode=) - this converts an array to an image
# colors, pixelcount = extcolors.extract_from_path(img, tolerance, limit)  - returns info about colors and occurence within an image
# Image.getcolors() - returns a list of tuples containing (pixelcount, (RGB_value))
# lambda : in python you can define a small lambda function, which has one statement
# sorted() - an inbuilt python function that returns a sorted list: sorted(iterable(the sequence to sort), key(the function to decide order), reverse(order of sort))

# PSEUDO
# 1. Read an image from file or url
# 2. Resize image to a standard size and save
# 3. Extract colors from the image

def info(img):
    array = np.array(img)  # returns image as an array
    shape = np.shape(img)  # returns (rows, columns, dimensions)
    dimensions = np.ndim(img)
    print(shape, dimensions)


# using PIL/Pillow to load an image
def load_image(img):
    im = Image.open(f'./images/{img}')
    return im


def resize(img):
    minwidth = 300
    scale_factor = minwidth / float(img.size[0])
    height = int(float(img.size[1]) * float(scale_factor))
    resized_image = img.resize((minwidth, height))
    return resized_image


# make an image grayscale
def grayscale(img):
    # 1. divide all values by 255 to get sRGB values
    # 2. multiply sRGB array by grey_vals array to convert to grayscale
    img_array = np.array(img)
    srgb_array = img_array / 255
    grey_vals = np.array([0.2176, 0.7152, 0.0722])
    grayscale_img = srgb_array @ grey_vals
    plt.imshow(grayscale_img, cmap='gray')


# Extracts 10 most common colors using PIL
def extract_colors(img):
    colors = img.convert('RGB').getcolors(img.size[0] * img.size[1])
    palette = sorted(colors, key=lambda x: x[0], reverse=True)[:25]
    rbg_palette = [i[1] for i in palette]  # returns a list of 25 most common rgb tuples
    print(rbg_palette)
    plt.imshow([rbg_palette])
    plt.show()


# Extract colors using extcolors library
def ext_colors(img):
    tolerance = 10  # how strong the color grouping is
    limit = 6  # the number of colors that will be extracted
    colors, pixel_count = extcolors.extract_from_image(img, tolerance, limit)
    return colors


# color palette renderer
def render_colors(colors):
    # define a size and columns
    size = 100
    columns = 6
    # specify total width and height
    width = int(columns * size)
    height = int((math.floor(len(colors) / columns) + 1) * size)
    # create a new image
    palette = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    # allow 2d image drawing on image
    canvas = ImageDraw.Draw(palette)
    # for each color in the list, draw a 2d rectangle
    for index, color in enumerate(colors):
        x = int((index % columns) * size)  # x-pos dependent on index
        y = int(math.floor(index / columns) * size)
        canvas.rectangle([(x, y), (x + size - 1, y + size - 1)], fill=color[0])
    plt.imshow(palette)
    plt.show()


dec_to_hex = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

# Converts rgb values to HEX values
def hex_converter(colors):
    rgb_values = [i[0] for i in colors]
    hex_values = []
    for j in rgb_values:
        new_hex_value = "#"
        for value in j:
            x = value / 16
            x_remainder = x - math.floor(value / 16)

            first_digit = dec_to_hex[math.floor(value / 16)]
            second_digit = dec_to_hex[x_remainder * 16]
            new_hex_value = new_hex_value + str(first_digit) + str(second_digit)
        hex_values.append(new_hex_value)

    return hex_values



# 1. READ AN IMAGE AND ACQUIRE INFORMATION
new_image = load_image('image3.jpg')
info(new_image)
# new_image.show()

# 2. RESIZE IMAGE TO A STANDARD SIZE AND SAVE
resized_image = resize(new_image)

# 3. EXTRACT COLORS FROM IMAGE

colors = ext_colors(resized_image)
print(colors)
# render_colors(colors)
hex_colors = hex_converter(colors)
print(hex_colors)

#

