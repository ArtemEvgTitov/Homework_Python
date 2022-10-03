import random

def bot_move(regulations): 
    if regulations["move"] >= 7 and (regulations["total"] > regulations["move"] + 1 and regulations["total"] < regulations["move"] * 2):
        move = regulations["total"] - regulations["move"] - 1
    elif regulations["move"] == 6:
        if regulations["total"] == regulations["move"] + 2:
            move = 1
        elif regulations["total"] == regulations["move"] + 3:
            move = 2
        elif regulations["total"] == regulations["move"] + 4:
            move = 3
        elif regulations["total"] == regulations["move"] + 5:
            move = 4
        elif regulations["total"] == regulations["move"] + 6:
            move = 5
        elif regulations["total"] == regulations["move"] + 7:
            move = 6
        else:
            move = random.randint(1, regulations["move"])
    elif regulations["move"] == 5:
        if regulations["total"] == regulations["move"] + 2:
            move = 1
        elif regulations["total"] == regulations["move"] + 3:
            move = 2
        elif regulations["total"] == regulations["move"] + 4:
            move = 3
        elif regulations["total"] == regulations["move"] + 5:
            move = 4
        elif regulations["total"] == regulations["move"] + 6:
            move = 5
        else:
            move = random.randint(1, regulations["move"])
    elif regulations["move"] == 4:
        if regulations["total"] == regulations["move"] + 2:
            move = 1
        elif regulations["total"] == regulations["move"] + 3:
            move = 2
        elif regulations["total"] == regulations["move"] + 4:
            move = 3
        elif regulations["total"] == regulations["move"] + 5:
            move = 4
        else:
            move = random.randint(1, regulations["move"])
    elif regulations["move"] == 3:
        if regulations["total"] == regulations["move"] + 2:
            move = 1
        elif regulations["total"] == regulations["move"] + 3:
            move = 2
        elif regulations["total"] == regulations["move"] + 4:
            move = 3
        else:
            move = random.randint(1, regulations["move"])
    elif regulations["move"] == 2:
        if regulations["total"] == regulations["move"] + 2:
            move = 1
        elif regulations["total"] == regulations["move"] + 3:
            move = 2
        else:
            move = random.randint(1, regulations["move"])
    elif regulations["move"] == 1:
        if regulations["total"] == regulations["move"] + 2:
            move = 1
        else:
            move = random.randint(1, regulations["move"])
    elif regulations["total"] < regulations["move"]:
        move = regulations["total"]
    else:
        move = random.randint(1, regulations["move"])

    return move
