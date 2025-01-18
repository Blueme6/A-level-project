def main(spells = [["CHIVALROUS"], ["FIREBALL","AVADA KADAVARA"], ["CROSSBOW"]],):

    print(""" 
░▀█▀░█░█░█▀▄░█▀█░░░█▀▄░█▀█░█▀▀░█▀▀░█▀▄░░░█▀▄░█▀█░█▀▀
░░█░░█░█░█▀▄░█░█░░░█▀▄░█▀█░▀▀█░█▀▀░█░█░░░█▀▄░█▀▀░█░█
░░▀░░▀▀▀░▀░▀░▀░▀░░░▀▀░░▀░▀░▀▀▀░▀▀▀░▀▀░░░░▀░▀░▀░░░▀▀▀""")

    spells = [["CHIVALROUS"], ["FIREBALL","AVADA KADAVARA"], ["CROSSBOW"]]
    Class = input("""pick a class:
    1) knight
    2) mage
    3) ranger
    choose here:""")

    if Class == "1":
        print("""knight :
    HP : 500
    ATK: 50
    DEF: 50
    SPELL:"""+spells[0][0])
        pHP = 500
        pATK = 50
        pDEF = 50
        spell = 25
        spells = spells[0][0]
    elif Class == "2":
        print("""mage:
    HP: 350
    ATK: 100
    DEF: 30
    SPELLS:"""+spells[1][0], spells[1][1])
        pHP = 350
        pATK = 100
        pDEF = 30
        spell = 75
        spells = spells[1][0],spells[1][1]
    elif Class == "3":
        print("""ranger:
    HP: 400
    ATK: 75
    DEF: 45
    SPELL:"""+spells[2][0])
        pHP = 400
        pATK = 75
        pDEF = 45
        spell = 80
        spells = spells[2][0]
    else:
        print("re-enter choice")
        main()

    enemy = input("""choose your opponent:
    1) goblin
    2) farmer
    3) royal guard
        choose here:""")

    if enemy == "1":
        print("goblin")
        eHP = 130
        eATK = 35
        eDEF = 35

    elif enemy == "2":
        print("farmer")
        eHP = 325
        eATK = 45
        eDEF = 35

    elif enemy == "3":
        print("royal guard")
        eHP = 700
        eATK = 60
        eDEF = 60
    else:
        print("re-enter choice")
        main()

    difficulty = input("""Now choose your difficulty:
    1) Easy
    2) Normal
    3) Impossible
    Choose here:""")
    if difficulty == "1":
        eHP = eHP / 3
        eATK = eATK / 3
        eDEF = eDEF / 3
    elif difficulty == "2":
        eHP = eHP
        eATK = eATK
        eDEF = eDEF
    elif difficulty == "3":
        eHP = eHP * 1.5
        eATK = eATK * 1.5
        eDEF = eDEF * 1.5


    else:
        print("re-enter choice")
        main()

def  battle(Class, enemy, pHP, pATK, pDEF, eHP, eATK, eDEF, spells, spell,pDMG,eDMG):
    pass


def battle(Class, enemy, pHP, pATK, pDEF, eHP, eATK, eDEF, spells, spell, pDMG, eDMG,): 
    
    turn = 1
    battle(Class, enemy, pHP, pATK, pDEF, eHP, eATK, eDEF, spells, spell, pDMG, eDMG,)
    if turn == 1:
        if pDEF > 0:
            eDMG = eATK - (eATK * (pDEF / 100))
            if eDMG < 0:
                eDMG = 0
            pDEF = pDEF - eDMG
            if pDEF < 0:
               pDEF = 0
        else:
           pHP = pHP - eATK
           pATK = round(pATK)
           pHP = round(pHP)
           pDEF = round(pDEF)
           pDMG = round(pDMG)
           eATK = round(eATK)
           eHP = round(eHP)
           eDEF = round(eDEF)
           eDMG = round(eDMG)
        print("you have been attacked for", eDMG, "damage")
        print("you have ", pHP, " health, ", pDEF, " defence.")

    crit = 12
    while pHP > 0 and eHP > 0:
        choice = input("""choose you attack:
            1. attack
            2. special attack
            3. spells """ """\nchoose:
             """)
        if choice == "1":
            if eDEF == 0:
               pDMG = pATK
               eHP = eHP - pDMG
            else:
               pDMG = pATK - (pATK * (eDEF / 500))
               eDEF = eDEF - pDMG
               if eDEF < 0:
                   eDEF = 0
            print("you hit the enemy for", pDMG)
        if choice == "2":
            crit = crit - 1
            if eDEF > 0:
                spDMG = pATK * 1.25
            else:
                spDMG = pATK * 2
                spDMG = round(spDMG * (crit / 12.5))
            if crit <= 0:
                eHP = eHP + (spDMG * -1)
                eDEF = eDEF + (spDMG * -1)
                print("your opponent nulifies your attack and laughs hysterically: they have regenerated", spDMG * -1,"HP/DEF")
            else:
                eHP = eHP - spDMG
                if eDEF <= 0:
                    eDEF = 0
                else:
                    eDEF = eDEF - spDMG
                print("CRITICAL HIT you dealt", spDMG, "damage!")

        # class spells : different spells dependant on class
        import random
        if choice == "3":
            if Class == "1":
                upper = len(spells[0])
                for i in range(0, len(spells[0])):
                    print("You can cast ", spells[0][i], "\n or")

            if Class == "2":
                for i in range(0, len(spells[1])):
                    print("You can cast ", spells[1][i], "\n or")
            if Class == "3":
                for i in range(0, len(spells[2])):
                    print("You can cast ", spells[2][i], "\n or")









           #####if pspell == spells[0][0]:
               #####print("you think back to your time training with your comrades you gain", spell, "defence!")
               #####pDEF = pDEF + spell
           #####elif pspell == spells[1][0]:
               #####print("you remember what the master alchemist said, you conjure a fireball that deals", spell, "damage!")
               #####eHP = eHP - spell
           #####else:

               #####if random.randint(1, 4) == 1:
                   #####eHP = eHP - spell * 2
                   #####print("you pull out the crossbow given to you by your master,you fire an arrow.CRITICAL HIT! you dealt",spell * 2, "damage!")

           #####else:
                   #####eHP = eHP - spell
                   #####print("you pull out the crossbow given to you as a gift by your master,you fire an arrow. Dealing",spell, "damage!")

        print("you have ", pHP, " health, ", pDEF, " defence.")
        print("they have ", eHP, " health, ", eDEF, " defence.")

        if pDEF > 0:
            eDMG = eATK - (eATK * (pDEF / 100))
            if eDMG < 0:
                eDMG = 0
            pDEF = pDEF - eDMG
            if pDEF < 0:
                pDEF = 0
        else:
            eDMG = eATK
            pHP = pHP - eDMG
        print("you have been attacked for", eDMG, "damage")
        print("you have ", pHP, " health, ", pDEF, " defence.")

    if eHP <= 0:
        print("victory!")
        main()

    else:
        pHP <= 0
        print("defeat!")
        main()


    if main():
        print("CONTINUE")
    else:
        main(battle(Class, enemy, pHP, pATK, pDEF, eHP, eATK, eDEF, spells, spell, pDMG, eDMG,))

