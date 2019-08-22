

def average_temps(temps):
    sum_of_temps = 0

    for temp in temps:
        sum_of_temps += float(temp)

    return sum_of_temps / len(temps)


if __name__ == "__main__":
    temps = [23, 45,22,41,12,9,31]


    avarage = average_temps (temps)

    print ("La temperatura promedio es de {}". format(avarage))