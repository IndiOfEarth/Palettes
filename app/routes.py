import os.path

from app import app
from flask import render_template, request, redirect, url_for, flash, abort
from app.images import Img

# Page/app layout
# 1. Home Page - asks to get image
# 2. Extract Route - this extracts colors from the image
# 3. Palette Page - Separate page that displays palette.

# Home route handling GET and POST requests
@app.route("/", methods=['GET', 'POST'])
def home():
    image_dir = 'static/images'
    for file in os.scandir(image_dir):
        os.remove(file.path)
    return render_template("index.html")


# extract route responsible for extracting colors
@app.route("/extract", methods=['GET', 'POST'])
def extract():
    if request.method == "POST":
        uploaded_image = request.files['image']
        filename = uploaded_image.filename
        # 2. Check if filename is valid
        if filename != '':
            file_ext = os.path.splitext(filename)[1] # get file extension
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                print("Incorrect file extension")
                abort(400)
            # 3. If filename is valid, extract colors and update homepage
            else:
                print(f"Successfully uploaded image: {filename}")
                uploaded_image.save(os.path.join('static/images', filename))
                return redirect(url_for("palette"))
        else:
            print("Upload failed")
            # flash('No selected image!') TODO - set a secret key in config.py
        return redirect(url_for("home"))

@app.route("/palette")
def palette():
    images = os.listdir('static/images')

    new_img = Img(images[0])
    extracted_colors = new_img.hex_colors
    selected_img = images[0]
    print(extracted_colors)
    return render_template("palette.html", img=selected_img, palette=extracted_colors)

