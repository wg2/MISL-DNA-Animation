from manim import *
import paired_group
import unpaired_group
class CreateDNALine(Scene):
    def construct(self):
        notation = "...((((..+.))+))..."
        stackOfParen = []
        listOfIndexes = {}
        listOfPlus = []
        numOf = 0

        for i, string in enumerate(notation):
            if string == '(':
                numOf += 1
                stackOfParen.append(numOf - 1)
            elif string == ')':
                numOf += 1
                listOfIndexes.update({stackOfParen.pop(): numOf - 1})
            elif string == "+":
                listOfPlus.append(numOf - 1)
            else:
                numOf += 1

        
        lineLength = .5
        dots = []
        lines = []
        curves = []
        xVal = -numOf * (.25)
        for i in range(numOf - 1):
            dots.append(Dot([xVal, 0, 0]))
            if not listOfPlus.__contains__(i):
                lines.append(Line(dots[i].get_center(), dots[i].get_center() + [lineLength, 0, 0]))
            xVal += lineLength


        
        
        dots.append(Dot([xVal, 0, 0]))

        for i in listOfIndexes.keys():
            start = dots[i].get_center()
            end = dots[listOfIndexes[i]].get_center()
            curves.append(ArcBetweenPoints(start, end, angle=-PI))
        

        if not curves:
            KeyError("No matching parenthesis found")
        self.add(*dots, *lines)
        for i in curves:
            self.play(Create(i))

class CreateDNAStructure(Scene):
    def construct(self):
        notation = "...((("
        stackOfParen = []
        listOfIndexes = {}
        listOfPlus = []
        groupsOfdots = []
        numOf = 0
        prevChar = ""
        for i, string in enumerate(notation):
            if string == '(':
                numOf += 1
                stackOfParen.append(numOf - 1)
                prevChar = "("
            elif string == ')':
                numOf += 1
                listOfIndexes.update({stackOfParen.pop(): numOf - 1})
                prevChar = ")"
            elif string == "+":
                listOfPlus.append(numOf - 1)
                prevChar = "+"
            elif string == ".":
                numOf += 1
                if prevChar == ".":
                    groupsOfdots[-1].append(numOf - 1)
                else:
                    groupsOfdots.append([numOf - 1])
                if i + 1 == len(notation) and notation[0] == "." and len(groupsOfdots) > 1:
                    groupsOfdots[0] = groupsOfdots[-1] + groupsOfdots[0]
                    groupsOfdots.pop()
                prevChar = "."
        
        lineLength = .5
        dots = []
        lines = []
        circles = []
        prevLocation = [0, 0, 0]
        angle = 0
        for i, string in enumerate(notation):
            if string == '.':
                size = len(groupsOfdots[0])
                radius = lineLength * size / (2 * PI)
                circles.append(Circle(radius=radius))
                dots.append(Dot(circles[0].point_at_angle(angle)))
                angle += 2 * PI / size
            elif string == '(':
                newLoc = prevLocation
                newLoc[0] += lineLength
                dots.append(Dot(newLoc))
                lines.append(Line(prevLocation, dots[-1].get_center()))
                prevLocation = dots[-1].get_center()
            #elif string == ')':

                

            
        self.add(*dots, *lines, *circles)
    
class paired_group_test(Scene):
    def construct(self):
        
        i = paired_group.paired_group(prev_item=0, next_item=0, origin=[0,0,0], length=5, angle=PI/6)
        i.create()
        self.add(*i.get_objects())

class unpaired_group_test(Scene):
    def construct(self):
        i = unpaired_group.unpaired_group(origin=[0,0,0], length=5, angle=PI/6, index_of_pairs=[0])
        i.create()
        self.add(*i.get_objects())
        