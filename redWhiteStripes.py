#Maya Carla Loleatha Anderson
#maya.anderson86@myhunter.cuny.edu
#this program displays: an image of the users input

import matplotlib.pyplot as plt
import numpy as np

size = int(input("Enter the size: "))
output = input("Enter output file: ")

img = np.ones((size, size, 3))
img[::2, :, 1:] = 0


plt.imsave(output, img)


