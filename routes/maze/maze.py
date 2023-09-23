
from flask import Blueprint, render_template, session, jsonify, request, make_response

maze = Blueprint("maze", __name__)

class MazeSolver:
    def __init__(self, id):
        self.maze = {}
        self.maze[(0,0)] = 0
        self.id = id
        self.current_position = (0,0)
        self.backtrack = []

    def find_direction(self, nearby):
        # Define the directions for moving up, down, left, and right
        directions = [(0, -1, "up"), (0, 1, "down"), (-1, 0, "left"), (1, 0, "right")]

        cx = 1
        cy = 1

        bestMove = "respawn"
        for dx, dy, direction in directions:
            x, y = self.current_position[0] + dx, self.current_position[1] + dy

            if nearby[cy + dy][cx + dx] == 0:
                continue

            if nearby[cy + dy][cx + dx] == 3:
                bestMove = direction
                break

            if (x,y) in self.maze:
                continue
            
            bestMove = direction

        if bestMove == "respawn" and len(self.backtrack) > 0:
            bestMove = self.backtrack.pop()
            if bestMove == "up":
                self.current_position = (self.current_position[0], self.current_position[1] + 1)
            elif bestMove == "down":
                self.current_position = (self.current_position[0], self.current_position[1] - 1)
            elif bestMove == "left":
                self.current_position = (self.current_position[0] - 1, self.current_position[1])
            elif bestMove == "right":
                self.current_position = (self.current_position[0] + 1, self.current_position[1])
            return bestMove
        

        if bestMove == "up":
            self.current_position = (self.current_position[0], self.current_position[1] - 1)
            self.maze[self.current_position] = 1
            self.backtrack.append("down")
        elif bestMove == "down":
            self.current_position = (self.current_position[0], self.current_position[1] + 1)
            self.maze[self.current_position] = 1
            self.backtrack.append("up")
        elif bestMove == "left":
            self.current_position = (self.current_position[0] - 1, self.current_position[1])
            self.maze[self.current_position] = 1
            self.backtrack.append("right")
        elif bestMove == "right":
            self.current_position = (self.current_position[0] + 1, self.current_position[1])
            self.maze[self.current_position] = 1
            self.backtrack.append("left")
        return bestMove

solver = MazeSolver("a")

@maze.route("/maze", methods=["POST"])
def getCommon():
    global solver

    mazeId = request.json["mazeId"]
    nearby = request.json["nearby"]
    mazeWidth = request.json["mazeWidth"]
    step = request.json["step"]
    isPreviousMovementValid = request.json["isPreviousMovementValid"]
    message = request.json["message"]
    if mazeId != solver.id:
        solver = MazeSolver(mazeId)
    
    res = {"playerAction": solver.find_direction(nearby)}
    return jsonify(res)


# # Example usage:
# solver = MazeSolver("asd")

# # Update the maze state with the first nearby matrix
# nearby1 = [
#     [0, 0, 0],
#     [0, 2, 1],
#     [0, 0, 1]
# ]

# # Find the first direction to move
# direction1 = solver.find_direction(nearby1)
# print(direction1)  # Output: "down"

# # Update the maze state with the second nearby matrix
# nearby2 = [
#     [0, 0, 0],
#     [2, 1, 0],
#     [0, 1, 0]
# ]

# # Find the second direction to move
# direction2 = solver.find_direction(nearby2)
# print(direction2)  # Output: "left"

# # Update the maze state with the second nearby matrix
# nearby3 = [
#     [2, 1, 0],
#     [0, 1, 0],
#     [3, 1, 1],
# ]

# # Find the second direction to move
# direction3 = solver.find_direction(nearby3)
# print(direction3)  # Output: "left"

# # Update the maze state with the second nearby matrix
# nearby4 = [
#     [0, 1, 0],
#     [3, 1, 1],
#     [0, 1, 0],
# ]

# # Find the second direction to move
# direction4 = solver.find_direction(nearby4)
# print(direction4)  # Output: "left"
