input = open("11/input.txt", "r").read()

# input = """
# L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL
# """

seats = input.strip().split("\n")

def count_adjecent(seats, x: int, y: int, seat) -> int:
    posses = [(x-1,y), (x-1, y-1), (x, y-1), (x+1,y-1), (x+1,y), (x+1,y+1), (x,y+1), (x-1,y+1)]
    count = 0
    for pos in posses:
        xp = pos[0]
        yp = pos[1]
        if yp >= 0 and yp < len(seats) and \
            xp >= 0 and xp < len(seats[yp]) and \
            seats[yp][xp] == seat:
            count += 1
    return count

def set_seat(seats, x: int, y: int, seat):
    seats[y] = seats[y][:x] + seat + seats[y][x+1:]

def update_seats(source_seats, target_seats, x: int, y: int) -> int:
    change_count = 0
    seat = source_seats[y][x]
    if seat == "L" and count_adjecent(source_seats, x, y, "#") == 0:
        set_seat(target_seats, x, y, "#")
        change_count += 1
    elif seat == "#" and count_adjecent(source_seats, x, y, "#") >= 4:
        set_seat(target_seats, x, y, "L")
        change_count += 1

    return change_count

def count_seats(seats, seat) -> int:
    count = 0
    for y in range(len(seats)):
        for x in range(len(seats[0])):
            if seats[y][x] == seat:
                count += 1
    return count

while True:
    seats_copy = seats.copy()
    changes = 0
    for y in range(len(seats)):
        for x in range(len(seats[0])):
            changes += update_seats(seats, seats_copy, x, y)
    seats = seats_copy
    
    if changes == 0:
        print(count_seats(seats, "#"))
        break