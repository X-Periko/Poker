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
Card5 = None
for x in range (0,5):
    if '1' or '2' or '3' or '4' or '5' or '6' or '7' or '10' or '11' or '12' in AI_cards[x]:
        if x == 1: 
            Card1 = True
        if x == 2:
            Card2 = True
        if x == 3:
            Card3 = True
        if x == 4:
            Card4 = True 
        if x == 5:
            Card5 = True
if Card1 and Card2:
    pairs.append(Card1)
    pairs.append(Card2)
    pair_count =+ 1

if Card1 and Card3:
    pairs.append(Card1)
    pairs.append(Card3)
    pair_count =+ 1

if Card1 and Card4:
    pairs.append(Card1)
    pairs.append(Card4)
    pair_count =+ 1

if Card1 and Card5:
    pairs.append(Card1)
    pairs.append(Card5)
    pair_count =+ 1

if Card2 and Card3:
    pairs.append(Card2)
    pairs.append(Card3)
    pair_count =+ 1

if Card2 and Card4:
    pairs.append(Card2)
    pairs.append(Card4)
    pair_count =+ 1

if Card2 and Card5:
    pairs.append(Card2)
    pairs.append(Card5)
    pair_count =+ 1

if Card4 and Card3:
    pairs.append(Card4)
    pairs.append(Card3)
    pair_count =+ 1

if Card5 and Card3:
    pairs.append(Card5)
    pairs.append(Card3)
    pair_count =+ 1

if Card4 and Card5:
    pairs.append(Card4)
    pairs.append(Card5)
    pair_count =+ 1

print('I have ', pairs_count, ' pairs')
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