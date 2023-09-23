import math

from flask import Blueprint, render_template, session, jsonify, request, make_response

minichess = Blueprint("minichess", __name__)

WHITE = True
BLACK = False

def get_moves_bishop(grid, r, c, player):
    moves = []

    for i in range(1, 5):
        new_row = r - i
        new_col = c - i
        if new_row < 0 or new_col < 0:
            break
        if grid[new_row][new_col] != None and grid[new_row][new_col].player == player:
            break
        else:
            moves.append(((r, c), (new_row, new_col)))
            if grid[new_row][new_col] != None and grid[new_row][new_col].player != player:
                break

    for i in range(1, 5):
        new_row = r + i
        new_col = c + i
        if new_row >= 5 or new_col >= 5:
            break
        if grid[new_row][new_col] != None and grid[new_row][new_col].player == player:
            break
        else:
            moves.append(((r, c), (new_row, new_col)))
            if grid[new_row][new_col] != None and grid[new_row][new_col].player != player:
                break

    for i in range(1, 5):
        new_row = r + i
        new_col = c - i
        if new_row >= 5 or new_col < 0:
            break
        if grid[new_row][new_col] != None and grid[new_row][new_col].player == player:
            break
        else:
            moves.append(((r, c), (new_row, new_col)))
            if grid[new_row][new_col] != None and grid[new_row][new_col].player != player:
                break

    for i in range(1, 5):
        new_row = r - i
        new_col = c + i
        if new_row < 0 or new_col >= 5:
            break
        if grid[new_row][new_col] != None and grid[new_row][new_col].player == player:
            break
        else:
            moves.append(((r, c), (new_row, new_col)))
            if grid[new_row][new_col] != None and grid[new_row][new_col].player != player:
                break

    return moves

def get_moves_rook(grid, r, c, player):
    moves = []

    for i in range(1, 5):
        new_row = r + i
        new_col = c
        if new_row >= 5:
            break

        if grid[new_row][new_col] != None and grid[new_row][new_col].player == player:
            break
        else:
            moves.append(((r, c), (new_row, new_col)))
            if grid[new_row][new_col] != None and grid[new_row][new_col].player != player:
                break

    for i in range(1, 5):
        new_row = r - i
        new_col = c
        if new_row < 0:
            break
        if grid[new_row][new_col] != None and grid[new_row][new_col].player == player:
            break
        else:
            moves.append(((r, c), (new_row, new_col)))
            if grid[new_row][new_col] != None and grid[new_row][new_col].player != player:
                break

    for i in range(1, 5):
        new_row = r
        new_col = c - i
        if new_col < 0:
            break
        if grid[new_row][new_col] != None and grid[new_row][new_col].player == player:
            break
        else:
            moves.append(((r, c), (new_row, new_col)))
            if grid[new_row][new_col] != None and grid[new_row][new_col].player != player:
                break

    for i in range(1, 5):
        new_row = r
        new_col = c + i
        if new_col >= 5:
            break
        if grid[new_row][new_col] != None and grid[new_row][new_col].player == player:
            break
        else:
            moves.append(((r, c), (new_row, new_col)))
            if grid[new_row][new_col] != None and grid[new_row][new_col].player != player:
                break

    return moves

def get_moves_knight(grid, r, c, player):
    moves = []

    new_row = r+1
    new_col = c-2
    if new_row < 5 and new_col >= 0:
        if grid[new_row][new_col] == None or grid[new_row][new_col].player != player:
            moves.append(((r, c), (new_row, new_col)))
    new_row = r+2
    new_col = c-1
    if new_row < 5 and new_col >= 0:
        if grid[new_row][new_col] == None or grid[new_row][new_col].player != player:
            moves.append(((r, c), (new_row, new_col)))

    new_row = r+1
    new_col = c+2
    if new_row < 5 and new_col < 5:
        if grid[new_row][new_col] == None or grid[new_row][new_col].player != player:
            moves.append(((r, c), (new_row, new_col)))
    new_row = r+2
    new_col = c+1
    if new_row < 5 and new_col < 5:
        if grid[new_row][new_col] == None or grid[new_row][new_col].player != player:
            moves.append(((r, c), (new_row, new_col)))

    new_row = r-1
    new_col = c-2
    if new_row >= 0 and new_col >= 0:
        if grid[new_row][new_col] == None or grid[new_row][new_col].player != player:
            moves.append(((r, c), (new_row, new_col)))
    new_row = r-2
    new_col = c-1
    if new_row >= 0 and new_col >= 0:
        if grid[new_row][new_col] == None or grid[new_row][new_col].player != player:
            moves.append(((r, c), (new_row, new_col)))

    new_row = r-2
    new_col = c+1
    if new_row >= 0 and new_col < 5:
        if grid[new_row][new_col] == None or grid[new_row][new_col].player != player:
            moves.append(((r, c), (new_row, new_col)))
    new_row = r-1
    new_col = c+2
    if new_row >= 0 and new_col < 5:
        if grid[new_row][new_col] == None or grid[new_row][new_col].player != player:
            moves.append(((r, c), (new_row, new_col)))

    return moves

def get_moves_king(grid, r, c, player):
    moves = []

    new_col = c-1
    if new_col >= 0:
        for nr in range(-1, 2):
            new_row = nr + r
            if new_row >= 0 and new_row < 5:
                if grid[new_row][new_col] == None or grid[new_row][new_col].player != player:
                    moves.append(((r, c), (new_row, new_col)))

    new_col = c+1
    if new_col < 5:
        for nr in range(-1, 2):
            new_row = nr + r
            if new_row >= 0 and new_row < 5:
                if grid[new_row][new_col] == None or grid[new_row][new_col].player != player:
                    moves.append(((r, c), (new_row, new_col)))

    new_row = r-1
    if new_row >= 0:
        if grid[new_row][c] == None or grid[new_row][c].player != player:
            moves.append(((r, c), (new_row, c)))

    new_row = r+1
    if new_row < 5:
        if grid[new_row][c] == None or grid[new_row][c].player != player:
            moves.append(((r, c), (new_row, c)))

    return moves

def get_moves_pawn(grid, r, c, player):
    moves = []

    if player == 'White':
        new_row = r+1
    else:
        new_row = r-1

    if new_row < 5 and new_row >= 0:
        if grid[new_row][c] == None:
            moves.append(((r, c), (new_row, c)))

        if c-1 >= 0:
            if grid[new_row][c-1] != None and grid[new_row][c-1].player != player:
                moves.append(((r, c), (new_row, c-1)))

        c+1
        if c+1 < 5:
            if grid[new_row][c+1] != None and grid[new_row][c+1].player != player:
                moves.append(((r, c), (new_row, c+1)))

    return moves

def to_piece(grid, piece):
    piece_type = piece[0]
    player = piece[1]
    if piece_type == 'King':
        return King(grid, player)
    elif piece_type == 'Pawn':
        return Pawn(grid, player)
    elif piece_type == 'Rook':
        return Rook(grid, player)
    elif piece_type == 'Bishop':
        return Bishop(grid, player)
    elif piece_type == 'Queen':
        return Queen(grid, player)
    elif piece_type == 'Knight':
        return Knight(grid, player)
    elif piece_type == 'Ferz':
        return Ferz(grid, player)
    elif piece_type == 'Princess':
        return Princess(grid, player)
    elif piece_type == 'Empress':
        return Empress(grid, player)

class Pawn:
    def __init__(self, grid, player):
        self.value = 1
        self.player = player
        self.grid = grid

    def actions(self, r, c):
        return get_moves_pawn(self.grid, r, c, self.player)

class King:
    def __init__(self, grid, player):
        self.value = 200
        self.player = player
        self.grid = grid

    def actions(self, r, c):
        return get_moves_king(self.grid, r, c, self.player)

class Rook:
    def __init__(self, grid, player):
        self.value = 5
        self.player = player
        self.grid = grid

    def actions(self, r, c):
        return get_moves_rook(self.grid, r, c, self.player)

class Bishop:
    def __init__(self, grid, player):
        self.value = 3
        self.player = player
        self.grid = grid

    def actions(self, r, c):
        return get_moves_bishop(self.grid, r, c, self.player)

class Knight:
    def __init__(self, grid, player):
        self.value = 3
        self.player = player
        self.grid = grid

    def actions(self, r, c):
        return get_moves_knight(self.grid, r, c, self.player)

class Queen:
    def __init__(self, grid, player):
        self.value = 9
        self.player = player
        self.grid = grid

    def actions(self, r, c):
        return get_moves_bishop(self.grid, r, c, self.player) + get_moves_rook(self.grid, r, c, self.player)

class Board:
    def __init__(self, pieces):
        self.grid = [[None for j in range(5)] for i in range(5)]
        self.w_king = None
        self.b_king = None
        self.pieces = {}

        for coord in pieces:
            piece = pieces[coord]
            parsed_piece = to_piece(self.grid, piece)

            if piece[0] == "King" and piece[1] == "White":
                self.w_king = parsed_piece
            elif piece[0] == "King":
                self.b_king = parsed_piece

            self.grid[coord[0]][coord[1]] = parsed_piece
            self.pieces[coord] = parsed_piece

    def get_value(self):
        value = 0
        for coord in self.pieces:
            if self.pieces[coord].player == 'White':
                value += self.pieces[coord].value
            else:
                value -= self.pieces[coord].value

        return value

    def get_actions(self, turn):
        moves = []
        if turn == WHITE:
            for coord in self.pieces:
                piece = self.pieces[coord]
                if piece.player == 'White':
                    moves += piece.actions(coord[0], coord[1])
        else:
            for coord in self.pieces:
                piece = self.pieces[coord]
                if piece.player == 'Black':
                    moves += piece.actions(coord[0], coord[1])
        return moves

def ab(gameboard):
    state = Board(gameboard)
    return minimax(state)
def minimax(state):
    value, move = minimax_util(state, WHITE, -99999, 99999, 3)
    print(value)
    return move

def minimax_util(state, turn, alpha, beta, depth):
    if depth == 0 or state.w_king not in state.pieces.values() or state.b_king not in state.pieces.values() or state.w_king == None or state.b_king == None:
        return (state.get_value(), None)

    if turn:
        best_score = -99999
        best_move = None
        for action in state.get_actions(turn):
            from_coord = action[0]
            to_coord = action[1]

            piece = state.grid[from_coord[0]][from_coord[1]]
            old = state.grid[to_coord[0]][to_coord[1]]

            if old != None:
                del state.pieces[to_coord]

            state.grid[to_coord[0]][to_coord[1]] = piece
            state.grid[from_coord[0]][from_coord[1]] = None
            del state.pieces[from_coord]
            state.pieces[to_coord] = piece

            action_util, _ = minimax_util(
                state, not turn, alpha, beta, depth - 1)

            if action_util > best_score:
                best_score = action_util
                best_move = action
                alpha = max(alpha, best_score)

            state.grid[to_coord[0]][to_coord[1]] = old
            state.grid[from_coord[0]][from_coord[1]] = piece
            del state.pieces[to_coord]
            state.pieces[from_coord] = piece
            if old != None:
                state.pieces[to_coord] = old

            if alpha >= beta:
                return (best_score, best_move)
        return (best_score, best_move)
    else:
        best_score = 99999
        best_move = None
        for action in state.get_actions(turn):
            from_coord = action[0]
            to_coord = action[1]

            piece = state.grid[from_coord[0]][from_coord[1]]
            old = state.grid[to_coord[0]][to_coord[1]]

            if old != None:
                del state.pieces[to_coord]

            state.grid[to_coord[0]][to_coord[1]] = piece
            state.grid[from_coord[0]][from_coord[1]] = None
            del state.pieces[from_coord]
            state.pieces[to_coord] = piece

            action_util, _ = minimax_util(
                state, not turn, alpha, beta, depth - 1)

            if action_util < best_score:
                best_score = action_util
                best_move = action
                beta = min(beta, best_score)

            state.grid[to_coord[0]][to_coord[1]] = old
            state.grid[from_coord[0]][from_coord[1]] = piece
            del state.pieces[to_coord]
            state.pieces[from_coord] = piece
            if old != None:
                state.pieces[to_coord] = old

            if alpha >= beta:
                return (best_score, best_move)
        return (best_score, best_move)

piecemap = {
    "\u2659": ("Pawn", "White"),
    "\u265F": ("Pawn", "Black"),
    "\u2656": ("Rook", "White"),
    "\u265C": ("Rook", "Black"),
    "\u2658": ("Knight", "White"),
    "\u265E": ("Knight", "Black"),
    "\u2657": ("Bishop", "White"),
    "\u265D": ("Bishop", "Black"),
    "\u2655": ("Queen", "White"),
    "\u265B": ("Queen", "Black"),
    "\u2654": ("King", "White"),
    "\u265A": ("King", "Black"),
}

def parse(testcase):

    rows = 5
    cols = 5
    gameboard = {}

    for r in range(5):
        for c in range(5):
            data = testcase[r][c]
            a = data.split("|")
            r = a[1]
            c = a[2]
            piece = piecemap[a[0]]
            gameboard[(c,r)] = piece

    return rows, cols, gameboard
def add_piece(comma_seperated):
    piece, ch_coord = comma_seperated.split(",")
    r, c = ch_coord
    return [(r, c), piece]
def studentAgent(testcase):
    gameboard = {}

    for r in range(5):
        for c in range(5):
            data = testcase[r][c]
            if data == "":
                continue
            a = data.split("|")
            piece = piecemap[a[0]]
            gameboard[(int(a[1]),int(a[2]))] = piece
            # print((int(a[1]),int(a[2])), piece)

    move = ab(gameboard)

    from_coord = move[0]
    to_coord = move[1]

    res = {
        "move": [from_coord[0], from_coord[1], to_coord[0], to_coord[1]]
    }

    return res

@minichess.route("/minichess", methods=["POST"])
def getCommon():
    board = request.json["board"]
    return jsonify(studentAgent(board))


# print(studentAgent([
#         ["♜|0|0", "♞|0|1", "♝|0|2", "♛|0|3", "♚|0|4"],
#         ["♟|1|0", "♟|1|1", "♟|1|2", "♟|1|3", "♟|1|4"],
#         ["", "", "", "", ""],
#         ["♙|3|0", "♙|3|1", "♙|3|2", "♙|3|3", "♙|3|4"],
#         ["♖|4|0", "♘|4|1", "♗|4|2", "♕|4|3", "♔|4|4"]
#     ]))