class Game:
    def __init__(self):
        self.wincount=0
        self.score=0

    def dealCard(self):
        if self.roundnum<5:
            card = random.randint(0,51)
            while self.deck[card] == True:
                card = random.randint(0, 51)
            
            self.deck[card]=True
            face,suit=cardconvert(card)
            self.score+=Points(face)
        else:
            print("Game is over!")

    def Points(self, face):
        if face=="King" or face=="Queen" or face=="Jack":
            return 10
        elif face=="Ace":
            return 11
        else:
            return eval(face)    


class Deck:
    def __init__(self):
        self.deck=list(range(52))
        for card in self.deck:
            self.deck[card]=False

    def getCount(self):
        return self.count

    def cardconvert(self,card):
        if card < 13:
            value = card+1
            suit = "Hearts"
        elif card < 26:
            value = card-12
            suit = "Diamonds"
        elif card < 39:
            value = card-25
            suit = "Clubs"
        else:
            value = card-38
            suit = "Spades"
        face=self.stringconvert(value)
        return face,suit
    
    def stringconvert(self,value):
        if value==1:
            face="Ace"
        elif value==11:
            face="Jack"
        elif value==12:
            face="Queen"
        elif value==13:
            face="King"
        else:
            face=value
        return face


def main():
    
    
main()



'''
    for i in range(5):
        card=cards.dealCard()
        player.points+=player.Calc(card)
    player.pointShow()
'''