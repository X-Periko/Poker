import random as r

Baraja = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p10', 'p11', 'p12',
            't1', 't2', 't3', 't4', 't5', 't6', 't7', 't10', 't11', 't12',
            'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd10', 'd11', 'd12',
            'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c10', 'c11', 'c12']

AI_cards = []
Player_cards = []
pointsAI = []
pointsPlayer = []

#Poner 4 cartas

Mesa = []

for x in range(0,4):
    selected_card = r.choice(Baraja)
    selected_index = Baraja.index(selected_card)
    del Baraja[selected_index]
    Mesa.append(selected_card)
    

while len(Baraja) > 0:
    AI_cards = []
    def shuffleAI():
        selected_card =  r.choice(Baraja)
        selected_index = Baraja.index(selected_card)
        del Baraja[selected_index]
        AI_cards.append(selected_card)
    
    for x in range(0,3):
       shuffleAI()
    print(AI_cards)

    Player_cards = []
    def shuffleP():
        selected_card =  r.choice(Baraja)
        selected_index = Baraja.index(selected_card)
        del Baraja[selected_index]
        Player_cards.append(selected_card)

    for x in range(0,3):
        shuffleP()
    print(Player_cards)

    print(Mesa)