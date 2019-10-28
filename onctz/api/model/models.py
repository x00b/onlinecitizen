from onctz.metadata import conf
from marshmallow import fields, Schema

db = conf.db
ma = conf.ma


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(600), nullable=False, unique=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'username')


class Search(db.Model):
    search_hash = db.Column(db.String(900), primary_key=True)
    alias = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(80), nullable=False)
    by_user = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __init__(self, search_hash, alias, status, date, by_user):
        self.search_hash = search_hash
        self.alias = alias
        self.status = status
        self.date = date
        self.by_user = by_user


class SearchSchema(ma.Schema):
    class Meta:
        fields = ('search_hash', 'alias', 'status', 'date', 'by_user')


class SearchStruct(Schema):
    search_hash = fields.Str()
    alias = fields.Str()
    status = fields.Int()
    date = fields.Str()
    by_user = fields.Str()


class ArpenpStruct(Schema):
    cartorioRegistro = fields.Str()
    numeroCns = fields.Str()
    uf = fields.Str()
    nomeConjuge1 = fields.Str()
    novoNomeConjuge1 = fields.Str()
    nomeConjuge2 = fields.Str()
    novoNomeConjuge2 = fields.Str()
    dataCasamento = fields.Str()
    dataEntrada = fields.Str()
    dataRegistro = fields.Str()


class CadespStruct(Schema):
    ie = fields.Str()
    cnpj = fields.Str()
    nomeEmpresarial = fields.Str()
    drt = fields.Str()
    situacao = fields.Str()
    dataInscricaoEstado = fields.Str()
    regimeEstadual = fields.Str()
    postoFiscal = fields.Str()


class CagedResponsavelStruct(Schema):
    cnpj_cpf = fields.Str()
    razao_social = fields.Str()
    logradouro = fields.Str()
    bairro = fields.Str()
    municipio = fields.Str()
    uf = fields.Str()
    cep = fields.Str()
    nome = fields.Str()
    cpf = fields.Str()
    telefone = fields.Str()
    email = fields.Str()


class CagedTrabalhadorStruct(Schema):
    nome = fields.Str()
    pis_base = fields.Str()
    pis_convertido = fields.Str()
    cpf = fields.Str()
    ctps = fields.Str()
    situacao_pis = fields.Str()
    nacionalidade = fields.Str()
    grau_instrucao = fields.Str()
    pessoa_deficiencia = fields.Str()
    nascimento = fields.Str()
    uf_ctps = fields.Str()
    sexo = fields.Str()
    raca = fields.Str()
    cep = fields.Str()


class CensecStruct(Schema):
    carga = fields.Str()
    data = fields.Str()
    ato = fields.Str()
    data_ato = fields.Str()
    partes = fields.Str()


class DetranCondutorStruct(Schema):
    relatorio = fields.Str()


class DetranCnhStruct(Schema):
    renach = fields.Str()
    categoria = fields.Str()
    emissao = fields.Str()
    nascimento = fields.Str()
    nome = fields.Str()
    identidade = fields.Str()
    cpf = fields.Str()
    nome_mae = fields.Str()
    nome_pai = fields.Str()
    registro = fields.Str()
    tipografico = fields.Str()


class InfocrimStruct(Schema):
    relatorio = fields.Str()


class JucespStruct(Schema):
    nome_emp = fields.Str()
    tipo_emp = fields.Str()
    data_constituicao = fields.Str()
    data_inicio_atividade = fields.Str()
    cnpj = fields.Str()
    inscricao_estadual = fields.Str()
    objeto = fields.Str()
    capital = fields.Str()
    logradouro = fields.Str()
    bairro = fields.Str()
    municipio = fields.Str()
    numero = fields.Str()
    complemento = fields.Str()
    cep = fields.Str()
    uf = fields.Str()


class ResultStruct(Schema):
    '''
      loading: Search database for search_hash in each of the tables; if not None:
      get result of each, generate struct(dump())
        infocrim = dict(relatorio=infocrim_data.relatorio)
	    schema = InfocrimStruct().dump(infocrim)
        and with each build the ResultStruct
        https://marshmallow.readthedocs.io/en/stable/quickstart.html#serializing-objects-dumping
        https://marshmallow.readthedocs.io/en/stable/quickstart.html#deserializing-objects-loading
    '''
    search = fields.Nested(SearchStruct())
    arpenp = fields.Nested(ArpenpStruct())
    cadesp = fields.Nested(CadespStruct())
    caged_resp = fields.Nested(CagedResponsavelStruct())
    caged_trab = fields.Nested(CagedTrabalhadorStruct())
    censec = fields.Nested(CensecStruct())
    detran_cnh = fields.Nested(DetranCnhStruct())
    infocrim = fields.Nested(InfocrimStruct())
    jucesp = fields.Nested(JucespStruct())


class ArispStruct(Schema):
    relatorio = fields.Str()


class Arisp(db.Model):
    arisp_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    relatorio = db.Column(db.String(1000))
    search_hash = db.Column(db.Integer, db.ForeignKey('search.search_hash'))

    def __init__(self, relatorio, search_hash):
        self.relatorio = relatorio
        self.search_hash = search_hash


class Arpenp(db.Model):
    arpenp_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cartorioRegistro = db.Column(db.String(200))
    numeroCns = db.Column(db.String(200))
    uf = db.Column(db.String(200))
    nomeConjuge1 = db.Column(db.String(200))
    novoNomeConjuge1 = db.Column(db.String(200))
    nomeConjuge2 = db.Column(db.String(200))
    novoNomeConjuge2 = db.Column(db.String(200))
    dataCasamento = db.Column(db.String(200))
    matricula = db.Column(db.String(200))
    dataEntrada = db.Column(db.String(200))
    dataRegistro = db.Column(db.String(200))
    search_hash = db.Column(db.Integer, db.ForeignKey('search.search_hash'))

    def __init__(self, cartorioRegistro, numeroCns, uf, nomeConjuge1, novoNomeConjuge1, nomeConjuge2, novoNomeConjuge2, dataCasamento, matricula, dataEntrada, dataRegistro, search_hash):
        self.cartorioRegistro = cartorioRegistro
        self.numeroCns = numeroCns
        self.uf = uf
        self.nomeConjuge1 = nomeConjuge1
        self.novoNomeConjuge1 = novoNomeConjuge1
        self.nomeConjuge2 = nomeConjuge2
        self.novoNomeConjuge2 = novoNomeConjuge2
        self.dataCasamento = dataCasamento
        self.dataEntrada = dataEntrada
        self.dataRegistro = dataRegistro
        self.search_hash = search_hash


class Cadesp(db.Model):
    cadesp_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ie = db.Column(db.String(200))
    cnpj = db.Column(db.String(200))
    nomeEmpresarial = db.Column(db.String(200))
    drt = db.Column(db.String(200))
    situacao = db.Column(db.String(200))
    dataInscricaoEstado = db.Column(db.String(200))
    regimeEstadual = db.Column(db.String(200))
    postoFiscal = db.Column(db.String(200))
    search_hash = db.Column(db.Integer, db.ForeignKey('search.search_hash'))

    def __init__(self, ie, cnpj, nomeEmpresarial, drt, situacao, dataInscricaoEstado, regimeEstadual, postoFiscal, search_hash):
        self.ie = ie
        self.cnpj = cnpj
        self.nomeEmpresarial = nomeEmpresarial
        self.drt = drt
        self.situacao = situacao
        self.dataInscricaoEstado = dataInscricaoEstado
        self.regimeEstadual = regimeEstadual
        self.postoFiscal = postoFiscal
        self.search_hash = search_hash


class CagedResponsavel(db.Model):
    caged_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cnpj_cpf = db.Column(db.String(200))
    razao_social = db.Column(db.String(200))
    logradouro = db.Column(db.String(200))
    bairro = db.Column(db.String(200))
    municipio = db.Column(db.String(200))
    uf = db.Column(db.String(200))
    cep = db.Column(db.String(200))
    nome = db.Column(db.String(200))
    cpf = db.Column(db.String(200))
    telefone = db.Column(db.String(200))
    email = db.Column(db.String(200))
    search_hash = db.Column(db.Integer, db.ForeignKey('search.search_hash'))

    def __init__(self, cnpj_cpf, razao_social, logradouro, bairro, municipio, uf, cep, nome, cpf, telefone, email, search_hash):
        self.cnpj_cpf = cnpj_cpf
        self.razao_social = razao_social
        self.logradouro = logradouro
        self.bairro = bairro
        self.municipio = municipio
        self.uf = uf
        self.cep = cep
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.search_hash = search_hash


class CagedEmpresaStruct(Schema):
    cnpj = fields.Str()
    razao_social = fields.Str()
    cnae = fields.Str()
    numero_filiais = fields.Str()
    total_vinculos = fields.Str()
    desligamentos = fields.Str()


class CagedEmpresa(db.Model):
    caged_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cnpj = db.Column(db.String(200))
    razao_social = db.Column(db.String(200))
    cnae = db.Column(db.String(200))
    numero_filiais = db.Column(db.String(200))
    total_vinculos = db.Column(db.String(200))
    desligamentos = db.Column(db.String(200))
    search_hash = db.Column(db.Integer, db.ForeignKey('search.search_hash'))

    def __init__(self, cnpj, razao_social, cnae, numero_filiais, total_vinculos, desligamentos, search_hash):
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.cnae = cnae
        self.numero_filiais = numero_filiais
        self.total_vinculos = total_vinculos
        self.desligamentos = desligamentos
        self.search_hash = search_hash


class CagedTrabalhador(db.Model):
    caged_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200))
    pis_base = db.Column(db.String(200))
    pis_convertido = db.Column(db.String(200))
    cpf = db.Column(db.String(200))
    ctps = db.Column(db.String(200))
    situacao_pis = db.Column(db.String(200))
    nacionalidade = db.Column(db.String(200))
    grau_instrucao = db.Column(db.String(200))
    pessoa_deficiencia = db.Column(db.String(200))
    nascimento = db.Column(db.String(200))
    uf_ctps = db.Column(db.String(200))
    sexo = db.Column(db.String(200))
    raca = db.Column(db.String(200))
    cep = db.Column(db.String(200))
    search_hash = db.Column(db.Integer, db.ForeignKey('search.search_hash'))

    def __init__(self, nome, pis_base, pis_convertido, cpf, ctps, situacao_pis, nacionalidade, grau_instrucao, pessoa_deficiencia, nascimento, uf_ctps, sexo, raca, cep, search_hash):
        self.nome = nome
        self.pis_base = pis_base
        self.pis_convertido = pis_convertido
        self.cpf = cpf
        self.ctps = ctps
        self.situacao_pis = situacao_pis
        self.nacionalidade = nacionalidade
        self.grau_instrucao = grau_instrucao
        self.pessoa_deficiencia = pessoa_deficiencia
        self.nascimento = nascimento
        self.uf_ctps = uf_ctps
        self.sexo = sexo
        self.raca = raca
        self.cep = cep
        self.search_hash = search_hash


class Censec(db.Model):
    censec_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    carga = db.Column(db.String(200))
    data = db.Column(db.String(200))
    ato = db.Column(db.String(200))
    data_ato = db.Column(db.String(200))
    partes = db.Column(db.String(200))
    search_hash = db.Column(db.Integer, db.ForeignKey('search.search_hash'))

    def __init__(self, carga, data, ato, data_ato, partes, search_hash):
        self.carga = carga
        self.data = data
        self.ato = ato
        self.data_ato = data_ato
        self.partes = partes
        self.search_hash = search_hash


class DetranCnh(db.Model):
    detran_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    renach = db.Column(db.String(200))
    categoria = db.Column(db.String(200))
    emissao = db.Column(db.String(200))
    nascimento = db.Column(db.String(200))
    nome = db.Column(db.String(200))
    identidade = db.Column(db.String(200))
    cpf = db.Column(db.String(200))
    nome_mae = db.Column(db.String(200))
    nome_pai = db.Column(db.String(200))
    registro = db.Column(db.String(200))
    tipografico = db.Column(db.String(200))
    search_hash = db.Column(db.Integer, db.ForeignKey('search.search_hash'))

    def __init__(self, renach, categoria, emissao, nascimento, nome, identidade, cpf, nome_mae, nome_pai, registro, tipografico, search_hash):
        self.renach = renach
        self.categoria = categoria
        self.emissao = emissao
        self.nascimento = nascimento
        self.nome = nome
        self.identidade = identidade
        self.cpf = cpf
        self.nome_mae = nome_mae
        self.nome_pai = nome_pai
        self.registro = registro
        self.tipografico = tipografico
        self.search_hash = search_hash

class DetranVeiculoStruct(Schema):
    relatorio = fields.Str()


class DetranVeiculo(db.Model):
    detran_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    relatorio = db.Column(db.String(1000))
    search_hash = db.Column(db.Integer, db.ForeignKey('search.search_hash'))

    def __init__(self, relatorio, search_hash):
        self.relatorio = relatorio
        self.search_hash = search_hash


class DetranCondutor(db.Model):
    detran_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    relatorio = db.Column(db.String(1000))
    search_hash = db.Column(db.Integer, db.ForeignKey('search.search_hash'))

    def __init__(self, relatorio, search_hash):
        self.relatorio = relatorio
        self.search_hash = search_hash


class Infocrim(db.Model):
    infocrim_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    relatorio = db.Column(db.String(1000))
    search_hash = db.Column(db.Integer, db.ForeignKey('search.search_hash'))

    def __init__(self, relatorio, search_hash):
        self.relatorio = relatorio
        self.search_hash = search_hash


class Jucesp(db.Model):
    jucesp_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_emp = db.Column(db.String(200))
    tipo_emp = db.Column(db.String(200))
    data_constituicao = db.Column(db.String(200))
    data_inicio_atividade = db.Column(db.String(200))
    cnpj = db.Column(db.String(200))
    inscricao_estadual = db.Column(db.String(200))
    objeto = db.Column(db.String(200))
    capital = db.Column(db.String(200))
    logradouro = db.Column(db.String(200))
    bairro = db.Column(db.String(200))
    municipio = db.Column(db.String(200))
    numero = db.Column(db.String(200))
    complemento = db.Column(db.String(200))
    cep = db.Column(db.String(200))
    uf = db.Column(db.String(200))
    search_hash = db.Column(db.Integer, db.ForeignKey('search.search_hash'))

    def __init__(self, nome_emp, tipo_emp, data_constituicao, data_inicio_atividade, cnpj, inscricao_estadual, objeto, capital, logradouro, bairro, municipio, numero, complemento, cep, uf, search_hash):
        self.nome_emp = nome_emp
        self.tipo_emp = tipo_emp
        self.data_constituicao = data_constituicao
        self.data_inicio_atividade = data_inicio_atividade
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual
        self.objeto = objeto
        self.capital = capital
        self.logradouro = logradouro
        self.bairro = bairro
        self.municipio = municipio
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.uf = uf
        self.search_hash = search_hash


class InfosegStruct(Schema):
    nome_rf = fields.Str()
    mae_rf = fields.Str()
    cpf_rf = fields.Str()
    nascimento_rf = fields.Str()
    municipio_rf = fields.Str()
    nome_renach = fields.Str()
    filiacao_renach = fields.Str()
    cpf_renach = fields.Str()
    nascimento_renach = fields.Str()
    categoria_renach = fields.Str()
    uf_renach = fields.Str()


class Infoseg(db.Model):
    infoseg_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_rf = db.Column(db.String(200))
    mae_rf = db.Column(db.String(200))
    cpf_rf = db.Column(db.String(200))
    nascimento_rf = db.Column(db.String(200))
    municipio_rf = db.Column(db.String(200))
    nome_renach = db.Column(db.String(200))
    filiacao_renach = db.Column(db.String(200))
    cpf_renach = db.Column(db.String(200))
    nascimento_renach = db.Column(db.String(200))
    categoria_renach = db.Column(db.String(200))
    uf_renach = db.Column(db.String(200))
    search_hash = db.Column(db.Integer, db.ForeignKey('search.search_hash'))

    def __init__(self, nome_rf, mae_rf, cpf_rf, nascimento_rf, municipio_rf, nome_renach, filiacao_renach, cpf_renach, nascimento_renach, categoria_renach, uf_renach, search_hash):
        self.nome_rf = nome_rf
        self.mae_rf = mae_rf
        self.cpf_rf = cpf_rf
        self.nascimento_rf = nascimento_rf
        self.municipio_rf = municipio_rf
        self.nome_renach = nome_renach
        self.filiacao_renach = filiacao_renach
        self.cpf_renach = cpf_renach
        self.nascimento_renach = nascimento_renach
        self.categoria_renach = categoria_renach
        self.uf_renach = uf_renach
        self.search_hash = search_hash

class SielStruct(Schema):
    nome = fields.Str()
    titulo = fields.Str()
    nascimento = fields.Str()
    zona = fields.Str()
    endereco = fields.Str()
    municipio = fields.Str()
    uf = fields.Str()
    data_domicilio = fields.Str()
    nome_pai = fields.Str()
    nome_mae = fields.Str()
    naturalidade = fields.Str()


class Siel(db.Model):
    siel_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200))
    titulo = db.Column(db.String(200))
    nascimento = db.Column(db.String(200))
    zona = db.Column(db.String(200))
    endereco = db.Column(db.String(200))
    municipio = db.Column(db.String(200))
    uf = db.Column(db.String(200))
    data_domicilio = db.Column(db.String(200))
    nome_pai = db.Column(db.String(200))
    nome_mae = db.Column(db.String(200))
    naturalidade = db.Column(db.String(200))
    search_hash = db.Column(db.Integer, db.ForeignKey('search.search_hash'))

    def __init__(self, nome, titulo, nascimento, zona, endereco, municipio, uf, data_domicilio, nome_pai, nome_mae, naturalidade, search_hash):
        self.nome = nome
        self.titulo = titulo
        self.nascimento = nascimento
        self.zona = zona
        self.endereco = endereco
        self.municipio = municipio
        self.uf = uf
        self.data_domicilio = data_domicilio
        self.nome_pai = nome_pai
        self.nome_mae = nome_mae
        self.naturalidade = naturalidade
        self.search_hash = search_hash


class SivecNomeStruct(Schema):
    nome = fields.Str()
    sexo = fields.Str()
    nascimento = fields.Str()
    rg = fields.Str()
    tipo_rg = fields.Str()
    alcunha = fields.Str()
    naturalidade = fields.Str()
    estado_civil = fields.Str()
    nome_mae = fields.Str()
    pele = fields.Str()
    profissao = fields.Str()
    naturalidade = fields.Str()
    naturalizado = fields.Str()
    endereco = fields.Str()


class SivecNome(db.Model):
    sivec_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200))
    sexo = db.Column(db.String(200))
    nascimento = db.Column(db.String(200))
    rg = db.Column(db.String(200))
    tipo_rg = db.Column(db.String(200))
    alcunha = db.Column(db.String(200))
    naturalidade = db.Column(db.String(200))
    estado_civil = db.Column(db.String(200))
    nome_mae = db.Column(db.String(200))
    pele = db.Column(db.String(200))
    profissao = db.Column(db.String(200))
    naturalidade = db.Column(db.String(200))
    naturalizado = db.Column(db.String(200))
    endereco = db.Column(db.String(200))
    search_hash = db.Column(db.Integer, db.ForeignKey('search.search_hash'))

    def __init__(self, nome, sexo, nascimento, rg, tipo_rg, alcunha, estado_civil, nome_mae, pele, profissao, naturalidade, naturalizado, endereco, search_hash):
        self.nome = nome
        self.sexo = sexo
        self.nascimento = nascimento
        self.rg = rg
        self.tipo_rg = tipo_rg
        self.alcunha = alcunha
        self.naturalidade = naturalidade
        self.estado_civil = estado_civil
        self.nome_mae = nome_mae
        self.pele = pele
        self.profissao = profissao
        self.naturalizado = naturalizado
        self.endereco = endereco
        self.search_hash = search_hash


class SivecSapStruct(Schema):
    nome = fields.Str()
    sexo = fields.Str()
    nascimento = fields.Str()
    rg = fields.Str()
    tipo_rg = fields.Str()
    alcunha = fields.Str()
    estado_civil = fields.Str()
    nome_mae = fields.Str()
    pele = fields.Str()
    profissao = fields.Str()
    naturalidade = fields.Str()
    naturalizado = fields.Str()
    endereco = fields.Str()


class SivecSap(db.Model):
    sivec_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200))
    sexo = db.Column(db.String(200))
    nascimento = db.Column(db.String(200))
    rg = db.Column(db.String(200))
    tipo_rg = db.Column(db.String(200))
    alcunha = db.Column(db.String(200))
    estado_civil = db.Column(db.String(200))
    nome_mae = db.Column(db.String(200))
    pele = db.Column(db.String(200))
    profissao = db.Column(db.String(200))
    naturalidade = db.Column(db.String(200))
    naturalizado = db.Column(db.String(200))
    endereco = db.Column(db.String(200))
    search_hash = db.Column(db.Integer, db.ForeignKey('search.search_hash'))

    def __init__(self, nome, sexo, nascimento, rg, tipo_rg, alcunha, estado_civil, nome_mae, pele, profissao, naturalidade, naturalizado, endereco, search_hash):
        self.nome = nome
        self.sexo = sexo
        self.nascimento = nascimento
        self.rg = rg
        self.tipo_rg = tipo_rg
        self.alcunha = alcunha
        self.naturalidade = naturalidade
        self.estado_civil = estado_civil
        self.nome_mae = nome_mae
        self.pele = pele
        self.profissao = profissao
        self.naturalizado = naturalizado
        self.endereco = endereco
        self.search_hash = search_hash
