# Patrones Estructurales: Decorator.
#***************************************
# Pizza.
#***************************************
class Pizza:
    def get_precio(self):
        pass

class PizzaBase(Pizza):
    def get_precio(self):
        return 10500.0

#***************************************
# Clase decoradora.
#***************************************
class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_precio(self):
        return self.pizza.get_precio()


#***************************************
# Decoradores.
#***************************************
class ConQueso(PizzaDecorator):
    def get_precio(self):
        # Toma el precio de lo que ya tenías y le suma el extra
        return self.pizza.get_precio() + 2500.0


class ConPanceta(PizzaDecorator):
    def get_precio(self):
        # Toma el precio de lo que ya tenías y le suma el extra
        return self.pizza.get_precio() + 4000.0
    
#***************************************
# Caso de uso.
#***************************************
if __name__ == "__main__":
    # 1. Empezamos con una pizza base ($10500)
    mi_pizza = PizzaBase()
    
    # 2. Le agregamos queso ($10500 + $2500)
    mi_pizza = ConQueso(mi_pizza)
    
    # 3. Le agregamos panceta ($13000 + $4000)
    mi_pizza = ConPanceta(mi_pizza)
    
    print(f"Precio total de la pizza armada: ${mi_pizza.get_precio()}")