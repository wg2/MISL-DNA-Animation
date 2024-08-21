from manim import *
import numpy as np

class paired_group:
    points = []
    lines = []
    prev_item = ''
    next_item =''
    length=''
    angle=''
    origin=''
    line_length = .5

    def __init__(self, prev_item, next_item, origin, length, angle):
        self.prev_item = prev_item
        self.next_item = next_item
        self.length = length
        self.angle = angle
        self.origin = origin

    def create(self):
        curr_point = self.origin
        rot_matrix = rotation_matrix(self.angle, [0, 0, 1])
        for i in range(self.length - 1):
            print(curr_point)
            # origin side dot
            self.points.append(Dot(np.dot(rot_matrix, curr_point)))

            # dot for the pair opposite origin side
            temp = [curr_point[0], curr_point[1], curr_point[2]]
            temp[1] += self.line_length
            self.points.append(Dot(np.dot(rot_matrix, temp)))

            # line between the two paired dots
            self.lines.append(Line(np.dot(rot_matrix, curr_point), np.dot(rot_matrix, temp)))

            # origin side line between this and the next pair
            temp2 = [curr_point[0], curr_point[1], curr_point[2]]
            temp2[0] += self.line_length
            self.lines.append(Line(np.dot(rot_matrix, curr_point), np.dot(rot_matrix, temp2)))

            # line opposite origin side between this and the next pair
            temp3 = [curr_point[0], curr_point[1], curr_point[2]]
            temp3[0] += self.line_length
            temp3[1] += self.line_length
            self.lines.append(Line(np.dot(rot_matrix, temp), np.dot(rot_matrix, temp3)))

            curr_point[0] += self.line_length
        
        # last pair
        self.points.append(Dot(np.dot(rot_matrix, curr_point)))
        temp = [curr_point[0], curr_point[1], curr_point[2]]
        temp[1] += self.line_length
        self.points.append(Dot(np.dot(rot_matrix, temp)))
        self.lines.append(Line(np.dot(rot_matrix, curr_point), np.dot(rot_matrix, temp)))

    # gets the coordinates of the last dot on the origin side
    def get_attach_point(self):
        return self.points[-2].get_center()
    
    # gets the coordinates of the last dot on the opposite side
    def get_reattach_point(self):
        return self.points[-1].get_center()
    
    # gets the coordinates of the last dot on the origin side
    def end_attach_point(self):
        return self.points[1].get_center()
    
    def get_objects(self):
        return *self.points, *self.lines
