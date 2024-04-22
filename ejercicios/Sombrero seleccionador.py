# Write code below 💖

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("que prefieres?")
print("1.El atardecer")
print("2.El anochecer")

Pregun_1 = input(":")

if Pregun_1 == "1":
    Gryffindor += 1
    Ravenclaw += 1
elif Pregun_1 == "2":
    Hufflepuff += 1
    Slytherin += 1
else: print("ingrese una opcion valida")


print("Cuando esté muerto, quiero que la gente me recuerde como:")
print("1) El Bien")
print("2) El Grande")
print("3) Los sabios")
print("4) El audaz")
pregun_2 = input(":")

if pregun_2 == "1":
    Hufflepuff += 2
elif pregun_2 == "2":
    Slytherin += 2
elif pregun_2 == "3":
    Ravenclaw += 2
elif pregun_2 == "4":
    Gryffindor += 2
else: print("ingrese una opcion valida")

print("Qué tipo de instrumento te agrada más?")
print("1) el violín")
print("2) la trompeta")
print("3) el piano")
print("4) El tambor")

pregun_3 = input(":")

if pregun_3 == "1":
    Slytherin += 4
elif pregun_3 == "2":
    Hufflepuff += 4
elif pregun_3 == "3":
    Ravenclaw += 4
elif pregun_3 == "4":
    Gryffindor += 4
else: print("ingrese una opcion valida")

if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
    print("¡¡¡¡ERES UN 🦁 GRYFFINDOR!!!! ")
elif Ravenclaw  >  Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
    print("¡¡¡¡ERES UN 🦅 RAVENCLAW!!!! ")
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
    print("¡¡¡ERES UN 🦡 HUFFELPUFF")
elif Slytherin > Gryffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff:
    print("¡¡¡ERES UN 🐍 SLYTHERIN!!!")



