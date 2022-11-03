import random
import pygame
import time
import os
from sys import platform

pygame.init()
X=600
Y=600

s = pygame.display.set_mode((X, Y))
pygame.display.set_caption('wumpus')
pygame.font.init()

font = pygame.font.SysFont('Comic Sans MS', 30)

if platform == "win32":

    img_graph = pygame.image.load(os.getcwd()+'\graph.png')
    img_wumpus = pygame.image.load(os.getcwd()+'\wumpus.png')
    img_hole = pygame.image.load(os.getcwd()+'\hole.png')
    img_gold = pygame.image.load(os.getcwd()+'\gold.png')
    img_exit = pygame.image.load(os.getcwd()+'\exit.png')
    img_robot = pygame.image.load(os.getcwd()+"\\robot.png")

else:

    img_graph = pygame.image.load(os.getcwd()+'/graph.png')
    img_wumpus = pygame.image.load(os.getcwd()+'/wumpus.png')
    img_hole = pygame.image.load(os.getcwd()+'/hole.png')
    img_gold = pygame.image.load(os.getcwd()+'/gold.png')
    img_exit = pygame.image.load(os.getcwd()+'/exit.png')
    img_robot = pygame.image.load(os.getcwd()+"/robot.png")

def wait():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                return

graph = {
    '1' :  ['2'  , '8'   , '5'   ,' ', ' ', '40', '275'],
    '2' :  ['1'  , '3'   , '10'  ,' ', ' ', '95', '29'],
    '3' :  ['2'  , '4'   , '12'  ,' ', ' ', '165', '89'],
    '4' :  ['3'  , '14'  , '5'   ,' ', ' ', '130', '170'],
    '5' :  ['4'  , '1'   , '6'   ,' ', ' ', '123', '252'],
    '6' :  ['5'  , '15'  , '7'   ,' ', ' ', '190', '296'],
    '7' :  ['6'  , '17'  , '8'   ,' ', ' ', '270', '342'],
    '8' :  ['1'  , '7'   , '11'  ,' ', ' ', '270', '410'],
    '9' :  ['12' , '10'  , '19'  ,' ', ' ', '380', '89'],
    '10' : ['2'  , '9'   , '11'  ,' ', ' ', '450', '30'],
    '11' : ['10' , '20'  , '8'   ,' ', ' ', '505', '275'],
    '12' : ['3'  , '13'  , '9'   ,' ', ' ', '270', '90'],
    '13' : ['12' , '14'  , '18'  ,' ', ' ', '270', '147'],
    '14' : ['4'  , '13'  , '15'  ,' ', ' ', '210', '190'],
    '15' : ['14' , '16'  , '6'   ,' ', ' ', '240', '253'],
    '16' : ['15' , '18'  , '17'  ,' ', ' ', '305', '252'],
    '17' : ['16' , '7'   , '20'  ,' ', ' ', '355', '298'],
    '18' : ['13' , '16'  , '19'  ,' ', ' ', '330', '189'],
    '19' : ['9'  , '18'  , '20'  ,' ', ' ', '400', '175'],
    '20' : ['19' , '17'  , '11'  ,' ', ' ', '425', '252']
}





file = open('sample.txt', 'r')
for line in file.readlines():

    x = line.split(',')
    y = []
    for z in x:
        y.append(z.replace("\n",""))
    x = y

    graph [ x[0] ] [ 3 ] = x[1]




for i in graph:
    if graph[i][3] == 'exit':
        player_node = i
got_gold = 0
options = []
moves = []
moves.append(player_node)

status = True
while (status):

    
    s.fill((255,255,255))
    s.blit(img_graph, (0,0))

    for i in graph:

        if graph[i][3] == 'gold':
            s.blit( img_gold, (int(graph[i][5]),int(graph[i][6])) )

        if graph[i][3] == 'wumpus':
            s.blit( img_wumpus, (int(graph[i][5]),int(graph[i][6])) )

        if graph[i][3] == 'hole':
            s.blit( img_hole, (int(graph[i][5]),int(graph[i][6])) )

        if graph[i][3] == 'exit':
            s.blit( img_exit, (int(graph[i][5]),int(graph[i][6])) )

    s.blit(img_robot, (int(graph[player_node][5]),
                    int(graph[player_node][6])) )

    pygame.display.update()

    if graph[player_node][3] == 'gold':
        got_gold = '1'
        graph[player_node][3] = ' '

    if got_gold == '1' and graph[player_node][3] == 'exit': 
        print('You made it!')
        exit()

    if graph[player_node][3] == 'wumpus':
        print('You were eaten by the Wumpus.')
        exit()

    if graph[player_node][3] == 'hole':
        print('You fell down a hole.')
        exit()

    print('Moves: ')
    print(moves)

    if got_gold == '1':
        player_node = moves.pop()
        #player_node = moves.pop()
        options = []
        options.append(graph[player_node][0])
        options.append(graph[player_node][1])
        options.append(graph[player_node][2])
        print("I have gold, I'm going back...")
    else:
        rnd = random.randint(0,2)

        options.append(graph[player_node][0])
        options.append(graph[player_node][1])
        options.append(graph[player_node][2])

        print('Position: '+player_node)
        print('Options: ')
        print(options)


        while graph[options[rnd]][4] == 'danger':
            rnd = random.randint(0,2)


        if graph[options[0]][3] == 'wumpus' or graph[options[1]][3] == 'wumpus' or graph[options[2]][3] == 'wumpus' or graph[options[0]][3] == 'hole' or graph[options[1]][3] == 'hole' or graph[options[2]][3] == 'hole':  

            print('\nI feel danger.')
            graph[player_node][4] = 'danger'
            player_node = moves.pop()
            player_node = moves.pop()

            print('New Position: '+player_node)

            options = []
            options.append(graph[player_node][0])
            options.append(graph[player_node][1])
            options.append(graph[player_node][2])

            print('New Options: ')
            print(options)

        else:
            player_node = options[rnd]
            moves.append(player_node)

        options = []
        print()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            status = False

    pygame.display.update()
    wait()

pygame.quit()





