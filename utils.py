import time

class FPS:
    """
    Handles the frames per second display
    """
    def __init__(self):
        self.start_time = None
        self.end_time = None
        pass

    def set_start_time(self):
        """
        Use this to set the start time to the current time.
        """
        self.start_time = time.time()
    
    def set_end_time(self):
        """
        Use this to set the end time to the current time.
        """
        self.end_time = time.time()

    def print_fps(self):
        """
        Print the fps using this.
        """
        time_diff = self.end_time - self.start_time
        fps = 1 / time_diff
        print(fps)

