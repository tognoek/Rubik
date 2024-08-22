from matrix_inversion import MatrixInversion
import pygame
class Block:
    def __init__(self, position, id):
        self.inversion = MatrixInversion()
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
    def get(self) -> int:
        return self.id
    
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
            index += 1

    def update(self, angles = (0, 0, 0)):
        self.reset()
        self.updateAngels(angles)
        for i in range(len(self.vertices)):
            self.vertices[i][0] += self.position[0] * 2 * self.len
            self.vertices[i][1] += self.position[1] * 2 * self.len
            self.vertices[i][2] += self.position[2] * 2 * self.len
        self.vertices = self.inversion.rotate_vertices(self.vertices, self.angles)

    def render(self, display : pygame.Surface):
        for i in self.edges:
            pygame.draw.line(display, (255, 255, 255), 
                             (self.vertices[i[0]][0] * self.size + self.screen[0] // 2, self.vertices[i[0]][1] * self.size + self.screen[1] // 2),
                               (self.vertices[i[1]][0] * self.size + self.screen[0] // 2, self.vertices[i[1]][1] * self.size + self.screen[1] // 2))