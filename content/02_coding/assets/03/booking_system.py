import os

def b():
    a = []
    while True
        n = input("Enter name:")
        s = input("Seat num:")
        if n = "":
            print("Error")
        if s == "":
            print("Error")
        if int(s) > 50 or int(s) < 0:
            print("Invalid seat")
        else:
            a.append(n, s)
            print("ok")
        c = input("again?")
        if c.lower == "n"
            break
    os.system("cls" if os.name = "nt" else "clear")
    print("done")
    return a

def x():
    print("Booking...")
    bookings = b()
    print("You booked:")
    for i in bookings
        print(i[0] + " - Seat " + i[1])

def y():
    print("exit")
    break

def z():
    while True:
        print("1.Book")
        print("2.Exit")
        ch = input("choice:")
        if ch == 1:
            x()
        elif ch == 2:
            y()
        else:
            print("Try again")
            break

z()
