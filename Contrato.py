massa = {
    'Base': 0.0,
    'Organica': 10.0}

molho = {
    'Base': 0,
    'Organico': 5.0}

queijo = {
    'Sem queijo': 0,
    'Mussarela': 4.0,
    'Cheddar': 2.0}

cobertura = {
    'Base': 0,
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
    pass

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
    pass

def listar():
    """
    Retorna a base de dados

    :return dict dados:
    
    """
    pass
    