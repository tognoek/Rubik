from matrix_inversion import MatrixInversion, Plane
import pygame
from pixel import Pixel
class Block:
    def __init__(self, position, id):
        self.inversion = MatrixInversion()
        self.plane = Plane()
        self.len = 1
        self.id = id
        self.position = position
        self.angles = {'X' : 0, 'Y' : 0, 'Z' : 0}
        self.vertices = [[ self.len,  self.len,  self.len],  # Đỉnh 0
                         [ self.len,  self.len, -self.len],  # Đỉnh 1
                         [ self.len, -self.len,  self.len],  # Đỉnh 2
                         [ self.len, -self.len, -self.len],  # Đỉnh 3
                         [-self.len,  self.len,  self.len],  # Đỉnh 4
                         [-self.len,  self.len, -self.len],  # Đỉnh 5
                         [-self.len, -self.len,  self.len],  # Đỉnh 6
                         [-self.len, -self.len, -self.len]]  # Đỉnh 7
        self.size = 30
        self.screen = (800, 600)
        self.edges = [
                    (0, 1),  # Đỉnh 0 nối với đỉnh 1
                    (0, 2),  # Đỉnh 0 nối với đỉnh 2
                    (0, 4),  # Đỉnh 0 nối với đỉnh 4
                    (1, 3),  # Đỉnh 1 nối với đỉnh 3    
                    (1, 5),  # Đỉnh 1 nối với đỉnh 5
                    (2, 3),  # Đỉnh 2 nối với đỉnh 3
                    (2, 6),  # Đỉnh 2 nối với đỉnh 6
                    (3, 7),  # Đỉnh 3 nối với đỉnh 7
                    (4, 5),  # Đỉnh 4 nối với đỉnh 5
                    (4, 6),  # Đỉnh 4 nối với đỉnh 6
                    (5, 7),  # Đỉnh 5 nối với đỉnh 7
                    (6, 7)]  # Đỉnh 6 nối với đỉnh 7
        for i in range(len(self.vertices)):
            self.vertices[i][0] += self.position[0] * 2 * self.len
            self.vertices[i][1] += self.position[1] * 2 * self.len
            self.vertices[i][2] += self.position[2] * 2 * self.len
        self.color = [None, None, None, None, None, None]
    def get(self) -> int:
        return self.id
    
    def setColors(self, colors):
        self.colors = colors

    def getPixel(self):
        planes = [[4, 5, 6, 7],
                  [4, 0, 2, 6],
                  [0, 1, 2, 3],
                  [1, 3, 5, 7],
                  [4, 0, 1, 5],
                  [6, 2, 3, 7]]
        result = []
        for childPlane in planes:
            vertices = []
            for palne in childPlane:
                vertices.append(self.vertices[palne] * self.size)
            self.plane.setDatas(vertices)
            result.append(self.plane.getResult())
        pixels = []
        for index in range(len(result)):
            for res in result[index]:
                pixel = (res, (255, 255, 255))
                pixels.append(pixel)
        return pixels
    
    def reset(self):
        self.vertices = [[ self.len,  self.len,  self.len],  # Đỉnh 0
                         [ self.len,  self.len, -self.len],  # Đỉnh 1
                         [ self.len, -self.len,  self.len],  # Đỉnh 2
                         [ self.len, -self.len, -self.len],  # Đỉnh 3
                         [-self.len,  self.len,  self.len],  # Đỉnh 4
                         [-self.len,  self.len, -self.len],  # Đỉnh 5
                         [-self.len, -self.len,  self.len],  # Đỉnh 6
                         [-self.len, -self.len, -self.len]]  # Đỉnh 7
        
    def updateAngels(self, angles = (0, 0, 0)):
        index = 0
        for i in self.angles:
            self.angles[i] += angles[index]
            if self.angles[i] == 360:
                self.angles[i] = 0
            index += 1

    def write(self):
        return self.angles

    def update(self, angles = (0, 0, 0)):
        self.updateAngels(angles)
        tempAngles = {'X' : angles[0], 'Y' : angles[1], 'Z' : angles[2]}
        self.vertices = self.inversion.rotate_vertices(self.vertices, tempAngles)

    def render(self, display : pygame.Surface):
        for edge in self.edges:
            pygame.draw.line(display, (255, 255, 255), 
                             (self.vertices[edge[0]][0] * self.size + self.screen[0] // 2, 
                              self.vertices[edge[0]][1] * self.size + self.screen[1] // 2),
                               (self.vertices[edge[1]][0] * self.size + self.screen[0] // 2, 
                                self.vertices[edge[1]][1] * self.size + self.screen[1] // 2))