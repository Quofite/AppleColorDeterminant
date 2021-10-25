"""
This is very simple neural network made by
Gleb Nikitin (vk.com/gleb.nikitin1) and Aleksey Davydenok (vk.com/doogls) and some internet searching :)

This neural network is detecting the color of apple in picture from /images/ with white or black background.
Program is very simple and can be useful for developers who only starting their adventure to neural networks and AIs.

In future this app can be rewrote with graphics interface but for now we had enough NNs
"""

# --------------------------------------------------- IMPORTS -----------------------------------
from PIL import Image  # needs to open and use images
from sklearn.cluster import KMeans  # needs to use AI
import numpy as np  # needs for math
import math  # needs for math too

# --------------------------------------------------- CUSTOM LISTS AND METHODS ------------------
# getting distance to the center of color
def delta(a, b):
    result = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2
    return math.sqrt(result)


# list of apples colors and their average RGB values + fully white and black backs
# numbers got by running the program without last loop's block - instead of this there were print(i)
colors = {"red": (175, 70, 70),
          "yellow": (230, 200, 50),
          "green": (100, 130, 50),
          # backgrouns colors are obvious
          "white background": (255, 255, 255),
          "black background": (0, 0, 0)}


# --------------------------------------------------- THAN ALL COMMANDS ARE EXECUTING IN ORDER --
# basic input of file name and adding directory
imgName = input("Enter the name of image WITH extension: ")
image = Image.open("images/" + imgName)

# getting every single pixel of image
pixels = []
for w in range(image.size[0]):  # running through all width
    for h in range(image.size[1]):  # and through all height
        pixel = image.getpixel((w, h))  # getting pixel with W and H coordinates
        pixels.append(pixel)  # adding this pixel to array

# converting common python array to numpy array
imageColors = np.array(pixels)

kmeans = KMeans(n_clusters=2)  # creating 2 color clusters for black/white and for yellow/red/green
kmeans.fit(imageColors)  # splitting pixels to clusters

# finding color
for i in kmeans.cluster_centers_:
    outputColor = "green"  # some basic color

    # running through all possible colors from list
    for color in colors:
        # if center of color from list less than color that we have wrote previously...
        if delta(colors[color], i) < delta(colors[outputColor], i):
            outputColor = color  # ... than setting color from list as basic

    # and if name of outputting color doesn't include word 'background' than it is red, yellow or green
    if outputColor.find("background") == -1:
        print("Apple in picture is " + outputColor)  # and then printing it to console
