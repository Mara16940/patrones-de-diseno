# Patrones Creacionales: Factory Method.
#***************************************
# Transporte.
#***************************************
class Transporte:
    def entregar(self):
        pass
    
    def calcular_tiempo(self, días):
        pass
    
class TransporteCamion(Transporte):
    def entregar(self):
        return "Entrega terrestre realizada en camión."
    
    def calcular_tiempo(self):
        return "Tiempo estimado: 2 días."

    
class TransporteBarco(Transporte):
    def entregar(self):
        return "Entrega fluvial realizada en barco."
    
    def calcular_tiempo(self):
        return "Tiempo estimado: 25 días."

class TransporteAvion(Transporte):
    def entregar(self):
        return "Entrega aerea realizada en avión."
    
    def calcular_tiempo(self):
        return "Tiempo estimado: 12 días."
    
#***************************************
# Logística.
#***************************************
class Logistica:
    def crear_transporte(self):
        pass

    def planificar_entrega(self):
        transporte = self.crear_transporte()
        info_entrega = transporte.entregar()
        info_tiempo = transporte.calcular_tiempo()
        return f"{info_entrega}\n{info_tiempo}"


class LogisticaTerrestre(Logistica):
    def crear_transporte(self):
        return TransporteCamion()


class LogisticaMaritima(Logistica):
    def crear_transporte(self):
        return TransporteBarco()
    
#***************************************
# Caso de uso.
#***************************************
if __name__ == "__main__":
    # Probamos la planificación de un envío marítimo
    logistica = LogisticaMaritima()
    print(logistica.planificar_entrega())