import random as rd
import numpy as np 
import affichage as af

def generate(n =10):
    maze = init(n)
    start,end = exits(n)

    maze[start], maze[end] = 2,-1

    maze = fill(maze,start,end)

    maze[start], maze[end] = 2,-1

    return maze

def init(n):
    maze = np.zeros((n,n), dtype=int)
    for i in range(n):
        maze[0,i] = 3
        maze[n-1,i] = 3
        maze[i,0] = 3
        maze[i,n-1] = 3
    return maze

def exits(n):
    if head_or_tail():
        start = (0, rd.randint(1,n-2))
    else :
        start = (rd.randint(1,n-2),0)
    
    if head_or_tail():
        exit = (n-1,rd.randint(1,n-2))
    else :
        exit = (rd.randint(1,n-2),n-1)

    while exit == start :
        exit = (rd.randint(0,n-1),rd.randint(0,n-1))
    return start,exit

def fill(maze,start,end):
    current = start
    while current != end :
        available = free(maze,current)
        current = available[rd.randint(0,len(available)-1)]
        maze[current] = 1
    return maze

def free(maze,current):
    available = []
    stop = 0

    while available == [] and stop < 10 : #If no positions to "dig" : go to a random place "digged" and do it again
        stop += 1
        # Determining the available positions to "dig"
        x, y = current
        neighbors = []

        if (x > 1 and maze[x-2,y] <= 0) or (x == 1 and maze[x-1,y] <= 0) :
            neighbors.append((x-1,y))
        if (x < maze.shape[0]-2 and maze[x+2,y] <= 0) or (x == maze.shape[0]-2 and maze[x+1,y] <= 0) :
            neighbors.append((x+1,y))
        if (y > 1 and maze[x,y-2] <= 0) or (y == 1 and maze[x,y-1] <= 0) :
            neighbors.append((x,y-1))
        if (y < maze.shape[1]-2 and maze[x,y+2] <= 0) or (y == maze.shape[1]-2 and maze[x,y+1] <= 0) :
            neighbors.append((x,y+1))

        for el in neighbors : 
            if maze[el] == -1 :
                return [el] #priority to the exit
            else :
                available.append(el)

        if available == [] :
            #Put current at a random place if nowhere to dig
            one_list = [tuple(pos) for pos in np.argwhere(maze==1)]
            current = one_list[rd.randint(0,len(one_list)-1)]

    af.affiche_maze(maze)

    return available

def head_or_tail():
    return rd.randint(0,1)


af.affiche_maze(generate())