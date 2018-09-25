

init -50 python:
    import random

    class CardGameRival:
        
        def __init__(self,avatar,name):
            self.name = name
            self.mood = 0
            self.avatar = avatar
        
        def pick_my_card_last(self):
            for i in range(0,n_cards):
                if  cards_my[i].interesting:
                    x = i
            return x
        
        def allow_to_take(self):
            for i in range(0,n_cards):
                cards_rival[i].allow = True
        
        def allow_to_defend(self):
            return True
        
        def want_to_defend(self):
            return True
        
        def what_to_xchange(self):
            i = random.randrange(0,n_cards)
            j = random.randrange(0,n_cards)
            while i==j:
                j = random.randrange(0,n_cards)
            return (i,j)
        
        def give_away_card(self):
            return random.randrange(0,n_cards)

    class CardGameRivalUn(CardGameRival):
        def pick_my_card(self):
            x = random.randrange(0,n_cards)
            while cards_my[x].name == name_of_none or cards_my[x].interesting:
                x = random.randrange(0,n_cards)
            return x
        
        def pick_my_card_last(self):
            return self.pick_my_card()

    class CardGameRivalUs(CardGameRival):
        def pick_my_card(self):
            type,index = cards_interact()
            return index
        
        def allow_to_take(self):
            for i in range(0,n_cards):
                cards_rival[i].allow = False
            i = random.randrange(0,n_cards)
            while cards_rival[i].hot:
                i = random.randrange(0,n_cards)
            cards_rival[i].allow = True
            cards_rival[i].interesting = True
        
        def want_to_defend(self):
            return False
        
        def allow_to_defend(self):
            return False


    class CardGameRivalDv(CardGameRival):
        def what_to_xchange(self):
            i = random.randrange(0,n_cards)
            while not cards_rival[i].interesting:
                i = random.randrange(0,n_cards)
            j = random.randrange(0,n_cards)
            while i==j:
                j = random.randrange(0,n_cards)
            return (i,j)
        
        def pick_my_card(self):
            x_set = []
            for i in range(0,n_cards):
                if  cards_my[i].hot and cards_my[i].name != name_of_none:
                    x_set.append(i)
            if  x_set == []:
                x = random.randrange(0,n_cards)
                while cards_my[x].name == name_of_none:
                    x = random.randrange(0,n_cards)
                return x
            else:
                return renpy.random.choice(x_set)
        
        def pick_my_card_last(self):
            return self.pick_my_card()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
