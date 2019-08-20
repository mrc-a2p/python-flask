import random 

def run():
    numero_found = False
    random_numero = random.randint(0,30)

    while not numero_found:
        numero = int(input("intenta un numeor:"))
        
        
        if numero == random_numero:
            print("felicidades ")
            numero_found = True
        elif numero > random_numero:
            print("El numeor es mas pequeño")
        else:
            print("el numero es mas grande")


if __name__ == "__main__":
    run()