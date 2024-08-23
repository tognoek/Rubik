import numpy
import copy
from matrix_inversion import Matrix3D
from block import Block

class Rubik:
    def __init__(self, display):
        self.const = "Tognoek"
        self.display = display
        self.rotation = self.const
        self.angle = 0
        self.erroAngles = (0, 0, 0)
        self.matrix3d = Matrix3D()
        self.blocks = []
        self.defaultAngle = 10
        self.sizeRotation = 9
        self.loop = []
        self.index = 0
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                for z in [-1, 0, 1]:
                    block = Block((x, y, z), len(self.blocks))
                    self.blocks.append(block)
        self.cubes = numpy.array([
                                [[ 2,  11,  20], [ 1,  10,  19], [ 0,  9,  18]],  # Lớp 0
                                [[ 5, 14, 23], [4, 13, 22], [3, 12, 21]],  # Lớp 1
                                [[8, 17, 26], [7, 16, 25], [6, 15, 24]]   # Lớp 2
                            ])
        self.blocksCopy = None
        
    def write(self):
        with open('data.txt', 'w') as f:
            # f.write(str(self.cubes))
            for block in self.blocks:
                f.writelines(str(block.get()) + " " + str(block.write()) + "\n")
            for cube in self.cubes:
                f.writelines(str(cube) + "\n")
        # print(self.cubes)

    def start(self):
        for block in self.blocks:
            block.update()

    def runLoop(self):
        if self.index < len(self.loop):
            if not self.isRotation():
                self.setRotation(self.loop[self.index])
                self.index += 1
        self.update()
        self.render()

    def addRotation(self, rotation):
        self.loop.append(rotation)
    
    def isRotation(self):
        return self.rotation != self.const

    def setRotation(self, rotation):
        if self.rotation != rotation:
            self.rotation = rotation
            self.angle = 0


    def update(self):
        if self.angle < self.sizeRotation:
            if self.rotation == 'F':
                self.F()
                self.angle += 1
            if self.rotation == 'D':
                self.D()
                self.angle += 1
            if self.rotation == 'B':
                self.B()
                self.angle += 1
            if self.rotation == 'L':
                self.L()
                self.angle += 1
            if self.rotation == 'R':
                self.R()
                self.angle += 1
            if self.rotation == 'U':
                self.U()
                self.angle += 1
        
        if self.angle == self.sizeRotation:
            self.setRotation(self.const)
    
    def controlRotation(self, angle = (0, 0, 0)):
        self.erroAngles = (self.erroAngles[0] + angle[0], 
                           self.erroAngles[1] + angle[1],
                           self.erroAngles[2] + angle[2])
        
    def resetRotations(self):
        self.erroAngles = (6, 6, 6)

    def controllErro(self):
        self.blocksCopy = copy.deepcopy(self.blocks)
        for block in self.blocksCopy:
            block.update(self.erroAngles)

    def resetErro(self):
        tempErroAngles = (-self.erroAngles[0],
                          -self.erroAngles[1],
                          -self.erroAngles[2])
        for block in self.blocks:
            block.update(tempErroAngles)
            
    def B(self, inverted = False):  
        array = self.matrix3d.get_layer_x(self.cubes, 2)
        array = array.reshape((-1))
        for block in self.blocks:
            if block.get() in array:
                block.update((self.defaultAngle, 0, 0))
        if self.angle == self.sizeRotation - 1:
            self.matrix3d.rotate_layer_yz(self.cubes, 2, 1)
    def D(self, inverted = False):
        array = self.matrix3d.get_layer_y(self.cubes, 2)
        array = array.reshape((-1))
        for block in self.blocks:
            if block.get() in array:
                block.update((0, self.defaultAngle, 0))
        if self.angle == self.sizeRotation - 1:
            self.matrix3d.rotate_layer_xz(self.cubes, 2, 1)
            # print(self.cubes)
    def F(self, inverted = False):
        array = self.matrix3d.get_layer_x(self.cubes, 0)
        array = array.reshape((-1))
        for block in self.blocks:
            if block.get() in array:
                block.update((self.defaultAngle, 0, 0))
        if self.angle == self.sizeRotation - 1:
            self.matrix3d.rotate_layer_yz(self.cubes, 0, 1)
            # print(self.cubes)
            
    def L(self, inverted = False):
        array = self.matrix3d.get_layer_z(self.cubes, 0)
        array = array.reshape((-1))
        for block in self.blocks:
            if block.get() in array:
                block.update((0, 0, self.defaultAngle))
        if self.angle == self.sizeRotation - 1:
            self.matrix3d.rotate_layer_xy(self.cubes, 0, 1)
    def R(self, inverted = False):
        array = self.matrix3d.get_layer_z(self.cubes, 2)
        array = array.reshape((-1))
        for block in self.blocks:
            if block.get() in array:
                block.update((0, 0, self.defaultAngle))
        if self.angle == self.sizeRotation - 1:
            self.matrix3d.rotate_layer_xy(self.cubes, 2, 1)
    def U(self, inverted = False):
        array = self.matrix3d.get_layer_y(self.cubes, 0)
        array = array.reshape((-1))
        for block in self.blocks:
            if block.get() in array:
                block.update((0, self.defaultAngle, 0))
        if self.angle == self.sizeRotation - 1:
            self.matrix3d.rotate_layer_xz(self.cubes, 0, 1)

    def render(self):
        self.controllErro()
        for block in self.blocksCopy:
            block.render(self.display)