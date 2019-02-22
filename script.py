import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import time
import os
from tqdm import tqdm
import string

FONT_SIZE = 24
FONT_PATH = 'fonts/'
FONT_COLOR = (255, 255, 255)
BLANK_IMAGE = np.zeros((32,32,3),np.uint8)
DATASET_PATH = 'dataset/'

if not os.path.exists(DATASET_PATH):
    os.mkdir(DATASET_PATH[:-1])

# numbers = list(range(0,10)) + ['.']
numbers = ['.']

# characters = list(string.ascii_uppercase)

ALL_CHARS = numbers

# for character in ALL_CHARS:
#     if not os.path.exists(DATASET_PATH + str(character)):
#         os.mkdir(DATASET_PATH + str(character))

os.mkdir(DATASET_PATH + 'dot')

# iterating through all the fonts in the directory
for font_file in tqdm(os.listdir('fonts/')):

    # parsing through all characters
    for character in ALL_CHARS:
        
        character = str(character)

        direc_charac = 'dot'

        for size in range(FONT_SIZE, 29):

            # Setting font type for drawing
            font_type = ImageFont.truetype(FONT_PATH + font_file, size)

            # Creating canvas to draw on
            canvas = Image.fromarray(BLANK_IMAGE)
            
            # Setting canvas for drawing
            draw = ImageDraw.Draw(canvas)

            # Drawing specified text on canvas
            draw.text((7, 2),  character, font = font_type, fill = FONT_COLOR)

            # Getting the drawn canvas
            drawn_canvas = np.array(canvas)

            # Directory to save the drawn_canvas
            directory_grayscale = DATASET_PATH + direc_charac + '/' + font_file[:-4] + '_' + str(size) + '_' + 'grayscale.jpg'
            directory_binary = DATASET_PATH + direc_charac + '/' + font_file[:-4] + '_' + str(size) + '_' + 'binary.jpg'

            # Saving grayscaled image to directory 
            cv2.imwrite(directory_grayscale, drawn_canvas)

            # Binarizing image
            thresh = cv2.imread(directory_grayscale, 0)
            _, thresh = cv2.threshold(thresh, 200, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            # Saving binarized image
            cv2.imwrite(directory_binary, thresh)