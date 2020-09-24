import string
import math
from tqdm import tqdm


def darth(a, b, c ,d):
    return a + d + b + c


def settler(that_string):
    output = ""
    for element in that_string:
        if element != " ":
            output = output + element
    return output


characters = string.ascii_uppercase + string.punctuation + string.digits + " " + "\n" + "\t" + string.ascii_lowercase


def encrypt(x):
    crisscrossed = {}
    y1 = int(x[2:5])
    y2 = int(settler(x[-7:-4]))

    p = 0
    blanky = ""
    variable_x = len(x) / int(x[-3])
    for i in x:
        try:
            pof = x[p:(p + int(variable_x) + 1)]
            digit = int(pof)
            digits = digit ** (y1)
            blanky = blanky + str(digits)
            p += 1
        except:
            pass

    variable_y = len(blanky)/(variable_x*(int(x[3])))
    variable_xy = int(variable_x*(int(x[3])))
    variable_y = int(math.sqrt(variable_y)) - 1
    pos = 0
    neg = 0
    list_lord = []
    for element in range(variable_y):
        list_duke = []
        for duke_element in range(variable_y):
            list_duke.append(blanky[pos:pos + variable_xy])
            pos += variable_xy
        list_lord.append(list_duke)
    list_queen = []
    ilo = 0
    for list_prince in range(variable_y):
        if ilo < (variable_y - 1):
            alpha = list_lord[ilo]
            beta = list_lord[ilo + 1]
            jak = 0
            for list_princess in range(variable_y):
                    if jak < (variable_y - 1):
                        list_queen.append(darth(alpha[jak],alpha[jak + 1], beta[jak], beta[jak + 1]))
                        jak += 1
            ilo += 1

    lassiter = int(y2)

    for character in characters:
        summation = 0
        summation += int(list_queen[lassiter])
        crisscrossed[character] = str(summation)
        lassiter += int(x[-2])
    return crisscrossed


def encryption():
    encrypted_string = ""
    e_string = input("Please type in the message to be encrypted: ")
    crisscrossed = encrypt(input("Please give a key to begin encryption: "))
    print("encrypting...")
    for element in e_string:
        encrypted_string = encrypted_string + crisscrossed[str(element)]
    print("Encryption successful!")
    print("Encrypted Message: ", encrypted_string)


encryption()