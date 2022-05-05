"""
Rewrote by Charlie 5/3, making it a dummy class, just to make train_MC.py runnable.
Will simply disable all functionalities of scaler, and make offset 0 and scale 1.
"""

import numpy as np
import pandas as pd

DIRECTORY = '../statistics/scaler/'
if not DIRECTORY.endswith('/'):
    DIRECTORY += '/'


class Scaler(object):
    def __init__(self, file_name='state_action_reinterpreted'):
        # mean_std = pd.read_csv(DIRECTORY + file_name + '.csv', index_col=0).drop(columns=['dimension'])
        # self.offset = mean_std['mean'].values
        # epsilon = max(min(mean_std['std'].min(), .1), 1e-4)
        # self.scale = 1. / (mean_std['std'].values + epsilon) / 3.
        # del mean_std
        self.offset = 0
        self.scale = 1

    def get(self):
        return self.scale, self.offset


def main():
    scaler = Scaler('state_action_reinterpreted')
    offset, scale = scaler.get()
    print('Offset: \n', offset[80:90])
    print('Scale: \n', scale[80:90])


if __name__ == '__main__':
    main()
