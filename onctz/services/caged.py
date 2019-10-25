from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import onctz.api.model.models as modeller


class Caged:

    def __init__(self, browser, model):
        self.driver = browser.driver
        self.cagedresponsavel_data = None
        self.cagedempresa_data = None
        self.Model = model

    def login(self, login, password):
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='username']").send_keys(login)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='btn-submit']").click()

    def search_responsavel(self, chave):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//*[@id='j_idt12:lk_menu_consultas']")).perform()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='j_idt12:idMenuLinkAutorizado']").click()
        self.driver.find_element_by_xpath("//*[@id='formPesquisarAutorizado:slctTipoPesquisaAutorizado']")
        self.driver.find_element_by_xpath("//*[@id='formPesquisarAutorizado:slctTipoPesquisaAutorizado']/option[1]")
        self.driver.find_element_by_xpath("//*[@id='formPesquisarAutorizado:txtChavePesquisaAutorizado014']").send_keys(chave)
        self.driver.find_element_by_xpath("//*[@id='formPesquisarAutorizado:bt027_8']").click()

    def get_results_responsavel(self):
        cnpj_cpf = self.driver.find_element_by_xpath("//*[@id='txCnpj020_2']").text
        razao_social = self.driver.find_element_by_xpath("//*[@id='txtrazaosocial020_4']").text
        logradouro = self.driver.find_element_by_xpath("//*[@id='txt3_logradouro020']").text
        bairro = self.driver.find_element_by_xpath("//*[@id='txt4_bairro020']").text
        municipio = self.driver.find_element_by_xpath("//*[@id='conteudo']/fieldset[2]/div[3]/div/div[2]").text
        uf = self.driver.find_element_by_xpath("//*[@id='txt7_uf020']").text
        cep = self.driver.find_element_by_xpath("//*[@id='txt8_cep020']").text
        nome = self.driver.find_element_by_xpath("//*[@id='txt_nome_contato']").text
        cpf = self.driver.find_element_by_xpath("//*[@id='txt_contato_cpf']").text
        telefone = self.driver.find_element_by_xpath("//*[@id='conteudo']/fieldset[3]/div[3]/div[1]/div[2]").text
        email = self.driver.find_element_by_xpath("//*[@id='txt11_email']").text

        self.cagedresponsavel_data = modeller.CagedResponsavel(cnpj_cpf, razao_social, logradouro, bairro, municipio, uf,cep, nome, cpf, telefone, email, self.Model.search_hash)
        self.driver.quit()
        return self.cagedresponsavel_data

    def search_emp(self, cnpj):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//*[@id='j_idt12:lk_menu_consultas']")).perform()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='j_idt12:idMenuLinkEmpresaCaged']").click()
        self.driver.find_element_by_xpath("//*[@id='formPesquisarEmpresaCAGED:txtcnpjRaiz']").send_keys(cnpj)
        self.driver.find_element_by_xpath("//*[@id='formPesquisarEmpresaCAGED:btConsultar']").click()

    def get_results_emp(self):
        cnpj = self.driver.find_element_by_xpath("//*[@id='formResumoEmpresaCaged:txtCnpjRaiz']").text
        razao_social = self.driver.find_element_by_xpath("//*[@id='formResumoEmpresaCaged:txtRazaoSocial']").text
        cnae = self.driver.find_element_by_xpath("//*[@id='formResumoEmpresaCaged']/fieldset[1]/div[3]/div/div[2]").text
        num_filiais = self.driver.find_element_by_xpath("//*[@id='formResumoEmpresaCaged:txtNumFiliais']").text
        total_vinculos = self.driver.find_element_by_xpath("//*[@id='formResumoEmpresaCaged:txtTotalVinculos']").text
        desligamentos = self.driver.find_element_by_xpath("//*[@id='formResumoEmpresaCaged:txtTotalNumDesligamentos']").text

        self.cagedempresa_data = modeller.CagedEmpresa(cnpj, razao_social, cnae, num_filiais, total_vinculos, desligamentos, self.Model.search_hash)
        self.driver.quit()

        return self.cagedempresa_data

    def search_trab(self, chave):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//*[@id='j_idt12:lk_menu_consultas']")).perform()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='j_idt12:idMenuLinkTrabalhador']").click()
        self.driver.find_element_by_xpath("//*[@id='formPesquisarTrabalhador:slctTipoPesquisaTrabalhador']").click()
        self.driver.find_element_by_xpath("//*[@id='formPesquisarTrabalhador:slctTipoPesquisaTrabalhador']/option[1]").click()
        self.driver.find_element_by_xpath("//*[@id='formPesquisarTrabalhador:txtChavePesquisa']").send_keys(chave)
        self.driver.find_element_by_xpath("//*[@id='formPesquisarTrabalhador:submitPesqTrab']").click()

    def get_results_trab(self):
        nome = self.driver.find_element_by_xpath("//*[@id='txt2_Nome027']").text
        pis_base = self.driver.find_element_by_xpath("//*[@id='txt1_Pis028']").text
        pis_convertido = self.driver.find_element_by_xpath("//*[@id='txt1_elos028']").text
        cpf = self.driver.find_element_by_xpath("//*[@id='txt3_Cpf027']").text
        ctps = self.driver.find_element_by_xpath("//*[@id='txt5_Ctps027']").text
        situacao_pis = self.driver.find_element_by_xpath("//*[@id='txt4_SitPis027']").text
        nacionalidade = self.driver.find_element_by_xpath("//*[@id='conteudo']/fieldset[2]/div[4]/div[1]/div[2]").text
        grau_instrucao = self.driver.find_element_by_xpath("//*[@id='conteudo']/fieldset[2]/div[5]/div/div[2]").text
        pessoa_deficiencia = self.driver.find_element_by_xpath("//*[@id='conteudo']/fieldset[2]/div[6]/div[1]/div[2]").text
        nascimento = self.driver.find_element_by_xpath("//*[@id='conteudo']/fieldset[2]/div[1]/div[2]/div[2]").text
        uf_ctps = self.driver.find_element_by_xpath("//*[@id='txt6_ufctps027']").text
        sexo = self.driver.find_element_by_xpath("//*[@id='txt6_Sexo027']").text
        raca = self.driver.find_element_by_xpath("//*[@id='conteudo']/fieldset[2]/div[4]/div[2]/div[2]").text
        cep = self.driver.find_element_by_xpath("//*[@id='conteudo']/fieldset[2]/div[6]/div[2]/div[2]").text
        self.driver.find_element_by_xpath("//*[@id='HistoricoMov_Trabalhador_2:panelTabbedPane_resumo_trabalhador_2:movimentos_rais_caged_4']/div/a").click()
        print(nome)
        print(pis_base)
        print(pis_convertido)
        print(cpf)
        print(ctps)
        print(situacao_pis)
        print(nacionalidade)
        print(grau_instrucao)
        print(pessoa_deficiencia)
        print(nascimento)
        print(uf_ctps)
        print(sexo)
        print(raca)
        print(cep)

        sleep(5)
        self.driver.quit()
