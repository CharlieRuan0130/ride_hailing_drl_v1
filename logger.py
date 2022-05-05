import logging

"""
Created by Charlie 5/3/22, just for a placeholder so that the file can run.
Ask Mark for the actual logger file (or utils).
"""

class Logger(object):
    def __init__(self, logname, now, time_start):
        self.logname = logname
        self.now = now 
        self.time_start = time_start 
        self.path_weights = 'path_weights/'
    
    def write(self, display):
        pass

    def close(self):
        pass

    def log(self, input_dict):
        pass