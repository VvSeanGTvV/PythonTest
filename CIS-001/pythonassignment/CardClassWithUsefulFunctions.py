class Card:
  def __init__(self, ranks: int, suits: str):
    self.ranks = ranks
    self.suits = suits

  # custom func
  def color(self):
    if (self.suits.lower() == 'hearts' or self.suits.lower() == 'diamonds'): 
      return 'red'
    else: 
      return 'black'

  def get_rank(self): #yey ranking
    if (self.ranks == 1): return 'A'
    elif(self.ranks == 11): return 'J'
    elif(self.ranks == 12): return 'Q'
    elif(self.ranks == 13): return 'K'
    return self.ranks
    
  # single variable self
  def __str__(self): # usage on print and such
    return f"{self.get_rank()} of {self.suits}"
    
  def __repr__(self): # usage on list/array
    return f"Card({self.ranks}, '{self.suits}')"
    
  # two variable comparison
  def __eq__(self, b): # usage on two value (self which is primary and b which is the secondary)
    if (self.ranks == b.ranks and self.suits.lower() == b.suits.lower()): return True
    return False
    
  def __lt__(self, b): # usage on list sorting / max / min
    if (int(self.ranks) < int(b.ranks)): return True # returns from small to big
    else: return False # default

if __name__ == "__main__":
  # Problem 1: the Card class
  c = Card(12, 'hearts')
  print(c.color()) # color(...)
  
  # Problem 2: __str__ and __repr__
  print(c) # __str__
  print([c, Card(1, 'spades')]) # __repr__
  print("you drew the " + str(c)) # __str__
  
  # Problem 3: __eq__
  a = Card(12, "hearts")
  print(a == Card(12, "hearts")) # __eq__
  print(a == Card(12, "spades")) # __eq__
  # b) by default (without __eq__ customized), it compares two as object id which is never equal to each other.
  # c) self and b becomes the two inputs for __eq__, 'self' is the main variable, whilist 'b' is the secondary variable comparing the two
  pile = [Card(1, "clubs"), Card(5, "clubs")]
  print(Card(5, "clubs") in pile) # __eq__
  # it compares multiple list but 'self' is the second value while 'b' is the primary value, basically it does a iteration loop of all values think of it like: 
  # var a = something
  # foreach(var b in list)
  # { ... __eq__(b, a)... }
  
  # Problem 4: __lt__ and sorting
  hand = [Card(12, "hearts"),
          Card(3, "spades"),
          Card(7, "clubs")]
  print(sorted(hand)) # __lt__
  print(max(hand)) # __lt__
  print(Card(5, "hearts") < Card(5, "spades")) # __lt__
  print(Card(5, "spades") < Card(5, "hearts")) # __lt__
  #c) Look at the last two lines. Neither card is less than the other, but with your __eq__ they aren’t equal either. Is that a problem for sorting a hand of cards? Why or why not?
  # not really as it would just be like 1 red 1 black 2 red 2 black... etc.
  # but then again it would be like a pattern of red and black rather than actually sorted w/ colors from red 1 -> 13 and black 1 -> 13
  
  #Problem 5: face cards
  print(Card(12, "hearts"))    # should print Q of hearts
  print(Card(1, "spades"))     # should print A of spades
  print(Card(7, "clubs"))      # should print 7 of clubs
  print([Card(12, "hearts")])  # should print [Card(12, 'hearts')]
