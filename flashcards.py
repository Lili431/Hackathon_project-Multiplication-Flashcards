def multiples_card(n: int):
    cards = []#create my list
    for i in range(1, 13):
        card = {'id': i,'problem': f'{n} * {i}','answer': n * i}#id is the card number from 1-12, problem is the multiplication problem, answer is the result of the problem.
        cards.append(card)#add to list
    return cards