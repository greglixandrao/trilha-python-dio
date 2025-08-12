class Bicicleta:

    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

    def buzinar(self):
        print("Plim plim!")

    def parar(self):
        print("Parando bicicleta...")
        print("...")
        print("Bicicleta parada!")

    def correr(self):
        print("correndo com a bicicleta...")

    def __str__(self):
        return f"Bicicleta(cor= {self.cor}, modelo= {self.modelo}, ano= {self.ano})"

    # def __str__(self):
    #     return f"Bicicleta({self.cor}, {self.modelo}, {self.ano})"

bike1 = Bicicleta("Azul", "Speed", 2025)

bike1.buzinar()
bike1.parar()
bike1.correr()
print(f"Cor: {bike1.cor}, Modelo: {bike1.modelo}, Ano: {bike1.ano}")
print(bike1)