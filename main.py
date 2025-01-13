from stuff import *
import random
from item import Item

indialogue = False

lvl1 = Level(
    'Use W/A/S/D to move around.',
    size=8, 
    exitPos=Pos(7, 7),
    message=colorama.Style.DIM + "you hear a whisper calling to you . . ." + colorama.Style.RESET_ALL
)
lvl2 = MazeLevel(
    'I',
    length=3,
    width=5,
    message=purple('WHAT BRINGS YOU TO MY DOMAIN?')
)
lvl3 = MazeLevel(
    'II',
    length=6,
    width=5,
    message=purple('IS IT TREASURE?')
)
lvl4 = MazeLevel(
    'III',
    length=7,
    width=6,
    message=purple('WHY ARE YOU IN SUCH A HURRY?')
)
lvl5 = MazeLevel(
    'IV',
    length=7,
    width=6,
    message=purple('WOW! BUT I\'M SURE YOU\'LL GIVE UP SOON')
)
lvl6 = Level(
    'INTERLUDE',
    exitPos=Pos(15, 15),
    message=colorama.Style.DIM + 'The calm before the storm.' + colorama.Style.RESET_ALL
)
lvl7 = MazeLevel(
    'V',
    length=7,
    width=6,
    message=purple('OH, YOU AREN\'T GIVING UP?')
)
lvl8 = MazeLevel(
    'VI',
    length=8,
    width=7,
    message=purple('OH WELL. YOU SHALL SUFFER AND SO SHALL THE PEOPLE!')
)
stage1 = True

villager1 = NPC(
    'Villager',
    [
        f'The tyranny of the {purple('Game Master')} has gone on for far too long!',
        f'{purple('He')} hoards {gold('treasure')} and treats us like slaves!',
        f'But {purple('he')}\'s always watching',
        '...'
    ]
)

villager2 = NPC(
    'Villager',
    [
        f'*covered in blood* PLEASE!!',
        'Do what you can to help us, and we shall be eternally grateful!',
        f'After winning, you can help yourself to {purple('his')} large hold of {gold('treasure')}!!!!',
        'PLS VRO 🙏🙏🙏🙏'
    ]
)

villager3 = NPC(
    'Medic',
    [
        'EVERYONE! GIVE US SPACE SO I CAN HELP THIS MAN!',
        '*whispering to you* this guys dying bro im not qualified enough 😭😭'
    ]
)

villager4 = NPC(
    colorama.Fore.RED + 'cool guy in trench coat' + colorama.Style.RESET_ALL,
    [
        f'I heard the {purple('Game Master')} will accept anyone to a challenge, if you complete his maze!',
        'You didn\'t hear that from me.',
        colorama.Style.DIM + '*vanishes*' + colorama.Style.RESET_ALL
    ]
)

lvl6.placeobject((4, 9), villager2)
lvl6.placeobject((2, 8), villager1)
lvl6.placeobject((5, 9), villager3)
lvl6.placeobject((10, 10), villager4)

lvl1.setexitmatrix(lvl2)
lvl2.setexitmatrix(lvl3)
lvl3.setexitmatrix(lvl4)
lvl4.setexitmatrix(lvl5)
lvl5.setexitmatrix(lvl6)
lvl6.setexitmatrix(lvl7)
lvl7.setexitmatrix(lvl8)



currentLvl = lvl1

def display(current):
    
    print('\n')
    print(colorama.Fore.GREEN + current.getname() + colorama.Style.RESET_ALL)
    outputgrid = ''

    # RECODE THIS WHOLE THING
    for i in range(0, current.getmatrix().size):
        for j in range(0, current.getmatrix().size):
            printedobj = False
            for pos in current.objects:
                if pos[0] == j and pos[1] == i:
                    if isinstance(current.objects[pos], NPC):
                        outputgrid += current.objects[pos].getsymbol() + ' '
                        printedobj = True
                    elif isinstance(current.objects[pos], Item):
                        outputgrid += f'{current.objects[pos].icon} '
                        printedobj = True
                    
            if playerpos.x == j and playerpos.y == i:
                outputgrid += playericon + ' '
            elif i == entranceLocation.y and j == entranceLocation.x:
                outputgrid += '< '
            elif i == current.exitPos.y and j == current.exitPos.x:
                outputgrid += '> '
            else:
                if printedobj:
                    printedobj = False
                else:
                    outputgrid += '. '
        outputgrid += '\n'

    return outputgrid

def display_maze(maze: MazeLevel):
    grid = maze.getmatrix()

    print('\n')
    print(f'>> {maze.getname()} <<')
    outputgrid = ''
    
    for i in range(len(grid)):
        xsize = len(grid[i])
        for j in range(xsize):
            if playerpos.y == i and playerpos.x == j:
                outputgrid += playericon + ' '
            elif i == entranceLocation.y + 1 and j == entranceLocation.x:
                outputgrid += '< '
            elif i == maze.exitPos.y and j == maze.exitPos.x:
                outputgrid += '> '
            else:
                outputgrid += '. ' if grid[i][j] == 0 else f'{wall} '
        outputgrid += '\n'

    return outputgrid


def validate_move(display):
    
    moves = list(input('where to move? ').lower())
    for move in moves:
        valid = validate_movement(display)
        if move == 'w' and valid[0]:
            playerpos.y -= 1
        elif move == 's' and valid[1]:
            playerpos.y += 1
        elif move == 'a' and valid[2]:
            playerpos.x -= 1
        elif move == 'd' and valid[3]:
            playerpos.x += 1
        else:
            pass
    
    xbound = currentLvl.exitPos.getx()
    ybound = currentLvl.exitPos.gety()
    if playerpos.x > xbound:
        playerpos.x = xbound
    if playerpos.y > ybound:
        playerpos.y = ybound
    if playerpos.x < 0:
        playerpos.x = 0
    if playerpos.y < 0:
        playerpos.y = 0

def move():
    moves = list(input('where to move? ').lower())
    for move in moves:
        if move == 'w':
            playerpos.y -= 1
        elif move == 's':
            playerpos.y += 1
        elif move == 'a':
            playerpos.x -= 1
        elif move == 'd':
            playerpos.x += 1
        else:
            pass
    
    xbound = currentLvl.exitPos.getx()
    ybound = currentLvl.exitPos.gety()
    if playerpos.x > xbound:
        playerpos.x = xbound
    if playerpos.y > ybound:
        playerpos.y = ybound
    if playerpos.x < 0:
        playerpos.x = 0
    if playerpos.y < 0:
        playerpos.y = 0


currentLvl.enter()


while stage1:
    printable = ''
    if isinstance(currentLvl, MazeLevel):
        printable = display_maze(currentLvl)
        print(printable)
        validate_move(printable)
    else:
        printable = display(currentLvl)
        print(printable)
        move()
    
    for pos in currentLvl.objects:
        if pos[0] == playerpos.getx() and pos[1] == playerpos.gety():
            if isinstance(currentLvl.objects[pos], NPC):
                currentLvl.objects[pos].gothroughdialogue()
                if currentLvl.objects[pos].name == villager4.name:
                    currentLvl.objects[pos].name =  colorama.Style.DIM + 'suspicious looking man' + colorama.Style.RESET_ALL
                    currentLvl.objects[pos].setdialogue(['Trench coat? I don\'t know what you\'re talking about.'])
                playerpos.y += 1

    if playerpos.x == currentLvl.exitPos.x and playerpos.y == currentLvl.exitPos.y:
        if currentLvl.getexitmatrix() != None:
            currentLvl = currentLvl.getexitmatrix().enter()
            playerpos.x = 1
            playerpos.y = 1
        else:
            if currentLvl.getname() == 'VI':
                stage1 = False

    if playerpos.x == entranceLocation.x and playerpos.y == entranceLocation.y:
        if currentLvl.getstartingmatrix() != None:
            currentLvl = currentLvl.getstartingmatrix().enter()
            playerpos.x = 1
            playerpos.y = 1

print('\n'*10)
GAME_MASTER = NPC(
    purple('Game Master'),
    [
        'OH. IT SEEMS I SEVERLY UNDERESTIMATED YOU.',
        'ANYHOW, IT IS STILL MY GAME AFTER ALL!',
        'I CHOOSE TO END THIS DEBATE VIA THE CLASSIC GAME OF CHANCE.',
        colorama.Fore.RED + 'ROCK' + colorama.Style.RESET_ALL,
        colorama.Fore.RED + 'PAPER' + colorama.Style.RESET_ALL,
        colorama.Fore.RED + 'SCISSORS!' + colorama.Style.RESET_ALL,
        'MAKE YOUR PICK!'
    ]
)

GAME_MASTER.gothroughdialogue()


choice = int(input(f'''
Pick {colorama.Style.BRIGHT + 'ROCK' + colorama.Style.RESET_ALL} {gold('[1]')}
Pick {colorama.Style.BRIGHT + 'PAPER' + colorama.Style.RESET_ALL} {gold('[2]')}
Pick {colorama.Style.BRIGHT + 'SCISSORS' + colorama.Style.RESET_ALL} {gold('[3]')}
'''))

masterchoice = random.choice([1, 2, 3])
win = False
if (choice == 1 and masterchoice == 2) or (choice == 2 and masterchoice == 3) or (choice == 1 and masterchoice == 3):
    win = False
    print('\n'*20)
    dramatic_monologue(0.3, colorama.Style.BRIGHT + '' + colorama.Fore.RED + "YOU LOST . . ." + colorama.Style.RESET_ALL)
    exit()

print('\n'*20)
dramatic_monologue(0.1, colorama.Style.BRIGHT + '' + colorama.Fore.GREEN + "YOU BEAT THE GAME MASTER!" + colorama.Style.RESET_ALL)
dramatic_monologue(0.05, colorama.Style.BRIGHT + "The villagers thank you for your valiance.")
print('You loot the ' + purple('Game Master') + '\'s treasure and go home happily ever after.')
