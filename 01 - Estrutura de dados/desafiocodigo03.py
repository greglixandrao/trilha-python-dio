# Entrada dos quartos disponíveis
def processar_reservas():

    quartos_disponiveis = set(map(int, input().split()))

    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))

    # TODO: Crie o processamento das reservas:
    # TODO: Verifique se cada reserva pode ser confirmada com base na disponibilidade dos quartos:
    confirmadas = []
    recusadas = []

    for reserva in reservas_solicitadas:
        if reserva in quartos_disponiveis:
            confirmadas.append(reserva)
            quartos_disponiveis.remove(reserva)
        else:
            recusadas.append(reserva)

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função principal
processar_reservas()
