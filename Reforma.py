def __CalculaCustoSemDesconto(area: float, piso: str) -> float:
    """ Calcula o custo total da reforma sem considerar descontos """
    piso_lower = piso.lower()
    if piso_lower == "porcelanato":
        preco_por_metro_quadrado = 69.90 # em reais
        return preco_por_metro_quadrado * area

    if piso_lower == "madeira":
        preco_por_metro_quadrado = 50.00 # em reais
        return preco_por_metro_quadrado * area

    if piso_lower in {"cerâmica", "ceramica"}:
        preco_por_metro_quadrado = 43.20 # em reais
        return preco_por_metro_quadrado * area

    raise Exception("Tipo de piso inválido! Os tipos aceitos são: \"porcelanato\", \"madeira\" e \"cerâmica\"")

def CalculaDesconto(area: float, piso: str) -> float:
    """ Retorna o percentual de desconto a ser concedido """
    piso_lower = piso.lower()
    if piso_lower == "porcelanato" and area > 20:
        return 5/100 # 5%
    if piso_lower == "madeira" and area > 35:
        return 8/100 # 8%
    if piso_lower in {"cerâmica", "ceramica"} and area > 50:
        return 10/100 # 10%
    return 0/100 # nenhum desconto

def CalculaCusto(area: float, piso: str) -> float:
    """ Calcula o custo total da reforma """
    custo_base = __CalculaCustoSemDesconto(area, piso)
    desconto = CalculaDesconto(area, piso)
    return custo_base * (1 - desconto)
