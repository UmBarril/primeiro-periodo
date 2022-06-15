def CalculaCacheBanda(nome_banda, duracao):
    valorASerPago = 0
    nome_banda_lower = nome_banda.lower()
    if nome_banda_lower == "boneca de pano":
        valor_extra = 0
        MAX_TEMPO = 3
        if duracao > MAX_TEMPO:
            horas_extras = duracao - MAX_TEMPO
            valor_extra = 500 * horas_extras
        valorASerPago = 3700 + valor_extra

    elif nome_banda_lower == "calango doido":
        valor_extra = 0
        MAX_TEMPO = 4
        if duracao > MAX_TEMPO:
            horas_extras = duracao - MAX_TEMPO
            valor_extra = 700 * horas_extras
        valorASerPago = 5200 + valor_extra

    else:
        print("Erro! Insira as bandas \"boneca de pano\" ou \"calango doido\"")

    return valorASerPago