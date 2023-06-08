class Pantry:
    def __init__(self, food_dictionary):
        self.food_dictionary = food_dictionary
    
    def print_contents(self):
        print(self.food_dictionary)
        #print('I contain:')
        #for name,amount in self.food_dictionary:
            #print(f'{amount} {name}')
     
    def add_food(self, name, amount):
        if name in self.food_dictionary:
            self.food_dictionary[name] += amount
        else:
            self.food_dictionary[name] = amount