
def choose_user():
    hecho = 0
    while hecho != 1:
        choose_user = input("\n piedra, papel o tijera\n").lower()
        if choose_user == "tijera":
            hecho = 1
            continue
        else:
            if choose_user == "piedra":
                hecho = 1
                continue
            else:
                if choose_user == "papel":
                    hecho = 1
                    continue
                else:
                    print("no valido vuelve a intentarlo!")
        
        
        if choose_user == "tijeras" or choose_user == "tireja" or choose_user == "tirejas":
            choose_user = "tijera"
            
    return choose_user

def choose_computer():
    import random
    options = ["tijera","papel","piedra"]
    choose_computer = random.choice(options)
    return choose_computer

def choose_option():
    computer = choose_computer()
    user = choose_user()
    print(" PC: ",computer,"\n Usuario: ",user)
    return computer, user

def points():
    computer = 0
    user = 0
    computer_option, user_option = choose_option()
    if computer_option == user_option:
        print("empate")
    else:
        if computer_option == "piedra" and user_option == "tijera" or computer_option == "tijera" and user_option == "papel" or computer_option == "papel" and user_option == "piedra":
            computer = 1
            print("gana computadora +1pt")
        else:
            print("gana usuario +1pt")
            user = 1
    return computer, user
        
def win():
    points_user = 0
    points_computer = 0
    fin = 0
    while fin != 1:
        computer,user = points()
        if computer == 0 and user == 0:
            continue
        else:
            if user == 1:
                points_user = 1 + points_user
                print("\n usuario: ",points_user)
                print(" PC: ",points_computer,"\n")
                if points_user >= 2 and points_user > points_computer:
                    print("Usuario gana")
                    fin = 1
            elif computer == 1:
                points_computer = 1 + points_computer
                print("\nUsuario: ",points_user)
                print(" PC: ",points_computer,"\n")
                if points_computer >= 2 and points_computer > points_user:
                    print("computadora gana")
                    fin = 1
        

win()


