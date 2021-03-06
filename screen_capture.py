import subprocess
import re
from Xlib import display, X
from PIL  import Image
import cv2
import numpy as np
# import timeit

class ScreenCapture:
    """
    Handles functionality related to screen capture.
    
    Attributes:
        window_title (str): A unique word that appears
            in the title of the window to be captured.
        window_id (str): ID generated by unix command 'wmctrl -l'.
        window_pos (tuple(int)): The position inferred from the linux command
            'xwininfo -id {window_id}.
            
    Methods:
        get_window_id(): Gets the window_id and stores it in the attribute
            window_id
        get_window_position(): Gets the window coordinated and stores it in
            the attribute window_pos.
        screenshot(dsp): Takes a screenshot of the area bounded by window_pos
            and converts it to a numpy array
    """

    def __init__(self, window_name:str = 'Wine'):
        """
        Args:
            window_name (str): A literal that is unique to the title of the 
                window to be captured.
                default: 'Wine'"""
        self.window_title = window_name
        self.window_id = self.get_window_id()
        self.window_pos = self.get_window_position()

    def get_window_id(self):
        '''
        Gets the window id
        Returns:
            id (str): ID as provided by the wmctrl program.
        '''
        window_title = self.window_title
        windows = subprocess.run(['wmctrl', '-l'], stdout=subprocess.PIPE)
        windows = windows.stdout.decode('utf-8')
        windows = windows.split('\n')
        id = [window[:10] for window in windows if window_title in window][0]
        return id
    
    def get_window_position(self):
        """
        Gets the window position
        Returns:
            pos (tuple[int]): (abs_x, abs_y, width, height)
        """
        win_info = subprocess.run(['xwininfo', '-id', self.window_id],
                                  stdout=subprocess.PIPE)
        win_info = win_info.stdout.decode('utf-8')
        win_info = win_info.split('\n')
        num_regex = r'\d+'
        abs_x, abs_y, width, height = 0, 0, 0, 0
        for info in win_info:
            if 'Absolute' in info and 'X' in info:
                temp = re.search(num_regex, info)
                abs_x = int(temp.group(0))
            if 'Absolute' in info and 'Y' in info:
                temp = re.search(num_regex, info)
                abs_y = int(temp.group(0))
            if 'Width' in info:
                temp = re.search(num_regex, info)
                width = int(temp.group(0))
            if 'Height' in info:
                temp = re.search(num_regex, info)
                height = int(temp.group(0))
        
        pos = (abs_x, abs_y, width, height)
        return pos

    def screenshot(self, dsp:display.Display) -> np.ndarray:
        """
        Take a screenshot and convert it to numpy array.
        Args:
            dsp (display.Display): Initialized a single instance in 
                                   the main file.
        Returns:
            image (np.ndarray): The image in BGR color space.
        """
        width, height = self.window_pos[2], self.window_pos[3]
        x, y = self.window_pos[0], self.window_pos[1]

        #* Removed instantiating multiple display.Display objects because
        #* of decreasing fps with time.
        # dsp = display.Display()

        try:
            root = dsp.screen().root
            raw = root.get_image(x, y, width,height, X.ZPixmap, 0xffffffff)
            image = Image.frombytes("RGB",
                                    (width, height),
                                    raw.data,
                                    "raw",
                                    "BGRX")
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            return image
        finally: 
            # dsp.close()
            pass