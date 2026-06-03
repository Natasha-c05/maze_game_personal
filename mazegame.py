def Maze():
    maze=[
        list("##########"),
        list("#P       #"),
        list("# ###### #"),
        list("# ######E#"),
        list("# ###### #"),
        list("#        #"),
        list("# ###### #"),
        list("##########")
    ]
    return 

def player_position():

    #starting position
    player_row=1
    player_col=1

def wall(Maze, player_position):
    player_row=player_row
    player_col=player_col

    if maze[player_row][player_col]=="#":
        print("you hit a wall")
        return True


def move(player_position):
    user_input=input("Move(U/D/L/R): ")
    if user_input == "U":
        if player_row>1:
            player_row -=1
        else:
            print("out of bound, there is a wall")
        

print(Maze())

