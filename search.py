import os
import random
import numpy as np
import re
from queue import Queue

maze = []
dr = os.path.abspath('.')
height = -2
startX, startY, endX, endY = 0, 0, 0, 0

file_paths = {
    "1": r"dataset\0.txt",
    "2": r"dataset\4.txt",
    "3": r"dataset\6.txt",
    "4": r"dataset\26.txt",
    "5": r"dataset\36.txt",
    "6": r"dataset\42.txt",
    "7": r"dataset\72.txt",
    "8": r"dataset\84.txt",
    "9": r"dataset\114.txt",
    "10": r"dataset\220.txt",
    "11": r"dataset\332.txt",
    "12": r"testovaci_data\00_11_11_1550177690.txt",
    "13": r"testovaci_data\01_71_51_156.txt",
    "14": r"testovaci_data\02_71_51_1552235384.txt"
}

mazeNumber = input("Pick a Maze(1-11): ")
if mazeNumber in file_paths:
    with open(file_paths[mazeNumber], 'r') as curr:
        for l in curr.readlines():
            height += 1
            maze.append(list(l))
else:
    print("Invalid input")

width = len(maze) - 1

newMaze = []
i = 0
j = 0

for i in maze:
    newMaze.append(i[0:-1])

xVal = maze[height]
s = ''.join(xVal)
xList = re.findall('\d+', s)
yVal = maze[height+1]
s = ''.join(yVal)
yList = re.findall('\d+', s)


startX = xList[0]
startY = xList[1]
endX = yList[0]
endY = yList[1]

rows = width
cols = height

maze1 = newMaze
maze1.remove(maze1[height])
maze1.remove(maze1[height])

closedMaze = maze1

maze1[int(startY)][int(startX)] = "s"
maze1[int(endY)][int(endX)] = "E"

def reconstruct_path(table, x):
        x = (int(endY), int(endX))
        path = []
        while x != (int(startY), int(startX)):
            path.append(x)
            x = table[x[0]][x[1]]
        return path

def RandSearch(maze):
        curr = (int(startY), int(startX))
        op = []
        cl = []
        holder = []
        op.append(curr)
        moves = ["l", "r", "u", "d"]
        solution = []

        i = 0
        while i < len(op):
            curr = random.choice(op)
            if curr == (int(endY), int(endX)):
                solution = reconstruct_path(maze, curr)
                for item in holder:
                    maze[item[0]][item[1]] = "#"
                for item in solution:
                    maze[item[0]][item[1]] = "-"

                maze1[int(startY)][int(startX)] = "S"
                maze1[int(endY)][int(endX)] = "E"

                count = 0
                while count < height:
                    final = maze1[count]
                    s = ''.join(final)
                    print(s)
                    count+=1

            for m in moves:
                    x = curr[0]
                    y = curr[1]
                    if m == "l":
                        x-=1
                        tmp = (x, y)
                        if maze[tmp[0]][tmp[1]] == "X":
                            if tmp not in cl:
                                cl.append(tmp)
                                if tmp in op:
                                    op.remove(tmp)
                        elif tmp not in cl:
                            if tmp not in op:
                                op.append(tmp)
                                holder.append(tmp)
                                maze[tmp[0]][tmp[1]] = curr
                    elif m == "r":
                        x+=1
                        tmp = (x, y)
                        if maze[tmp[0]][tmp[1]] == "X":
                            if tmp not in cl:
                                cl.append(tmp)
                                if tmp in op:
                                    op.remove(tmp)
                        elif tmp not in cl:
                            if tmp not in op:
                                op.append(tmp)
                                holder.append(tmp)
                                maze[tmp[0]][tmp[1]] = curr
                    elif m == "u":
                        y-=1
                        tmp = (x, y)
                        if maze[tmp[0]][tmp[1]] == "X":
                            if tmp not in cl:
                                cl.append(tmp)
                                if tmp in op:
                                    op.remove(tmp)
                        elif tmp not in cl:
                            if tmp not in op:
                                op.append(tmp)
                                holder.append(tmp)
                                maze[tmp[0]][tmp[1]] = curr
                    elif m == "d":
                        y+=1
                        tmp = (x, y)
                        if maze[tmp[0]][tmp[1]] == "X":
                            if tmp not in cl:
                                cl.append(tmp)
                                if tmp in op:
                                    op.remove(tmp)
                        elif tmp not in cl:
                            if tmp not in op:
                                op.append(tmp)
                                holder.append(tmp)
                                maze[tmp[0]][tmp[1]] = curr
            op.remove(curr)
            cl.append(curr)
        print(f"Nodes Expanded: {len(holder) + len(solution)}\nPath Length: {len(solution)}")


def DFS(maze):
    op = []
    cl = []
    test = []
    solution = []
    curr = (int(startY), int(startX))
    moves = ["l", "r", "u", "d"]

    op.append(curr)
    i = 0
    while i < len(op):
        curr = op.pop()

        if curr == (int(endY), int(endX)):
            solution = reconstruct_path(maze, curr)

            for items in test:
                maze[items[0]][items[1]] = "#"
            for item in solution:
                maze[item[0]][item[1]] = "-"
                
            maze1[int(startY)][int(startX)] = "S"
            maze1[int(endY)][int(endX)] = "E"

            count = 0
            while count < height:
                final = maze1[count]
                s = ''.join(final)
                print(s)
                count+=1

            print(f"Nodes Expanded: {len(test) + len(solution)}\nPath Length: {len(solution)}")

        for m in moves:
                x = curr[0]
                y = curr[1]
                if m == "l":
                    x-=1
                    tmp = (x, y)
                    #moveHelp(tmp, curr, cl, op)
                    if maze1[tmp[0]][tmp[1]] == "X":
                        if tmp not in cl:
                            cl.append(tmp)

                    elif tmp not in cl:
                        if tmp not in op:
                            op.append(tmp)
                            test.append(tmp)
                            maze[tmp[0]][tmp[1]] = curr
                elif m == "r":
                    x+=1
                    tmp = (x, y)
                    if maze1[tmp[0]][tmp[1]] == "X":
                        if tmp not in cl:
                            cl.append(tmp)

                    elif tmp not in cl:
                        if tmp not in op:
                            op.append(tmp)
                            test.append(tmp)
                            maze[tmp[0]][tmp[1]] = curr
                elif m == "u":
                    y-=1
                    tmp = (x, y)
                    if maze1[tmp[0]][tmp[1]] == "X":
                        if tmp not in cl:
                            cl.append(tmp)

                    elif tmp not in cl:
                        if tmp not in op:
                            op.append(tmp)
                            test.append(tmp)
                            maze[tmp[0]][tmp[1]] = curr
                elif m == "d":
                    y+=1
                    tmp = (x, y)
                    if maze1[tmp[0]][tmp[1]] == "X":
                        if tmp not in cl:
                            cl.append(tmp)

                    elif tmp not in cl:
                        if tmp not in op:
                            op.append(tmp)
                            test.append(tmp)
                            maze[tmp[0]][tmp[1]] = curr
        cl.append(curr)


def Greedy(maze):
    op = []
    cl = []
    test = []
    solution = []
    curr = (int(startY), int(startX))
    moves = ["l", "r", "u", "d"]

    op.append(curr)
    i = 0
    while i < len(op):
        op.sort(reverse=True)
        curr = op.pop()
        
        if curr == (int(endY), int(endX)):
            solution = reconstruct_path(maze, curr)
            for items in test:
                maze[items[0]][items[1]] = "#"
            for item in solution:
                maze[item[0]][item[1]] = "-"

            maze1[int(startY)][int(startX)] = "S"
            maze1[int(endY)][int(endX)] = "E"
            
            count = 0
            while count < height:
                final = maze1[count]
                s = ''.join(final)
                print(s)
                count+=1

            print(f"Nodes Expanded: {len(test) + len(solution)}\nPath Length: {len(solution)}")

        for m in moves:
                x = curr[0]
                y = curr[1]
                if m == "l":
                    x-=1
                    tmp = (x, y)
                    if maze1[tmp[0]][tmp[1]] == "X":
                        if tmp not in cl:
                            cl.append(tmp)
                    elif tmp not in cl:
                        if tmp not in op:
                            op.append(tmp)
                            test.append(tmp)
                            maze[tmp[0]][tmp[1]] = curr
                elif m == "r":
                    x+=1
                    tmp = (x, y)
                    if maze1[tmp[0]][tmp[1]] == "X":
                        if tmp not in cl:
                            cl.append(tmp)
                    elif tmp not in cl:
                        if tmp not in op:
                            op.append(tmp)
                            test.append(tmp)
                            maze[tmp[0]][tmp[1]] = curr
                elif m == "u":
                    y-=1
                    tmp = (x, y)
                    if maze1[tmp[0]][tmp[1]] == "X":
                        if tmp not in cl:
                            cl.append(tmp)
                    elif tmp not in cl:
                        if tmp not in op:
                            op.append(tmp)
                            test.append(tmp)
                            maze[tmp[0]][tmp[1]] = curr
                elif m == "d":
                    y+=1
                    tmp = (x, y)
                    if maze1[tmp[0]][tmp[1]] == "X":
                        if tmp not in cl:
                            cl.append(tmp)
                    elif tmp not in cl:
                        if tmp not in op:
                            op.append(tmp)
                            test.append(tmp)
                            maze[tmp[0]][tmp[1]] = curr
        cl.append(curr)


def BFS(maze):
    op = Queue()
    cl = []
    test = []
    solution = []
    curr = (int(startY), int(startX))
    moves = ["l", "r", "u", "d"]

    op.put(curr)
    i = 0
    while not op.empty():
        curr = op.get()

        if curr == (int(endY), int(endX)):
            solution = reconstruct_path(maze, curr)
            for items in test:
                maze[items[0]][items[1]] = "#"
            for item in solution:
                maze[item[0]][item[1]] = "-"

            maze1[int(startY)][int(startX)] = "S"
            maze1[int(endY)][int(endX)] = "E"

            count = 0
            while count < height:
                final = maze1[count]
                s = ''.join(final)
                print(s)
                count+=1

            print(f"Nodes Expanded: {len(test) + len(solution)}\nPath Length: {len(solution)}")

        for m in moves:
                x = curr[0]
                y = curr[1]
                if m == "l":
                    x-=1
                    tmp = (x, y)
                    if maze1[tmp[0]][tmp[1]] == "X":
                        if tmp not in cl:
                            cl.append(tmp)

                    elif tmp not in cl:
                        if tmp not in test:
                            op.put(tmp)
                            test.append(tmp)
                            maze[tmp[0]][tmp[1]] = curr
                elif m == "r":
                    x+=1
                    tmp = (x, y)
                    if maze1[tmp[0]][tmp[1]] == "X":
                        if tmp not in cl:
                            cl.append(tmp)

                    elif tmp not in cl:
                        if tmp not in test:
                            op.put(tmp)
                            test.append(tmp)
                            maze[tmp[0]][tmp[1]] = curr
                elif m == "u":
                    y-=1
                    tmp = (x, y)
                    if maze1[tmp[0]][tmp[1]] == "X":
                        if tmp not in cl:
                            cl.append(tmp)

                    elif tmp not in cl:
                        if tmp not in test:
                            op.put(tmp)
                            test.append(tmp)
                            maze[tmp[0]][tmp[1]] = curr
                elif m == "d":
                    y+=1
                    tmp = (x, y)
                    if maze1[tmp[0]][tmp[1]] == "X":
                        if tmp not in cl:
                            cl.append(tmp)

                    elif tmp not in cl:
                        if tmp not in test:
                            op.put(tmp)
                            test.append(tmp)
                            maze[tmp[0]][tmp[1]] = curr
        cl.append(curr)


searchType = input("1. Random Search\n2. DFS\n3. BFS\n4. Greedy Search\n(Pick a number 1-5): ")
if searchType == "1":
    RandSearch(maze1)
elif searchType == "2":
    DFS(maze1)
elif searchType == "3":
    BFS(maze1)
elif searchType == "4":
    Greedy(maze1)
else:
    print("Invalid input")