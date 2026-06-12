import random
def Maze():
    return [
        list("##########"),
        list("#P       #"),
        list("# ##T### #"),
        list("# ######E#"),
        list("# T##### #"),
        list("#        #"),
        list("#K#####T #"),
        list("##########")
    ]

def print_maze(maze):
    for row in maze:
        print("".join(row))

def wall(maze, new_row, new_col):
    if maze[new_row][new_col]=="#":
        print("you hit a wall")
        return True
    return False

def move(maze, player_row, player_col, move_count,life_count):
    while True:
        user_input=input("Move(U/D/L/R): ").lower()

        new_row = player_row
        new_col= player_col
        
        if user_input == "u":
            move_count-=1
            new_row-=1
        elif user_input=="d":
            move_count-=1
            new_row+=1
        elif user_input=="l":
            move_count-=1
            new_col-=1
        elif user_input=="r":
            move_count-=1
            new_col+=1
        
        print(f"move's left= {move_count}") 
        
        if not wall(maze, new_row, new_col):
            maze[player_row][player_col]=" "
            if maze[new_row][new_col]!="E":
                if maze[new_row][new_col]!="T":
                    if maze[new_row][new_col]!="K":
                        if maze[new_row][new_col]!="M":
                            maze[new_row][new_col]="p"
                            player_row=new_row
                            player_col=new_col
                            return player_row, player_col, move_count,life_count

            if maze[new_row][new_col]=="T":
                life_count-=1
                print(f"Its a trap!, life remaining= {life_count}")
                maze[player_row][player_col]="P"
                return player_row,player_col,move_count,life_count 
            
            if maze[new_row][new_col]=="K":
                player_row= new_row
                player_col= new_col
                return player_row,player_col,move_count,life_count


            if maze[new_row][new_col]=="E":
                player_row=new_row
                player_col=new_col
                return player_row, player_col, move_count,life_count
            
            if maze[new_row][new_col]=="M":
                life_count=0
                return player_row, player_col, move_count,life_count
                    
def key(maze,player_row,player_col):
    if maze[player_row][player_col]=="K":
        return "complete"
    return None


def win(maze,player_row, player_col,mission):
    if maze[player_row][player_col] == "E" and mission!="complete":
        print("You need a key to exit")
        return False
    if mission == "complete" and maze[player_row][player_col] == "E":
        return True
    return False
        
        
def lose(maze,move_count, life_count):
    if move_count==0:
        return True
    if life_count==0:
        return True
    return False

def enemy(maze, enemy_row, enemy_col):  
    if enemy_row is not None and enemy_col is not None:
        maze[enemy_row][enemy_col] = " "
    
    while True:
        random_row= random.randint(2,5)
        random_col=random.randint(2,8)
        if maze[random_row][random_col]==" ":
            maze[random_row][random_col]="M"
            return random_row, random_col


def maze_game_initializer():
    maze=Maze()
    player_row, player_col = 1,1
    move_count=17
    life_count=4
    mission="incomplete"
    enemy_row=None
    enemy_col=None
    move_counter=0

    while True:
        print_maze(maze)
        player_row, player_col,move_count,life_count = move(maze, player_row, player_col,move_count,life_count)
        
        move_counter += 1

        if move_counter % 2 == 0:
            enemy_row, enemy_col = enemy(maze, enemy_row, enemy_col)

        print(life_count)

        if lose(maze, move_count, life_count):
            print("You lose")
            break


        result=key(maze,player_row, player_col)

        if result:
            mission = result
        
        if mission == "complete":
            print("you got a key")

        

        if win(maze,player_row,player_col,mission):
            print("you win")
            break
        

maze_game_initializer()



