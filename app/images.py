from PIL import Image, ImageDraw
import math
import extcolors
import time


# NOTES
# plt.imshow(img) - will show an image using matplotlib
# plt.show() - this statement will show the plot
# img.show() - shows image - same for PIL
# Image.fromarray(array, mode=) - this converts an array to an image
# colors, pixelcount = extcolors.extract_from_path(img, tolerance, limit)  - returns info about colors and occurence within an image
# Image.getcolors() - returns a list of tuples containing (pixelcount, (RGB_value))
# lambda : in python you can define a small lambda function, which has one statement
# sorted() - an inbuilt python function that returns a sorted list: sorted(iterable(the sequence to sort), key(the function to decide order), reverse(order of sort))
# enumerate() - for iterating over an index and item in a list

# PSEUDO
# 1. Read an image from file or url
# 2. Resize image to a standard size and save
# 3. Extract colors from the image


# Image class is responsible for loading image, resizing, extracting colors and generating hex codes
class Img():
    def __init__(self, img):
        self.image = self.load_image(img)
        self.resized_image = self.resize()
        self.extracted_colors = self.ext_colors()
        self.hex_colors = self.hex_converter(self.extracted_colors)

        # self.array = np.array(self.image)
        # self.shape = np.shape(self.image)
        # self.dimensions = np.ndim(self.image)

    # using PIL/Pillow to load an image
    def load_image(self, img):
        start_time = time.time()

        im = Image.open(f'static/images/{img}')
        print(f"Load Image time taken: {time.time() - start_time}")
        return im

    # resizing an image
    def resize(self):
        start_time = time.time()

        min_width = 300
        scale_factor = min_width / float(self.image.size[0])
        min_height = int(float(self.image.size[1]) * float(scale_factor))
        resized_image = self.image.resize((min_width, min_height))
        print(f"Resize Image time taken: {time.time() - start_time}")
        return resized_image

    # Extract colors using extcolors library
    def ext_colors(self):
        start_time = time.time()

        tolerance = 20  # how strong the color grouping is
        limit = 8  # the number of colors that will be extracted
        colors, pixel_count = extcolors.extract_from_image(self.resized_image, tolerance, limit)
        print(f"Color extraction time taken: {time.time() - start_time}")
        return colors

    # Converts rgb values to HEX values
    def hex_converter(self, colors):
        start_time = time.time()

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

        print(f"Hex conversion time taken: {time.time() - start_time}")
        return hex_values


# TIMER PSEUDO
# When each function is called, measure time it takes to execute function


# new_image = Img(img="image1.jpg")
# print(new_image.hex_colors)

