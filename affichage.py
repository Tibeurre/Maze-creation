import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap

colors = ['black', 'white', 'green', 'red']  # 0=mur, 1=chemin, 2=départ, 3=arrivée
cmap = ListedColormap(colors)

def affiche_maze(maze):
    plt.imshow(maze, cmap=cmap)
    plt.axis('off')
    plt.title("Maze")
    plt.show()
    return