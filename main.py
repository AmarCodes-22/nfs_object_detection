import os

import cv2
from Xlib import display

from screen_capture import ScreenCapture
from utils import FPS

#! Change this to 'Wine' later.
game_screen = ScreenCapture('Wine')
fps = FPS()
dsp = display.Display()

frame_count = 0

while True:
    if frame_count == 20:
        fps.set_start_time()
    frame = game_screen.screenshot(dsp=dsp)

    #* Resize for windows that are too large. Decreases fps signigicantly.
    # frame = cv2.resize(frame, (200, 200))
    cv2.imshow('Test', frame)
    if frame_count == 20:
        fps.set_end_time()
        fps.print_fps()
        frame_count = 0
    if cv2.waitKey(1) == ord('q'):
        break

    frame_count += 1
