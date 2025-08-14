class Bicicleta:
    """
    Classe que representa uma bicicleta.
    Atributos:
        cor (str): Cor da bicicleta.
        modelo (str): Modelo da bicicleta.
        ano (int): Ano de fabricação da bicicleta.
    Métodos:
        buzinar(): Emite o som da buzina da bicicleta.
        parar(): Exibe mensagens indicando que a bicicleta está parando.
        correr(): Exibe mensagem indicando que a bicicleta está em movimento.
        __str__(): Retorna uma representação em string da bicicleta.
    """



    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim!")

    def parar(self):
        print("Parando bicicleta...")
        print("...")
        print("Bicicleta parada!")

    def correr(self):
        print("correndo com a bicicleta...")

    # esse não é um metodo usado, pois o atributo cor já é acessível diretamente (publicamente)
    def get_cor(self):
        return self.cor

    # def __str__(self):
    #     return f"Bicicleta(cor= {self.cor}, modelo= {self.modelo}, ano= {self.ano})"

    # def __str__(self):
    #     return f"Bicicleta({self.cor}, {self.modelo}, {self.ano})"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        # Utiliza f-string para formatação de string, __class__.__name__ para obter o nome da classe dinamicamente,
        # e um list comprehension para iterar sobre os pares chave-valor do dicionário __dict__ (que armazena os atributos da instância),
        # gerando uma representação textual detalhada do objeto.


bike1 = Bicicleta("Azul", "Speed", 2025, 852)

bike1.buzinar()
bike1.parar()
bike1.correr()
print(f"Cor: {bike1.cor}, Modelo: {bike1.modelo}, Ano: {bike1.ano}, Valor: {bike1.valor}")

print(f"A cor dessa bicicleta é {bike1.get_cor()}") # não é necessário, pois bike1.cor já é acessível diretamente
print(bike1)
