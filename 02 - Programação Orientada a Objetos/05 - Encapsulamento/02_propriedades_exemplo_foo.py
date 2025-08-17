class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    # Setter para modificar o valor de x
    @x.setter
    def x(self, value):
        self._x += value

    # Pouco usado - Só quando você não quer deletar o atributo diretamente
    # Exemplo: quando você quer resetar o valor de x para um valor padrão
    @x.deleter
    def x(self):
        self._x = -1
        # del self._x - # Não deletar, mas sim reatribuir um valor padrão

foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)
