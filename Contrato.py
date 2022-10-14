massas = {
    'Base': 0.0,
    'Organica': 10.0}

molhos = {
    'Base': 0.0,
    'Organico': 5.0}

queijos = {
    'Sem queijo': 0.0,
    'Mussarela': 4.0,
    'Cheddar': 2.0}

coberturas = {
    'Base': 0.0,
    'Calabreza': 10.0,
    'Batata': 5.0,
    'Chocolate': 15.0}


def montar_calcular(massa ,molho ,queijo ,cobertura):
    """
    Recebe os ingredientes em string printa e retorna a pizza montada e seu valor de custo
    
    Lança exeção caso um dos valores não existam na base de dados

    :param massa: str
    :param molho: str
    :param queijo: str
    :param cobertura: str
    
    :return list pizza, float preco:

    """
    pizza = [massa, molho, queijo, cobertura]
    
    try:
        price1 = massas[massa]
        price2 = molhos[molho]
        price3 = queijos[queijo]
        price4 = coberturas[cobertura]
        
        preco = 25.0 + price1 + price2 + price3 + price4
    except:
        raise ValueError
        
    print(pizza)
    print(preco)
    
    return pizza, preco

montar_calcular('Base', 'Base', 'Cheddar', 'Batata')

def cadastrar(tipo, nome, preço):
    """
    Recebe as informações de um ingrediente e cadastra no banco de dados

    :param tipo: str
    :param nome: str
    :param preço: float
    
    """
    var = globals()[tipo]
    try:
        var[nome] = preço
    except:
        raise ValueError


def remover(tipo, nome):
    """
    Remove um ingrediente da base de dados
    
    Levanta exeção caso não exista tal ingrediente na base de dados
    
    :param tipo: str
    :param nome: str
    
    """
    var = globals()[tipo]
    try:
        var.pop(nome)
    except:
        raise ValueError

def listar():
    """
    Retorna a base de dados

    :return dict dados:
    
    """
    dicionario = {
        'Massas': massas,
        'Molhos': molhos,
        'Queijos': queijos,
        'Coberturas': coberturas}
    
    return dicionario

    