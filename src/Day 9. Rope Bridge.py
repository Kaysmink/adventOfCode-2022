Input = open("data/dag 9. input.txt", "r").read().split("\n")[:-1]
motions = [line.split() for line in Input]

# Deel 1 
S = [0,0]
H = [0,0]
T = [0,0]
visited = [[0,0]]

def move_head(direction):
    global H
    if direction == "D":
        H[1] = H[1] - 1
    if direction == "U":
        H[1] = H[1] + 1
    if direction == "L":
        H[0] = H[0] - 1
    if direction == "R":
        H[0] = H[0] + 1

        
def check_adjacent():
    neighbors = [[xn, yn] for xn in range(H[0]-1, H[0]+2) for yn in range(H[1]-1, H[1]+2)]
    if T not in neighbors:
        move_tail()


def move_tail():
    global H
    global T
    possible_positions = [[xn, yn] for xn in range(H[0]-1, H[0]+2) for yn in range(H[1]-1, H[1]+2) if (xn == H[0] or yn == H[1])]
    neigbors_tail = [[xn, yn] for xn in range(T[0]-1, T[0]+2) for yn in range(T[1]-1, T[1]+2)]
    
    new_position = neigbors_tail[[value in possible_positions for value in neigbors_tail].index(True)]
    T = new_position
    
    if T not in visited:
        visited.append(T)
    pass


        
for direction, steps in motions:
    for step in range(int(steps)):
        move_head(direction)
        check_adjacent()

print(len(visited))

##############################################################################
# Deel 2
positions = [[0,0] for value in range(10)]
visited_2 = [[0,0]]

def move_head_2(direction):
    global positions
    if direction == "D":
        positions[0][1] = positions[0][1] - 1
    if direction == "U":
        positions[0][1] = positions[0][1] + 1
    if direction == "L":
        positions[0][0] = positions[0][0] - 1
    if direction == "R":
        positions[0][0] = positions[0][0] + 1


def check_if_move():
    for idx in range(1,10):
        if not check_adjacent_2(idx-1, idx):
            move_idx(idx)
        else:
            break

    
def check_adjacent_2(idx1, idx2):
    neighbors = [[xn, yn] for xn in range(positions[idx1][0]-1, positions[idx1][0]+2) for yn in range(positions[idx1][1]-1, positions[idx1][1]+2)]
    return positions[idx2] in neighbors


def move_idx(idx):
    global positions
    possible_positions = [[xn, yn] for xn in range(positions[idx-1][0]-1, positions[idx-1][0]+2) for yn in range(positions[idx-1][1]-1, positions[idx-1][1]+2)]
    
    if positions[idx-1][0] == positions[idx][0]:
        possible_positions = [[xn, yn] for xn, yn in possible_positions if xn == positions[idx-1][0]]
        
    elif positions[idx-1][1] == positions[idx][1]:
        possible_positions = [[xn, yn] for xn, yn in possible_positions if yn == positions[idx-1][1]]
        
    else:
        possible_positions = [[xn, yn] for xn, yn in possible_positions if yn != positions[idx][1] and xn != positions[idx][0]]
        
    neigbors_idx = [[xn, yn] for xn in range(positions[idx][0]-1, positions[idx][0]+2) for yn in range(positions[idx][1]-1, positions[idx][1]+2)]
    
    new_position = neigbors_idx[[value in possible_positions for value in neigbors_idx].index(True)]
    positions[idx] = new_position
    
    if idx == 9 and new_position not in visited_2:
        visited_2.append(new_position)


for direction, steps in motions:
    for step in range(int(steps)):
        move_head_2(direction)
        check_if_move()
        

print(len(visited_2))
