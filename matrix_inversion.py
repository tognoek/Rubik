import numpy
import math
class MatrixInversion:
    def __init__(self):
        self.Rx = None
        self.Ry = None
        self.Rz = None
    
    def createRx(self, angle):
        # Create Matrix Rx in Beneral 3D Rotation
        angle = numpy.radians(angle)
        return numpy.array([[1, 0, 0],
                          [0, math.cos(angle), -math.sin(angle)],
                          [0, math.sin(angle), math.cos(angle)]])
    
    def createRy(self, angle):
        # Create Matrix Ry in Beneral 3D Rotation
        angle = numpy.radians(angle)
        return numpy.array([[math.cos(angle), 0, math.sin(angle)],
                          [0, 1, 0],
                          [-math.sin(angle), 0, math.cos(angle)]])
    
    def createRz(self, angle):
        # Create Matrix Rz in Beneral 3D Rotation
        angle = numpy.radians(angle)
        return numpy.array([[math.cos(angle), -math.sin(angle), 0],
                          [math.sin(angle), math.cos(angle), 0],
                          [0, 0, 1]])

    def rotationeX(self, points, angle):
        # Apply rotationeX on points
        points = numpy.array(points)
        Rx = self.createRx(angle)
        return numpy.dot(Rx, points)
    
    def rotationeY(self, points, angle):
        # Apply rotationeY on points
        points = numpy.array(points)
        Ry = self.createRy(angle)
        return numpy.dot(Ry, points)
    
    def rotationeZ(self, points, angle):
        # Apply rotationeZ on points
        points = numpy.array(points)
        Rz = self.createRz(angle)
        return numpy.dot(Rz, points)
    
    def rotate_vertices(self, vertices, angles):
        # Apply rotation on all vertices
        for i in range(len(vertices)):
            vertices[i] = self.rotationeX(vertices[i], angles['X'])
        for i in range(len(vertices)):
            vertices[i] = self.rotationeY(vertices[i], angles['Y'])
        for i in range(len(vertices)):
            vertices[i] = self.rotationeZ(vertices[i], angles['Z'])
        return vertices
    
class Matrix3D:
    def __init__(self):
        self.none = None
    def rotate_layer_xz(self, cube, y_layer, direction):
        cube[y_layer] = numpy.rot90(cube[y_layer], k=-direction)
        return cube
    def rotate_layer_xy(self, cube, z_layer, direction):
        cube[:, z_layer, :] = numpy.rot90(cube[:, z_layer, :], k=-direction)
        return cube
    def rotate_layer_yz(self, cube, x_layer, direction):
        cube[:, :, x_layer] = numpy.rot90(cube[:, :, x_layer], k=-direction)
        return cube

    def get_layer_x(self, cube, x_layer):
        return cube[:, :, x_layer]

    def get_layer_y(self, cube, y_layer):
        return cube[y_layer]
    
    def get_layer_z(self, cube, z_layer):
        return cube[:, z_layer, :]