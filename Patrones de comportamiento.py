# Patrones de Comportamiento: State.
#***************************************
# Estado base.
#***************************************
class EstadoReproductor:
    def presionar_boton(self):
        pass

#***************************************
# Estados concretos.
#***************************************
class EstadoDetenido(EstadoReproductor):
    def presionar_boton(self):
        return "Reproduciendo música."


class EstadoReproduciendo(EstadoReproductor):
    def presionar_boton(self):
        return "Música en pausa."
    
#***************************************
# Objeto: botón.
#***************************************
class BotonReproductor:
    def __init__(self, estado_inicial):
        self.estado = estado_inicial

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def presionar(self):
        return self.estado.presionar_boton()

#***************************************
# Caso de uso.
#***************************************
if __name__ == "__main__":
    # El reproductor arranca apagado/detenido
    reproductor = BotonReproductor(EstadoDetenido())
    print(reproductor.presionar())

    # Cambiamos su estado interno a reproduciendo
    reproductor.cambiar_estado(EstadoReproduciendo())
    print(reproductor.presionar())