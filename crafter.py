

tx = 3
ty = 3

px = 1
py = 1

gx = 1
gy = 1

def draw_table(tx, ty, px, py):
    for y in range(ty):
        for x in range(tx):
            if x == (px-1) and y == (py-1):
                print("⚫️", end = " ")
            elif x == (gx-1) and y ==(gy-1):
                print("🔴", end = " ")
            else:
                print("⬜️", end = " ")
        print()
        

while True:
    side = input("куда перемещаемся: ")
    
    if side == "w" and py > 1:
        py -= 1
    elif side == "s" and py < ty:
        py += 1
    elif side == "d" and px < tx:
        px += 1
    elif side == "a" and px > 1:
        px -= 1
    elif side == "q":
        gx = px
        gy = py
    else:
        print("за границы стола нельзя выйти!")
    print()
 
    draw_table(tx, ty, px, py)
    print()