grid = [['x', 'o', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

class Tictactoe:
    def __init__(self, grid=None):
        if not grid:
            grid = [[' ']*3 for _ in range(3)]
        self.grid = grid
        self.children = []
        
    def __str__(self):
        rows = [' │ '.join(i) for i in self.grid]
        return '\n──┼───┼───\n'.join(rows)

    def __repr__(self):
        rows = [' │ '.join(i) for i in self.grid]
        return '\n──┼───┼───\n'.join(rows)

    
    def next_player(self):
        count = sum([row.count(' ') for row in self.grid])
        if count == 0:
            return None
        elif count % 2 == 0:
            return 'x'
        return 'o'
        
    def emtpy_cells(self):
        cells = [(r, c) for r, row in enumerate(self.grid)
                 for c, cell in enumerate(row)
                 if self.grid[r][c] == ' '
                ]
        return cells
    
    def has_won(self, player):
        [[A,B,C],
         [D,E,F],
         [G,H,I]] = self.grid
        return (A == B == C == player or
            D == E == F == player or
            G == H == I == player or
            A == D == G == player or
            B == E == H == player or
            C == F == I == player or
            A == E == I == player or
            G == E == C == player)
    
    
    
    def winner(self):
        if self.has_won('x'):
            return 'x'
        if self.has_won('o'):
            return 'o'
        return None
    
    
    def evaluate_game(self):
        ''' returns a tuple X, D, O where X is the number of
            times X wins, O is when o wins and D are the games ending
            with a draw'''
        win = {'x':(1,0,0), 'o':(0,0,1)}
        w = self.winner()
        if w:
            return win[w]
        moves = self.emtpy_cells()
        if not moves:
            return (0,1,0)
        player = self.next_player()
        X = D = O = 0
        self.children = []
        for r, c in moves:
            new_grid = [row.copy() for row in self.grid]
            new_grid[r][c] = player
            child = Tictactoe(new_grid)
            self.children.append(child)
            x, d, o = child.evaluate_game()
            X += x
            D += d
            O += o
        return X, D, O