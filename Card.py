'''
A card from a deck of cards
'''
class Card():

    def __init__(self,suit,face,value):
        self.suit = suit
        self.face = face
        self.value = value

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def get_face(self):
        return self.face

    def suit_and_face(self):
        return self.face + self.suit
