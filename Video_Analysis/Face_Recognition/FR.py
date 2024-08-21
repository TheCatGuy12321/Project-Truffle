import face_recognition as fr
import argparse
import cv2

parse = argparse.ArgumentParser()
parse.add_argument("filename", type=str)
args = parse.parse_args()
filename = args.filename

input_movie = cv2.VideoCapture(filename)

length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')

output_movie = cv2.VideoWriter(filename="output.avi", fourcc=fourcc, fps=float(input_movie.get(cv2.CAP_PROP_FPS)),
                        frameSize=(int(input_movie.get(cv2.CAP_PROP_FRAME_WIDTH)), int(input_movie.get(cv2.CAP_PROP_FRAME_HEIGHT))))
frame_number = 0
while True:
    ret, frame = input_movie.read()
    frame_number += 1

    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = fr.face_locations(rgb_frame)
    for (top, right, bottom, left) in face_locations:
        colour = (33, 43, 237) # yes I'm british
        cv2.rectangle(frame, (left, top), (right, bottom), colour, int(abs(top-bottom)/40)) # draw a box around the face

    print("Writing frame {} / {}".format(frame_number, length))

    output_movie.write(frame)

# All done!
input_movie.release()
cv2.destroyAllWindows()