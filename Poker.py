import random as r

#Repartir cartas 

free_cards = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p10', 'p11', 'p12',
              't1', 't2', 't3', 't4', 't5', 't6', 't7', 't10', 't11', 't12',
              'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd10', 'd11', 'd12',
              'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c10', 'c11', 'c12']
AI_cards = []
Player_cards = []

def shuffleAI():
    selected_card =  r.choice(free_cards)
    selected_index = free_cards.index(selected_card)
    del free_cards[selected_index]
    AI_cards.append(selected_card)
    
for x in range(0,5):
    shuffleAI()
print(AI_cards)

def shuffleP():
    selected_card =  r.choice(free_cards)
    selected_index = free_cards.index(selected_card)
    del free_cards[selected_index]
    Player_cards.append(selected_card)

for x in range(0,5):
    shuffleP()
print(Player_cards)

#Comprobar parejas
pairs = []
for x in range (0,5):
    for y in range(0,5):
        if AI_cards[x] == AI_cards[y]:
            continue
        if '1' in AI_cards[x] and '1' in AI_cards[y]:
            if not len(AI_cards[x]) == 3 and not len(AI_cards[y]) == 3:
                if AI_cards[x] not in pairs and AI_cards[y] not in pairs:    
                    pairs.append(AI_cards[x])
                    pairs.append(AI_cards[y])
                print(AI_cards[x], ' and ', AI_cards[y])
        if '2' in AI_cards[x] and '2' in AI_cards[y]:
            if not len(AI_cards[x]) == 3 and not len(AI_cards[y]) == 3:
                if AI_cards[x] not in pairs and AI_cards[y] not in pairs:    
                    pairs.append(AI_cards[x])
                    pairs.append(AI_cards[y])
                print(AI_cards[x], ' and ', AI_cards[y])
        if '3' in AI_cards[x] and '3' in AI_cards[y]:
            if AI_cards[x] not in pairs and AI_cards[y] not in pairs:    
                pairs.append(AI_cards[x])
                pairs.append(AI_cards[y])
                print(AI_cards[x], ' and ', AI_cards[y])
        if '4' in AI_cards[x] and '4' in AI_cards[y]:
            if AI_cards[x] not in pairs and AI_cards[y] not in pairs:    
                pairs.append(AI_cards[x])
                pairs.append(AI_cards[y])
                print(AI_cards[x], ' and ', AI_cards[y])
        if '5' in AI_cards[x] and '5' in AI_cards[y]:
            if AI_cards[x] not in pairs and AI_cards[y] not in pairs:    
                pairs.append(AI_cards[x])
                pairs.append(AI_cards[y])
                print(AI_cards[x], ' and ', AI_cards[y])
        if '6' in AI_cards[x] and '6' in AI_cards[y]:
            if AI_cards[x] not in pairs and AI_cards[y] not in pairs:    
                pairs.append(AI_cards[x])
                pairs.append(AI_cards[y])
                print(AI_cards[x], ' and ', AI_cards[y])
        if '7' in AI_cards[x] and '7' in AI_cards[y]:
            if AI_cards[x] not in pairs and AI_cards[y] not in pairs:    
                pairs.append(AI_cards[x])
                pairs.append(AI_cards[y])
                print(AI_cards[x], ' and ', AI_cards[y])
        if '10' in AI_cards[x] and '10' in AI_cards[y]:
            if AI_cards[x] not in pairs and AI_cards[y] not in pairs:    
                pairs.append(AI_cards[x])
                pairs.append(AI_cards[y])
                print(AI_cards[x], ' and ', AI_cards[y])
        if '11' in AI_cards[x] and '11' in AI_cards[y]:
            if AI_cards[x] not in pairs and AI_cards[y] not in pairs:    
                pairs.append(AI_cards[x])
                pairs.append(AI_cards[y])
                print(AI_cards[x], ' and ', AI_cards[y])
        if '12' in AI_cards[x] and '12' in AI_cards[y]:
            if AI_cards[x] not in pairs and AI_cards[y] not in pairs:    
                pairs.append(AI_cards[x])
                pairs.append(AI_cards[y])
                print(AI_cards[x], ' and ', AI_cards[y])
pairs_count = int(len(pairs) / 2)
print('I have ', pairs_count, ' pairs')
if len(pairs) > 0:
    print(pairs)

#Comprobar tríos

trios = []
for x in range (0,5):
    for y in range(0,5):
        for z in range(0,5):
            if AI_cards[x] == AI_cards[y]:
                continue
            if AI_cards[x] == AI_cards[z]:
                continue
            if AI_cards[y] == AI_cards[z]:
                continue
            if '1' in AI_cards[x] and '1' in AI_cards[y] and '1' in AI_cards[z]:
                if not len(AI_cards[x]) == 3 and not len(AI_cards[y]) == 3 and not len(AI_cards[z] == 3):
                    if AI_cards[x] not in trios and AI_cards[y] not in trios and AI_cards[z] not in trios:    
                        trios.append(AI_cards[x])
                        trios.append(AI_cards[y])
                        trios.append(AI_cards[z])
                    print(AI_cards[x], ' and ', AI_cards[y], ' and ', AI_cards[z])
            if '2' in AI_cards[x] and '2' in AI_cards[y] and '2' in AI_cards[z]:
                if not len(AI_cards[x]) == 3 and not len(AI_cards[y]) == 3 and not len(AI_cards[z] == 3):
                    if AI_cards[x] not in trios and AI_cards[y] not in trios and AI_cards[z] not in trios:    
                        trios.append(AI_cards[x])
                        trios.append(AI_cards[y])
                        trios.append(AI_cards[z])
                    print(AI_cards[x], ' and ', AI_cards[y], ' and ', AI_cards[z])
            if '3' in AI_cards[x] and '3' in AI_cards[y] and '3' in AI_cards[z]:
                if AI_cards[x] not in trios and AI_cards[y] not in trios and AI_cards[z] not in trios:    
                    trios.append(AI_cards[x])
                    trios.append(AI_cards[y])
                    trios.append(AI_cards[z])
                print(AI_cards[x], ' and ', AI_cards[y], ' and ', AI_cards[z])
            if '4' in AI_cards[x] and '4' in AI_cards[y] and '4' in AI_cards[z]:
                if AI_cards[x] not in trios and AI_cards[y] not in trios and AI_cards[z] not in trios:    
                    trios.append(AI_cards[x])
                    trios.append(AI_cards[y])
                    trios.append(AI_cards[z])
                print(AI_cards[x], ' and ', AI_cards[y], ' and ', AI_cards[z])
            if '5' in AI_cards[x] and '5' in AI_cards[y] and '5' in AI_cards[z]:
                if AI_cards[x] not in trios and AI_cards[y] not in trios and AI_cards[z] not in trios:    
                    trios.append(AI_cards[x])
                    trios.append(AI_cards[y])
                    trios.append(AI_cards[z])
                print(AI_cards[x], ' and ', AI_cards[y], ' and ', AI_cards[z])
            if '6' in AI_cards[x] and '6' in AI_cards[y] and '6' in AI_cards[z]:
                if AI_cards[x] not in trios and AI_cards[y] not in trios and AI_cards[z] not in trios:    
                    trios.append(AI_cards[x])
                    trios.append(AI_cards[y])
                    trios.append(AI_cards[z])
                print(AI_cards[x], ' and ', AI_cards[y], ' and ', AI_cards[z])
            if '7' in AI_cards[x] and '7' in AI_cards[y] and '7' in AI_cards[z]:
                if AI_cards[x] not in trios and AI_cards[y] not in trios and AI_cards[z] not in trios:    
                    trios.append(AI_cards[x])
                    trios.append(AI_cards[y])
                    trios.append(AI_cards[z])
                print(AI_cards[x], ' and ', AI_cards[y], ' and ', AI_cards[z])
            if '10' in AI_cards[x] and '10' in AI_cards[y] and '10' in AI_cards[z]:
                if AI_cards[x] not in trios and AI_cards[y] not in trios and AI_cards[z] not in trios:    
                    trios.append(AI_cards[x])
                    trios.append(AI_cards[y])
                    trios.append(AI_cards[z])
                print(AI_cards[x], ' and ', AI_cards[y], ' and ', AI_cards[z])
            if '11' in AI_cards[x] and '11' in AI_cards[y] and '11' in AI_cards[z]:
                if AI_cards[x] not in trios and AI_cards[y] not in trios and AI_cards[z] not in trios:    
                    trios.append(AI_cards[x])
                    trios.append(AI_cards[y])
                    trios.append(AI_cards[z])
                print(AI_cards[x], ' and ', AI_cards[y], ' and ', AI_cards[z])
            if '12' in AI_cards[x] and '12' in AI_cards[y] and '12' in AI_cards[z]:
                if AI_cards[x] not in trios and AI_cards[y] not in trios and AI_cards[z] not in trios:    
                    trios.append(AI_cards[x])
                    trios.append(AI_cards[y])
                    trios.append(AI_cards[z])
                print(AI_cards[x], ' and ', AI_cards[y], ' and ', AI_cards[z])

trioscount = int(len(trios) / 3)
print('I have ', trioscount, ' trios')
if len(trios) > 0:
    print(trios)

#Identificar full

if len(pairs) >= 2 and len(trios) >= 3:
    HasFull = True
else:
    HasFull = False

#Identificar póker

for x in range(0,5):
    for y in range(0,5):
        for z in range(0,5):
            for n in range(0,5):
                if 'p' in AI_cards[x] and 'p' in AI_cards[y] and 'p' in AI_cards[z] and 'p' in AI_cards[n]:
                    HasPoker = True
                    break
                else: 
                    HasPoker = False

#Apuesta inicial y reparto de dinero

AI_money = 10
Player_money = 10
apuesta = 0

AI_money = AI_money - 1
Player_money = Player_money - 1
apuesta =+ 2

#Pensamiento de IA

EstimatedToWin = 50

def Check():
    if pairs_count == 1:
        EstimatedToWin = EstimatedToWin + 10
    elif pairs_count == 2:
        EstimatedToWin = EstimatedToWin + 20
    if trioscount == 1:
        EstimatedToWin = EstimatedToWin + 25
    if HasFull:
        EstimatedToWin = EstimatedToWin + 35
    if HasPoker:
        EstimatedToWin = EstimatedToWin + 40

Check

#Juego
while Player_money > 0 and AI_money > 0:
    Desea_subir = 'Desea subir la apuesta o retirarse (s/r)? Tiene ', Player_money, ' dólares'
    print(Desea_subir)
    Acción = input('> ')
    To_add = 0
    if Acción == 's':
        To_add = input('Cuanto desea subir? ')
        Acción = input('Desea cambiar cartas?(y/n) ')
        if Acción == 'y':
            ParaCambiar = input('Qué cartas desea cambiar? ')
            while ParaCambiar not in Player_cards:
                ParaCambiar = input('Qué cartas desea cambiar? ')
            def Cambiar():
                print(Player_cards)
                OldCard = Player_cards.index(ParaCambiar)
                del Player_cards[int(OldCard)]
                NewCard = r.choice(free_cards)
                Player_cards.append(NewCard)
                free_cards.remove(NewCard)
                print(Player_cards)
            Cambiar()
            print('Desea cambiar más cartas?(y/n) ')
            while input('> ') == 'y':
                    ParaCambiar = input('Qué carta desea cambiar? ')
                    Cambiar
                    print(Player_cards)
    if Acción == 'r':
        print('AI gana ', apuesta, ' dólares')
        AI_money = AI_money + apuesta
        apuesta = 0

    apuesta = apuesta + int(To_add)
    EstimatedToWin = EstimatedToWin - (int(To_add) * 5)
    if EstimatedToWin > 60:
        print('La IA iguala tu apuesta')
        AI_money = AI_money - int(To_add)
        apuesta = apuesta + int(To_add)
    elif EstimatedToWin > 80:
        print('La IA iguala tu apuesta')
        AI_money = AI_money - int(To_add)
        apuesta = apuesta + int(To_add)
        print('Y sube un dólar!')
        AI_money = AI_money - 1
        apuesta = apuesta + 1
        if input('Iguala o se retira? (i/r)') == 'i':
            Player_money = Player_money -1 
            apuesta = apuesta + 1
        else:
            print('La IA ha ganado ', apuesta, ' dólares')
            apuesta = 0
        
    print('La apuesta ahora es de:', apuesta)

if Player_money == 0:
    print('Has perdido contra la IA')
else:
    print('Ganaste!')