class Sweetgreens: 
    """
    represents a sweetgreens list 
    attributes: vegetable, grain, protein, standard topping, premium topping, bread
    """
    def __init__(self, vegetable = [], grain='wild rice', protein='chicken', standard='tomatoes', premium='corn', dressing='vinegar', bread='wheat'):
        self.vegetable = vegetable
        self.grain = grain
        self.protein = protein
        self.standard = standard
        self.premium = premium 
        self.dressing = dressing
        self.bread = bread 
    
    def __str__(self):
        """
        returns a salad order in human readable format
        """
        return f"Your sweetgreen order is {' , '.join(self.vegetable)}, {self.grain}, {self.protein}, {self.standard}, {self.premium} with {self.dressing} dressing and a piece of {self.bread} bread."

    def vegetables(self,number_of_vegetables):
        """
        will add extra amount of payment 
        """
        price = 0.00
        if number_of_vegetables==3:
            price += 2.75
            return f"You will need to pay an extra of {price} for an extra serving of vegetable"
        if number_of_vegetables==4:
            price += 5.50
            return f"You will need to pay an extra of {price} for 2 extra serving of vegetables"
        if number_of_vegetables>4:
            return f"Please, only 4 vegetables in total. You are not a cow - moo moo. \U0001F923"
        else:
            return f"Please just pay $10"
    
    def beverage(self, drink):
        """
        add a drink onto your order 
        """
         return f"Your order has {drink} included"

    def __contains__(self,parameter1):
        """
        will return true if bread is part of order
        will return false if bread is not part of order
        """
        if parameter1 in self.bread:
            return True
        else:
            return False


Myat_Order = Sweetgreens(['Kale','Arugula','Spinach','Romaine','Mesclun'],'Quinoa', 'Blackened Chicken Thighs', 'Corn', 'Avocado','Sesame Miso Ginger','White')
print(Myat_Order)
print(Myat_Order.vegetables(5))
print(Myat_Order.beverage('Tangerine Cerveza'))

Vicky_Order2 = Sweetgreens('Kale', 'Qunoa', 'Steelhead','Corn','Avocado','Olive Oil')
print('White' in Vicky_Order2)

