from PIL import Image
import face_recognition as fr
import argparse
import cv2
import random
import time

parse = argparse.ArgumentParser()
parse.add_argument("filename", type=str)
args = parse.parse_args()
filename = args.filename

image = fr.load_image_file(filename)
face_locations = fr.face_locations(image)
face_landmarks_list = fr.face_landmarks(image)

for face_location in face_locations:
    t, r, b, l = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(t, l, b, r))

    face_image = image[t:b, l:r]
    random.seed(time.time_ns())
    colour = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255)) # Yes, I am british
    cv2.rectangle(image, (l, t), (r, b), colour, int(abs(t-b)/40)) # draw a box around the face
    pil_image = Image.fromarray(image)
    pil_image.show()