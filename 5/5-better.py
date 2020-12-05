# better solution
# source: reddit

board_passes = open("5.txt", "r").read().split("\n")

highscore = 0
ids = list()

for boardpass in board_passes:

    x = boardpass[:7]
    x = x.replace("F", "0").replace("B", "1")
    x = int(x, 2)

    y = boardpass[7:]
    y = y.replace("L", "0").replace("R", "1")
    y = int(y, 2)

    seatid = x * 8 + y

    highscore = max(highscore, seatid)
    ids.append(seatid)

print(highscore)