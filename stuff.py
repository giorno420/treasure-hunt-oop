import time
from random import shuffle, randrange
import colorama

colorama.init()

wall = 'Ꚛ'
walkable = ['.', '<', '>']
playericon = colorama.Fore.GREEN + 'X' + colorama.Style.RESET_ALL

def delete_line(lines):
    for i in range(lines):
        print("\033[F\033[K", end="")


def dramatic_monologue(sleeptime, text):
    for x in list(text):
        time.sleep(sleeptime)
        print(x, end='', flush=True)
    print()

'''position on the grid'''
class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def equals(self, other):
        return other.x == self.x and other.y == self.y

    def output(self):
        print(f'Pos({self.x}, {self.y})')

    def getx(self):
        return self.x
    
    def gety(self):
        return self.y

playerpos = Pos(1, 1)
entranceLocation = Pos(0, 0)

class SquareMatrix:
    def __init__(self, size):
        self.objects = {}
        self.matrix = []
        self.size = size
        for i in range(0, size):
            self.matrix.append([[] for j in range(0, size)])
    
    def get_on_pos(self, pos: Pos):
        return self.matrix[pos.y][pos.x]
    
    def set_on_pos(self, pos: Pos, data: str):
        self.matrix[pos.y][pos.x] = [data]

    def get_size(self):
        return self.size


def create_maze(w = 9, h = 8):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["| "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+-"] * w + ['+'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+ "
            if yy == y: ver[y][max(x, xx)] = "  "
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    
    s = s.replace('+', wall).replace('-', wall).replace('|', wall)
    grid = []
    i = 0
    for line in s.split('\n'):
        grid.append([]) if line != '' else ...
        for char in line:
            grid[i].append(1 if char == wall else 0)
        i += 1

    return grid

def validate_movement(grid):
    grid = grid.replace(' ', '').replace(playericon, 'X')
    for whitelist in walkable:
        grid = grid.replace(whitelist, '0')
    grid = grid.replace(wall, '1')
    rows = grid.split('\n')

    def up(x, y):
        try:
            return not rows[y-1][x] == '1'
        except IndexError:
            return False
    def down(x, y):
        try:
            return not rows[y+1][x] == '1'
        except IndexError:
            return False
    def left(x, y):
        try:
            return not rows[y][x-1] == '1'
        except IndexError:
            return False
    def right(x, y):
        try:
            return not rows[y][x+1] == '1'
        except IndexError:
            return False

    return [
        up(playerpos.getx(), playerpos.gety()), 
        down(playerpos.getx(), playerpos.gety()), 
        left(playerpos.getx(), playerpos.gety()), 
        right(playerpos.getx(), playerpos.gety())
    ]


class Level:
    def __init__(
            self, 
            name: str,
            exitPos: Pos = None,
            exitMatrix = None,
            startingMatrix = None,
            size = 16,
            message = '',
            objects = {}
        ):
        self._name = name
        self._size = size
        self.exitPos = exitPos
        self._matrix = SquareMatrix(self._size)
        self.exitMatrix = exitMatrix
        self.startingMatrix = startingMatrix
        self.message = message
        self.objects = objects
    
    def getname(self):
        return self._name

    def getexitmatrix(self):
        return self.exitMatrix
    
    def setexitmatrix(self, mat):
        self.exitMatrix = mat
    
    def getstartingmatrix(self):
        return self.startingMatrix
    
    def setstartingmatrix(self, mat):
        self.startingMatrix = mat
    
    def getmatrix(self):
        return self._matrix
    
    def getsize(self):
        return self._size
    
    def placeobject(self, pos, object):
        self.objects[pos] = object

    def getobjectatxy(self, x: int, y: int):
        for pos in self.objects:
            if pos[0] == x and pos[1] == y:
                return self.objects[pos]
        return None
    
    def enter(self):
        print('\n\n', flush=True)
        dramatic_monologue(0.07, self.message)
        return self



class MazeLevel(Level):
    def __init__(
            self, 
            name: str,
            exitPos: Pos = None,
            exitMatrix: Level = None,
            length: int = 9,
            width: int = 8,
            message = '',
            objects = {}
    ):
        super().__init__(name, exitMatrix, message=message, objects=objects)
        self.exitPos = exitPos
        self._matrix = create_maze(length, width)
    
    def setexitpos(self, pos):
        self.exitPos = pos
    
    def enter(self):
        self.exitPos = Pos(len(self.getmatrix()[0])-1, len(self.getmatrix())-2)
        print('\n\n')
        dramatic_monologue(0.07, self.message)
        return self
        

        
class NPC:
    def __init__(self, name, dialogue=[]):
        self.name = name
        self.dialogue = dialogue
    
    def setdialogue(self, dialogue: list):
        self.dialogue = dialogue

    def addtodialogue(self, line: str):
        self.dialogue.append(line)

    def getsymbol(self):
        return colorama.Fore.CYAN + 'o' + colorama.Style.RESET_ALL

    def gothroughdialogue(self):
        for x in self.dialogue:
            print(f'{self.name} >', end=' ', flush=True)
            sentence = list(x)
            for char in sentence:
                time.sleep(0.03)
                print(char, end='', flush=True)
                
            print()
            input('press [enter] to continue')
            delete_line(2)


def purple(text: str):
    return colorama.Fore.MAGENTA + text + colorama.Style.RESET_ALL

def gold(text: str):
    return colorama.Fore.YELLOW + text + colorama.Style.RESET_ALL
