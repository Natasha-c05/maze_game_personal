def Maze():
    return [
        list("##########"),
        list("#P       #"),
        list("# ###### #"),
        list("# ######E#"),
        list("# ###### #"),
        list("#        #"),
        list("# ###### #"),
        list("##########")
    ]

def print_maze(maze):
    for row in maze:
        print("".join(row))

def wall(maze, new_row, new_col, player_row, player_col):
    if maze[new_row][new_col]=="#":
        print("you hit a wall")
        return player_row, player_col


def move(maze, player_row, player_col):
    user_input=input("Move(U/D/L/R): ").lower()

    new_row = player_row
    new_col= player_col

    while wall(maze, new_row, new_col, player_row, player_col):
        user_input=input("Move(U/D/L/R): ").lower()
        

    
    if user_input == "u":
        new_row-=1
    elif user_input=="d":
        new_row+=1
    elif user_input=="l":
        new_col-=1
    elif user_input=="r":
        new_col+=1
    
    if not wall(maze, new_row, new_col, player_row, player_col):
        maze[player_row][player_col]=" "
        if maze[new_row][new_col]!="E":
            maze[new_row][new_col]="p"
            return new_row, new_col
    
    return player_row, player_col
    


def win(maze,player_row, player_col):
    if maze[player_row][player_col] == "E":
        return True
    return False
        

def maze_game_initializer():
    maze=Maze()
    player_row, player_col = 1,1

    while True:

        print_maze(maze)

        if win(maze,player_row, player_col):
            print("you win")
            break
        player_row, player_col = move(maze, player_row, player_col)
        
        

        


maze_game_initializer()
