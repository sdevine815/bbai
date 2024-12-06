from blocks import blocks
from random import choice, randint
import numpy as np

BOARD_SIZE = 8


class Blockblast:

    def __init__(self):
        self.board = np.zeros(BOARD_SIZE ** 2)

    def generate_block(self):
        shaped_block = np.array(choice(blocks)).reshape(5, 5)
        rot = np.rot90(shaped_block, randint(0, 3), (0, 1))

        # rot.

        vector_block = rot.reshape(5 ** 2)

        return vector_block
    
    #places using upper left corner of block
    def place_block(self, block, x, y):
        position = (BOARD_SIZE * y) + x

        upper_left = None
    
        for i in block.reshape(5, 5):
            print("row 1: ")
            print(i)


