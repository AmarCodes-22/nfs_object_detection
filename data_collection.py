import os

import cv2
from Xlib import display

from screen_capture import ScreenCapture

raw_video_name = 'video3.avi'
raw_image_name = 'image1.jpg'
processed_video_name = 'video1_processed.avi'
processed_image_name = 'image1_processed.jpg'

paths = {
    'raw_video': os.path.join(os.getcwd(),
                              'data',
                              'raw',
                              'videos',
                               raw_video_name),
    'raw_image' : os.path.join(os.getcwd(),
                               'data',
                               'raw',
                               'images',
                                raw_image_name),
    'processed_video': os.path.join(os.getcwd(),
                              'data',
                              'processed',
                              'videos',
                               processed_video_name),
    'processed_image' : os.path.join(os.getcwd(),
                               'data',
                               'processed',
                               'images',
                                processed_image_name)
}

game_screen = ScreenCapture('Wine')
frame_width, frame_height = game_screen.window_pos[2], game_screen.window_pos[3]

dsp = display.Display()
out = cv2.VideoWriter(paths['raw_video'],
                      cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                      60,
                      (frame_width, frame_height))

while True:
    frame = game_screen.screenshot(dsp=dsp)
    out.write(frame)
    print('Recording')
    if cv2.waitKey(1) == ord('q'):
        break

out.release()
