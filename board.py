import random


class Board(object):

    def __init__(self, dim):
        """Creates a board. Takes one arguement dim = X. """
        self.dim = dim
        self.cells = set()

    def add_cell(self,  pos):
        """Adds an alive cell at the defined position. Takes one argument pos=(x,y)"""
        self.cells.add(pos)

    def insert_random_cells(self, n):
        """Adds n alive cells at random positions. Takes one argument n=number of cells to insert."""
        for cell in range(n):
            x = random.randint(0, self.dim)
            y = random.randint(0, self.dim)
            self.add_cell(pos=(x,y))

    def insert_blinker(self):
        """Inserts a Blinker figure to the board at a random position"""
        x = random.randint(1, self.dim-1)
        y = random.randint(0, self.dim - 3)
        self.add_cell(pos=(x,y))
        self.add_cell(pos=(x,y+1))
        self.add_cell(pos=(x,y+2))

    def insert_toad(self):
        """Inserts a Toad figure to the board at a random position"""
        x = random.randint(1, self.dim - 2)
        y = random.randint(1, self.dim - 3)
        self.add_cell(pos=(x,y))
        self.add_cell(pos=(x+1,y))
        self.add_cell(pos=(x+2,y))
        self.add_cell(pos=(x+1,y+1))
        self.add_cell(pos=(x+2,y+1))
        self.add_cell(pos=(x+3,y+1))

    def is_alive(self, pos):
        return pos in self.cells

    def neighbours(self, pos):
        #Returns neighbour locations for a provided position
        neighbours = set()
        if pos[0] < self.dim and pos[1] < self.dim:
            neighbours.add((pos[0]+1,pos[1]+1))
            neighbours.add((pos[0],pos[1]+1))
            neighbours.add((pos[0]+1,pos[1]))
        if pos[0] > 0:
            neighbours.add((pos[0]-1,pos[1]))
            if pos[1] < self.dim:
                neighbours.add((pos[0]-1,pos[1]+1))
        if pos[1] > 0:
            neighbours.add((pos[0],pos[1]-1))
            if pos[0] < self.dim:
                neighbours.add((pos[0]+1,pos[1]-1))
        if pos[0] > 0 and pos[1] > 0:
            neighbours.add((pos[0]-1,pos[1]-1))
        return neighbours

    def pos_to_analize(self):
        #Tell me what positions are worth analysing, namely the neighbours of the alive cells.
        to_analize = set(self.cells)
        for pos in self.cells:
            neighbour_positions = self.neighbours(pos=pos)
            to_analize = set().union(to_analize, neighbour_positions)
        return to_analize

    def are_neighbours(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) <= 1 and abs(pos1[1] - pos2[1]) <= 1 and pos1 != pos2

    def neighbours_alive(self, pos1):
        res = list()
        for pos in self.cells:
            #Return those that are neighbours from the alive cells
            if self.are_neighbours(pos1, pos):
                res.append(pos)
        return res

    def next(self):
        """Moves one period in time to the next generation of cells. Takes no arguements."""
        newCells = set()
        #For each position toanalize, check how many are alive. and Add them to new cells.
        for pos in self.pos_to_analize():
            n = len(self.neighbours_alive(pos))
            if (self.is_alive(pos)):
                #If it is alive and has 2 or 3 alive neighbours, it lives another day.
                if (n == 2 or n == 3):
                    newCells.add(pos)
            else:
                #If it was dead and has 3 alive neighbours, life is created!
                if n == 3:
                    newCells.add(pos)
        self.cells = newCells

    def show(self):
        """Shows the board with living cells marked with an 'X'."""
        for y in range(self.dim):
            print ''.join('X|' if (x,y) in self.cells
                     else ' |' for x in range(self.dim))
        print

    def __str__(self):
        text = "These are the current alive cells in the system: " + ", ".join(str(cell) for cell in self.cells)
        return str(text)
