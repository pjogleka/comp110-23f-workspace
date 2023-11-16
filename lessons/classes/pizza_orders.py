from lessons.classes.pizza import Pizza

sals_pizza = Pizza("large", 10, True)
#accessing/setting attributes
#my_pizza.size = 'large'
#my_pizza.toppings = 10
#my_pizza.gluten_free = True


def price(input_pizza: Pizza):
    if input_pizza.size  == 'large':
        price = 6.25
    else:
        price = 5
    return price

print(price(sals_pizza))