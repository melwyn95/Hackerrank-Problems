def take_input(n):
    t = []
    for i in range(n):
        s = raw_input()
        t.append(s[0:len(s)-1])
    return t
N = int(raw_input())
deck_a = take_input(N)
M = int(raw_input())
deck_b = take_input(M)

start_a = start_b = 0
end_a = len(deck_a) - 1
end_b = len(deck_b) - 1
len_a = len(deck_a)
len_b = len(deck_b)

for i in range(M): deck_a.append('#')
for i in range(N): deck_b.append('#')

precedence = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}

def is_game_over():
    global len_a, len_b
    #print len_a, len_b
    return len_a == 0 or len_b == 0

def incr(n, m, player):
    #global len_a, len_b
    #if player == 1: len_a += 1
    #else: len_b += 1
    return (n + 1) % m

def decr(n, m, player):
    #global len_a, len_b
    #if player == 1: len_a -= 1
    #else: len_b -= 1
    return (n - 1 + m) % m

def enqueue(player, x):
    if player == 1:
        global end_a, len_a
        end_a = incr(end_a, N+M, 1)
        deck_a[end_a] = x
        len_a += 1
    else:
        global end_b, len_b
        end_b = incr(end_b, N+M, 2)
        deck_b[end_b] = x
        len_b += 1

def dequeue(player):
    x = -1
    if player == 1:
        global start_a, len_a, deck_a
        x = deck_a[start_a]
        #print start_a, x
        deck_a[start_a] = '#'
        start_a = incr(start_a, N+M, 1)
        len_a -= 1
        #print start_a, x
        #print '----------------'
    else:
        global start_b, len_b, deck_b
        x = deck_b[start_b]
        #print start_b, x
        deck_b[start_b] = '#'
        start_b = incr(start_b, N+M, 2)
        len_b -= 1
        #print start_b, x
        #print '----------------'
    if x == '#': x = -1
    return x


######################################################
def game(war_a, war_b, is_war):
    #print 'game(', war_a, war_b, is_war, ')'
    turn_a = dequeue(1)
    turn_b = dequeue(2)

    #print war_a
    #print war_b
    #print deck_a
    #print deck_b
    #print turn_a, turn_b

    war_a.append(turn_a)
    war_b.append(turn_b)
    #TODO: precendece look up should be in try except
    #      because dequeue can return -1 which would
    #      result in Key Error

    #Hacky Safe Code
    if turn_a == -1 or turn_b == -1: return

    #print turn_a, turn_b
    #print precedence[turn_a], precedence[turn_b] 
    if precedence[turn_a] > precedence[turn_b]:
        #A wins
        for _ in range(len(war_a)): enqueue(1, war_a[_])
        for _ in range(len(war_b)): enqueue(1, war_b[_])
        return 1
    elif precedence[turn_a] < precedence[turn_b]:
        #B wins
        for _ in range(len(war_a)): enqueue(2, war_a[_])
        for _ in range(len(war_b)): enqueue(2, war_b[_])
        return 2
    else:
        #War
        for i in range(3):
            war_card_a = dequeue(1)
            war_car_b = dequeue(2)
            if war_card_a == -1 or war_car_b == -1: return True
            war_a.append(war_card_a)
            war_b.append(war_car_b)
        return game(war_a, war_b, True)
    
######################################################
##while is_game_over():
##    turn_a = dequeue(1)
##    turn_b = dequeue(2)
##    #TODO: precendece look up should be in try except
##    #      because dequeue can return -1 which would
##    #      result in Key Error
##
##    #Hacky Safe Code
##    if turn_a == -1 or turn_b == -1: break
##
##    if precedence(turn_a) > precedence(turn_a):
##        #A wins
##        enqueue(1, turn_a)
##        enqueue(1, turn_b)
##    elif precedence(turn_a) < precedence(turn_a):
##        #B wins
##        enqueue(2, turn_a)
##        enqueue(2, turn_b)
##    else:
##        #War
##        war_a = [turn_a]
##        war_b = [turn_b]
##        for i in range(3):
##            war_a.append(dequeue(1))
##            war_b.append(dequeue(2))
######################################################

#print deck_a
#print start_a, end_a
#print deck_b
#print start_b, end_b
#print len_a, len_b

rounds = 0
winner = -1
is_pat = False
while not is_game_over():
    rounds += 1
    winner = game([], [], False)
    if isinstance(winner, bool):
        is_pat = True
        print 'PAT'
        break
    #print deck_a
    #print deck_b
    #print len_a, len_b

if not is_pat: print winner, rounds
#print 'Game Over'





























