print("you see three doors select 1 from them")
door = input("1 or 2 or 3\n")
if door == 1:
    print("you denter the room,this is dark")
    print("you see two glowing eyes")
    print("what would you do?")
    ans = input("run / stand / attack")
    if ans == "run":
        print("you stumble and get hurt")
    if ans == "attack":
        print("you try to attack")
        if ans == "stand":
            print("nothing happens")
if door == "2":
    print(" it wa a trap, you die")
if door == "3":
    print("there is wall behind the door")
