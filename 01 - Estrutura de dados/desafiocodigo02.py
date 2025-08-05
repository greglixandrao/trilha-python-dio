"""
Desafio Código 02 - Agrupamento de Participantes por Tema
"""

# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:

for _ in range(n):
    line = input().strip()
    participante, tema = line.split(",")
    if tema not in eventos:
        eventos[tema] = []
    eventos[tema].append(participante)


# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
