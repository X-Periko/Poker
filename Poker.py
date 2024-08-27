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
print(free_cards)
print(AI_cards)

def shuffleP():
    selected_card =  r.choice(free_cards)
    selected_index = free_cards.index(selected_card)
    del free_cards[selected_index]
    Player_cards.append(selected_card)

for x in range(0,5):
    shuffleP()
print(free_cards)
print(Player_cards)

#Comprobar cartas
pairs = []
pairs_count = 0
for x in range (0,5):
    for y in range(0,5):
        if '1' in AI_cards[x] and '1' in AI_cards[y]:
            if x not in pairs and y not in pairs:    
                pairs.append(AI_cards[x])
                pairs.append(AI_cards[y])
                print(x, ' and ', y)
        if '2' in AI_cards[x] and '2' in AI_cards[y]:
            if x not in pairs and y not in pairs:
                pairs.append(AI_cards[x])
                pairs.append(AI_cards[y])
                print(x, ' and ', y)
        if '3' in AI_cards[x] and '3' in AI_cards[y]:
            if x not in pairs and y not in pairs:
                pairs.append(AI_cards[x])
                pairs.append(AI_cards[y])
                print(x, ' and ', y)
        if '4' in AI_cards[x] and '4' in AI_cards[y]:
            if x not in pairs and y not in pairs:
                pairs.append(x)
                pairs.append(y)
                print(x, ' and ', y)
        if '5' in AI_cards[x] and '5' in AI_cards[y]:
            if x not in pairs and y not in pairs:
                pairs.append(x)
                pairs.append(y)
                print(x, ' and ', y)
        if '6' in AI_cards[x] and '6' in AI_cards[y]:
            if x not in pairs and y not in pairs:
                pairs.append(x)
                pairs.append(y)
                print(x, ' and ', y)
        if '7' in AI_cards[x] and '7' in AI_cards[y]:
            if x not in pairs and y not in pairs:
                pairs.append(x)
                pairs.append(y)
                print(x, ' and ', y)
        if '10' in AI_cards[x] and '10' in AI_cards[y]:
            if x not in pairs and y not in pairs:
                pairs.append(x)
                pairs.append(y)
                print(x, ' and ', y)
        if '11' in AI_cards[x] and '11' in AI_cards[y]:
            if x not in pairs and y not in pairs:
                pairs.append(x)
                pairs.append(y)
                print(x, ' and ', y)
        if '12' in AI_cards[x] and '12' in AI_cards[y]:
            if x not in pairs and y not in pairs:
                pairs.append(x)
                pairs.append(y)
                print(x, ' and ', y)

pairs_count = len(pairs) / 2
print('I have ', pairs_count, ' pairs')
print(pairs)
#Apuesta inicial y reparto de dinero

AI_money = 10
Player_money = 10
apuesta = 0

AI_money = AI_money - 1
Player_money = Player_money - 1
apuesta =+ 2

Desea_subir = 'Desea subir la apuesta? Tiene ', Player_money, ' dólares'
print(Desea_subir)
To_add = input('>')
apuesta = apuesta + int(To_add)
print('La apuesta ahora es de:', apuesta)
