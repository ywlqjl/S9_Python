import numpy as np
from xml.dom.minidom import parse
import xml.dom.minidom
from scipy.misc import *
import sys


width = 500
height = 500

pic = np.full((width + 1, height + 1, 3), 255, dtype=np.uint8)

# [x, y]
dic_orientation = {
    3:[-1,0], #up
    7:[1, 0], #down
    1: [0, -1], #left
    5: [0, 1], # right
    2: [-1, -1], # up_left
    4: [-1, 1], # up_right
    8: [1, -1], # down_left
    6: [1, 1] # down_right
}

class Ant:
    def __init__(self, origin, size, colors, scolors, proba, dtype, ps, orientation):
        self.size = size
        self.colors = colors
        self.scolors = scolors
        self.proba = proba
        self.dtype = dtype # move type, 0 => oblique, 1 => angle
        self.ps = ps
        self.origin = origin
        self.position = origin
        self.orientation = orientation # int
        self.neighbors = [] # order of this is: let, up, right
        self.neighbors_pos = []

    def printColor(self):
        pic[self.position[0]][self.position[1]] = self.colors

    def direction(self):
        """
        Get the direction
        :return:
        """
        d = np.random.random()
        # print("proba = "+str(d))
        if d < self.proba[0]: # left
            self.orientation -= (self.dtype + 1)
            if self.orientation <= 0:
                self.orientation = 8 - self.dtype
            return 0
        elif d >= (self.proba[0] + self.proba[1]): # right
            return 1
        else:
            self.orientation += (self.dtype + 1)
            if self.orientation > 8 - self.dtype:
                self.orientation = 1
            return 2


    def get_neighbors(self):
        """
        Get 3 neighbors with their color
        :return:
        """
        # print(self.orientation)
        self.neighbors.clear() # clear
        self.neighbors_pos.clear()
        # if self.dtype == 0:
        #     pass
        # else:
        if self.orientation == 3: # orientation up
            n2 = self.position + dic_orientation[1]
            self.neighbors_pos.append(n2)  # left
            self.neighbors.append(pic[n2[0], n2[1]])

            n1 = self.position + dic_orientation[3]
            self.neighbors_pos.append(n1) # up
            self.neighbors.append(pic[n1[0],n1[1]])

            n3 = self.position + dic_orientation[5]
            self.neighbors_pos.append(n3) # right
            self.neighbors.append(pic[n3[0], n3[1]])
        elif self.orientation == 7: # down
            n3 = self.position + dic_orientation[5]
            self.neighbors_pos.append(n3)  # right
            self.neighbors.append(pic[n3[0], n3[1]])

            n1 = self.position + dic_orientation[7]
            self.neighbors_pos.append(n1)  # down
            self.neighbors.append(pic[n1[0], n1[1]])

            n2 = self.position + dic_orientation[1]
            self.neighbors_pos.append(n2)  # left
            self.neighbors.append(pic[n2[0], n2[1]])
        elif self.orientation == 1: # left
            n3 = self.position + dic_orientation[7]
            self.neighbors_pos.append(n3)  # down
            self.neighbors.append(pic[n3[0], n3[1]])

            n2 = self.position + dic_orientation[1]
            self.neighbors_pos.append(n2)  # left
            self.neighbors.append(pic[n2[0], n2[1]])

            n1 = self.position + dic_orientation[3]
            self.neighbors_pos.append(n1)  # up
            self.neighbors.append(pic[n1[0], n1[1]])
        elif self.orientation == 5: # right
            n1 = self.position + dic_orientation[3]
            self.neighbors_pos.append(n1)  # up
            self.neighbors.append(pic[n1[0], n1[1]])

            n3 = self.position + dic_orientation[5]
            self.neighbors_pos.append(n3)  # right
            self.neighbors.append(pic[n3[0], n3[1]])

            n2 = self.position + dic_orientation[7]
            self.neighbors_pos.append(n2)  # down
            self.neighbors.append(pic[n2[0], n2[1]])

        elif self.orientation == 2: # up_left
            n3 = self.position + dic_orientation[5]
            self.neighbors_pos.append(n3)  # left
            self.neighbors.append(pic[n3[0], n3[1]])

            n1 = self.position + dic_orientation[2]
            self.neighbors_pos.append(n1)  # up_left
            self.neighbors.append(pic[n1[0], n1[1]])

            n2 = self.position + dic_orientation[3]
            self.neighbors_pos.append(n2)  # up
            self.neighbors.append(pic[n2[0], n2[1]])

        elif self.orientation == 4: # up_right
            n3 = self.position + dic_orientation[3]
            self.neighbors_pos.append(n3)  # up
            self.neighbors.append(pic[n3[0], n3[1]])

            n1 = self.position + dic_orientation[4]
            self.neighbors_pos.append(n1)  # up_right
            self.neighbors.append(pic[n1[0], n1[1]])

            n2 = self.position + dic_orientation[5]
            self.neighbors_pos.append(n2)  # right
            self.neighbors.append(pic[n2[0], n2[1]])

        elif self.orientation == 8:  # down_left
            n1 = self.position + dic_orientation[7]
            self.neighbors_pos.append(n1)  # down
            self.neighbors.append(pic[n1[0], n1[1]])

            n3 = self.position + dic_orientation[8]
            self.neighbors_pos.append(n3)  # down_left
            self.neighbors.append(pic[n3[0], n3[1]])

            n2 = self.position + dic_orientation[1]
            self.neighbors_pos.append(n2)  # left
            self.neighbors.append(pic[n2[0], n2[1]])

        elif self.orientation == 6:  # down_right
            n2 = self.position + dic_orientation[5]
            self.neighbors_pos.append(n2)  # right
            self.neighbors.append(pic[n2[0], n2[1]])

            n3 = self.position + dic_orientation[6]
            self.neighbors_pos.append(n3)  # down_right
            self.neighbors.append(pic[n3[0], n3[1]])

            n1 = self.position + dic_orientation[7]
            self.neighbors_pos.append(n1)  # down
            self.neighbors.append(pic[n1[0], n1[1]])


    def check_inside(self):
        """
        Test if the position is inside the graphe
        """
        if self.position[0] < 0:
            self.position[0] = width - 1
        elif self.position[0]>= width:
            self.position[0] = 0

        if self.position[1] < 0:
            self.position[1] = width - 1
        elif self.position[1] >= width:
            self.position[1] = 0

    # neighbor => 3 * 3
    def move(self):
        """
        :param neighbors:  color of neighbors
        :param neighbors_pos: position of neighbors
        :return: None
        """
        self.get_neighbors()
        follow = np.random.random()
        # print("ori:" + str(self.orientation))
        direction = self.direction()
        if follow < self.ps:
            # follow color

            for i, n in enumerate(self.neighbors):
                # print(n)
                lum = 0.2426 * n[0] + 0.7152 * n[1] + 0.0722 * n[2]
                lumNow = 0.2426 * self.colors[0] + 0.7152 * self.colors[1] + 0.0722 * self.colors[2]
                deltaLum = np.absolute(lum - lumNow)
                if deltaLum < 40:
                    # follow

                    self.printColor()
                    self.position = self.neighbors_pos[i]
                    # print("next:", self.neighbors_pos[i])
                    if i == 0:
                        self.orientation -= (self.dtype + 1)
                        if self.orientation <= 0:
                            self.orientation = 8 - self.dtype
                    if i == 2:
                        self.orientation += (self.dtype + 1)
                        if self.orientation > 8 - self.dtype:
                            self.orientation = 1
                else:
                    self.printColor()
                    self.position = self.neighbors_pos[direction]

                    # print("next:",self.neighbors_pos[direction])
        else:
            # print("not in follow")
            self.printColor()
            self.position = self.neighbors_pos[direction]
        self.check_inside()



if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Il faut indiquer un fichier .xml pour les paramètres!")
    else:
        # get parameters
        file = sys.argv[1]
        DOMTree = xml.dom.minidom.parse(file)
        collection = DOMTree.documentElement
        if collection.hasAttribute("nombre"):
            nombre = int(collection.getAttribute("nombre"))

        if collection.hasAttribute("iteration"):
            iteration = int(collection.getAttribute("iteration"))


        fourmis = collection.getElementsByTagName("fourmis")

        list_fourmis = []

        for f in fourmis:
            origin_position = np.random.random_integers(1, width - 1, 2)
            orientation = np.random.random_integers(1, 8)

            colors = f.getElementsByTagName('couleur_deposee')[0]
            colors = colors.childNodes[0].data.split(',')
            for i in range(0, len(colors)):
                colors[i] = int(colors[i].strip())

            scolors = f.getElementsByTagName('couleur_suivi')[0]
            scolors = scolors.childNodes[0].data.split(',')
            for i in range(0, len(scolors)):
                scolors[i] = int(scolors[i].strip())

            proba = f.getElementsByTagName('proba')[0]
            proba = proba.childNodes[0].data.split(',')
            for i in range(0, len(proba)):
                proba[i] = float(proba[i].strip())

            dtype = f.getElementsByTagName('type')[0]
            dtype = int(dtype.childNodes[0].data)

            ps = f.getElementsByTagName('proba_suivi')[0]
            ps = float(ps.childNodes[0].data)

            ant = Ant(origin_position, 1, colors, scolors, proba, dtype, ps, orientation)
            list_fourmis.append(ant)

        # movement
        for i in range(1, iteration):
            for f in list_fourmis:
                f.move()
        imsave('ants.jpg', pic)

        print("Movement finished")