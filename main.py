import random as rd
import numpy as np 
import affichage as af

def generate(n = 11):

    if n<=2:
        n = 3
    if not n%2==1:
        n+=1
    
    maze = init(n)
    start,end = exits(n)

    maze = visit(maze,start)

    maze[start], maze[end] = 2,-1

    if end[0]==n-1:
        maze[(end[0]-1, end[1])] = 1
    else :
        maze[(end[0], end[1]-1)] = 1

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
        start = (0, rd.randint(2,n-3))
    else :
        start = (rd.randint(2,n-3),0)
    
    if head_or_tail():
        ex_ind = rd.randint(2,n-3)
        end = (n-1,ex_ind)
    else :
        ex_ind = rd.randint(2,n-3)
        end = (ex_ind,n-1)

    while end == start :
        ex_ind = rd.randint(2,n-3)
        end = (n-1, ex_ind)
    return start,end

def visit(maze,current):
    maze[current] = 1
    x, y = current

    while True:

        neighbors = []

        if (x > 1 and maze[x-2,y] <= 0) :
            neighbors.append(((x-1,y),(x-2,y)))
        if (x < maze.shape[0]-2 and maze[x+2,y] <= 0) :
            neighbors.append(((x+1,y),(x+2,y)))
        if (y > 1 and maze[x,y-2] <= 0) :
            neighbors.append(((x,y-1),(x,y-2)))
        if (y < maze.shape[1]-2 and maze[x,y+2] <= 0) :
            neighbors.append(((x,y+1),(x,y+2)))
        
        if neighbors == []:
            return maze
        else :
            print(neighbors)
            next_index = rd.randint(0,len(neighbors)-1)
            next = neighbors[next_index]
            maze[next[0]] = 1

        maze = visit(maze,next[1]).copy()

    return maze


def head_or_tail():
    return rd.randint(0,1)


af.affiche_maze(generate(95))