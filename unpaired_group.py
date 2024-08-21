import numpy as np
from manim import *

class unpaired_group:
    length = ''
    angle = ''
    origin = ''
    line_length = .5
    points = []
    arcs = []
    index_of_pairs = []
    center = 0
    radius = 0
    circle = 0

    def __init__(self, origin, length, angle, index_of_pairs):
        self.length = length
        self.angle = angle
        self.origin = origin
        self.index_of_pairs = index_of_pairs
        self.radius = self.line_length * self.length / (2 * PI)
        self.center = [origin[0] + np.sqrt(self.radius**2 - (self.line_length/2)**2), origin[1] + self.line_length / 2, origin[2] + 0]
        self.center = np.dot(rotation_matrix(self.angle, [0, 0, 1]), self.center)

    def create(self):
        curr_point = self.origin
        rot_matrix = rotation_matrix(self.angle, [0, 0, 1])

        self.circle = Circle(self.radius)
        self.circle.move_to(self.center)
        angle = self.angle
        for i in range(self.length):
            if i in self.index_of_pairs:
                self.arcs.append(Arc(start_angle=0, angle=2 * PI / self.length))
            else:
                self.points.append(Dot(np.dot(rot_matrix, curr_point)))
            self.angle += 2 * PI / self.length
            curr_point = self.circle.point_at_angle(angle)
        
    def get_objects(self):
        temp = [self.circle]
        return *self.points, *self.arcs, *temp