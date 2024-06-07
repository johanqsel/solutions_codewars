def mutations(alice, bob, word, first):
    """Four Letter Words ~ Mutations:  description on codewars"""
    fail = [None, None]
    while alice and bob:
        if word in alice: alice.remove(word)
        if word in bob: bob.remove(word)
        if first: player = bob
        else: player = alice
        for w in player:
            n = 0
            for i in range(4):
                if w[i] == word[i]: n += 1
            if n == 3 and len(set(w)) == 4:
                if player == alice: fail[0] = "v"
                else: fail[1] = "v"
                word = w
                break
        if n != 3 :
            if player == alice:
                fail[0] = "d"
            else:
                fail[1] = "d"
        if fail == ["v", "d"]: return 0
        if fail == ["d", "v"]: return 1
        if fail == ["d", "d"]: return -1
        first = not first