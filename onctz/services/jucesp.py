from time import sleep
import onctz.api.model.models as modeller


class Jucesp:

    def __init__(self, browser, model):
        self.driver = browser.driver
        self.Model = model

    def search(self, nomeEmp):
        self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmBuscaSimples_txtPalavraChave']").send_keys(nomeEmp)
        self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmBuscaSimples_pnlBuscaSimples']/table/tbody/tr/td[2]/input").click()
        Jucesp.captcha(self, "dsadsad")

    def get_results(self):
        self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_gdvResultadoBusca_gdvContent_ctl02_lbtSelecionar']").click()
        nome_emp = self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmPreVisualiza_lblEmpresa']").text
        tipo_emp = self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmPreVisualiza_lblDetalhes']").text
        data_constituicao = self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmPreVisualiza_lblConstituicao']").text
        data_inicio_atividade = self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmPreVisualiza_lblAtividade']").text
        cnpj = self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmPreVisualiza_lblCnpj']").text
        inscricao_estadual = self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmPreVisualiza_lblInscricao']").text
        objeto = self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmPreVisualiza_lblObjeto']").text
        capital = self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmPreVisualiza_lblCapital']").text
        logradouro = self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmPreVisualiza_lblLogradouro']").text
        bairro = self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmPreVisualiza_lblBairro']").text
        municipio = self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmPreVisualiza_lblMunicipio']").text
        numero = self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmPreVisualiza_lblNumero']").text
        complemento = self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmPreVisualiza_lblComplemento']").text
        cep = self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmPreVisualiza_lblCep']").text
        uf = self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmPreVisualiza_lblUf']").text

        self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmPreVisualiza_rblTipoDocumento_1']").click()
        self.driver.find_element_by_xpath("//*[@id='ctl00_cphContent_frmPreVisualiza_UpdatePanel2']/input").click()

        self.jucesp_data = modeller.Jucesp(nome_emp, tipo_emp, data_constituicao, data_inicio_atividade, cnpj, inscricao_estadual, objeto, capital, logradouro, bairro, municipio, numero, complemento, cep, uf, self.Model.search_hash)
        self.driver.quit()
        return self.jucesp_data

    def captcha(self, cod):
        self.driver.find_element_by_xpath("//*[@id='formBuscaAvancada']/table/tbody/tr[1]/td/div/div[2]/label/input").send_keys(cod)
        self.driver.find_element_by_xpath("//*[@id='formBuscaAvancada']/table/tbody/tr[2]/td/input").click()
