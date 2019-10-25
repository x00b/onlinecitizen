from onctz.api.model.models import *
import onctz.api.model.models as modeller


class Model:
    def __init__(self, search_hash):
        self.search_hash = search_hash

    def arpenp_dao(self, cartorioRegistro, numeroCns, uf, nomeConjuge1, novoNomeConjuge1, nomeConjuge2, novoNomeConjuge2, dataCasamento, matricula, dataEntrada, dataRegistro, search_hash):
        self.data = modeller.Arpenp(cartorioRegistro, numeroCns, uf, nomeConjuge1, novoNomeConjuge1, nomeConjuge2, novoNomeConjuge2, dataCasamento, matricula, dataEntrada, dataRegistro, search_hash)

    def Cadesp(self, ie, cnpj, nomeEmpresarial, drt, situacao, dataInscricaoEstado, regimeEstadual, postoFiscal, search_hash):
        self.data = Cadesp(ie, cnpj, nomeEmpresarial, drt, situacao, dataInscricaoEstado, regimeEstadual, postoFiscal, search_hash)

    def Censec(self, carga, data, ato, data_ato, partes, search_hash):
        self.data = Censec(carga, data, ato, data_ato, partes, search_hash)
