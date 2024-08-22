import pygame
import numpy
from matrix_inversion import Matrix3D
from block import Block

class Rubik:
    def __init__(self):
        self.matrix3d = Matrix3D()
        self.blocks = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                for z in [-1, 0, 1]:
                    block = Block((x, y, z), len(self.blocks))
                    self.blocks.append(block)
        self.cube = numpy.array([
                                [[ 0,  1,  2], [ 3,  4,  5], [ 6,  7,  8]],  # Lớp 0
                                [[ 9, 10, 11], [12, 13, 14], [15, 16, 17]],  # Lớp 1
                                [[18, 19, 20], [21, 22, 23], [24, 25, 26]]   # Lớp 2
                            ])
    def update(self, start = False):
        if start:
            for block in self.blocks:
                block.update()
            return
        # self.matrix3d.rotate_layer_yz(self.cube, 0, -1)
        # for i in range(90):
        for block in self.blocks:
                if block.get() < 9:
                    block.update((45, 0, 0))

    def render(self, display : pygame.Surface):
        for i in self.blocks:
            i.render(display)