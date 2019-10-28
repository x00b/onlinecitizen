import onctz.api.model.models as modeller


class Util:
    def __init__(self):
        return

    def check_json(self, json):
        arpenp = None
        cadesp = None
        censec = None
        caged_resp = None
        caged_trab = None
        caged_emp = None
        detran_cnh = None
        infocrim = None
        jucesp = None
        siel = None

        try:
            arpenp = json.get('arpenp')
        except TypeError:
            pass
        except KeyError:
            pass

        try:
            cadesp = json.get('cadesp')
        except TypeError:
            pass
        except KeyError:
            pass

        try:
            caged_resp = json.get('caged_resp')
        except TypeError:
            pass
        except KeyError:
            pass

        try:
            caged_trab = json.get('caged_trab')
        except TypeError:
            pass
        except KeyError:
            pass

        try:
            caged_emp = json.get('caged_emp')
        except TypeError:
            pass
        except KeyError:
            pass

        try:
            censec = json.get('censec')
        except TypeError:
            pass
        except KeyError:
            pass

        try:
            detran_cnh = json.get('detran_cnh')
        except TypeError:
            pass
        except KeyError:
            pass

        try:
            infocrim = json.get('infocrim')
        except TypeError:
            pass
        except KeyError:
            pass

        try:
            jucesp = json.get('jucesp')
        except TypeError:
            pass
        except KeyError:
            pass

        try:
            siel = json.get('siel')
        except TypeError:
            pass
        except KeyError:
            pass

        return [arpenp, cadesp, caged_resp, caged_trab, caged_emp, censec, detran_cnh, infocrim, jucesp, siel]

    def format_export(self, hash):
        search_data = modeller.Search.query.filter_by(search_hash=hash).first()
        arpenp_data = modeller.Arpenp.query.filter_by(search_hash=hash).first()
        cadesp_data = modeller.Cadesp.query.filter_by(search_hash=hash).first()
        cagedresp_data = modeller.CagedResponsavel.query.filter_by(search_hash=hash).first()
        cagedtrab_data = modeller.CagedTrabalhador.query.filter_by(search_hash=hash).first()
        cagedemp_data = modeller.CagedEmpresa.query.filter_by(search_hash=hash).first()
        censec_data = modeller.Censec.query.filter_by(search_hash=hash).first()
        detrancnh_data = modeller.DetranCnh.query.filter_by(search_hash=hash).first()
        infocrim_data = modeller.Infocrim.query.filter_by(search_hash=hash).first()
        jucesp_data = modeller.Jucesp.query.filter_by(search_hash=hash).first()
        siel_data = modeller.Siel.query.filter_by(search_hash=hash).first()

        searchstruct = modeller.SearchStruct().dump(search_data)
        arpenpstruct = modeller.ArpenpStruct().dump(arpenp_data)
        cadespstruct = modeller.CadespStruct().dump(cadesp_data)
        cagedrespstruct = modeller.CagedResponsavelStruct().dump(cagedresp_data)
        cagedtrabstruct = modeller.CagedTrabalhadorStruct().dump(cagedtrab_data)
        cagedempstruct = modeller.CagedEmpresaStruct().dump(cagedemp_data)
        censecstruct = modeller.CensecStruct().dump(censec_data)
        detrancnhstruct = modeller.DetranCnhStruct().dump(detrancnh_data)
        infocrimstruct = modeller.InfocrimStruct().dump(infocrim_data)
        jucespstruct = modeller.JucespStruct().dump(jucesp_data)
        sielstruct = modeller.SielStruct().dump(siel_data)

        aux = dict(search=searchstruct, arpenp=arpenpstruct, cadesp=cadespstruct, caged_resp=cagedrespstruct, caged_trab=cagedtrabstruct, caged_emp=cagedempstruct, censec=censecstruct, detran_cnh=detrancnhstruct, infocrim=infocrimstruct, jucesp=jucespstruct, siel=sielstruct)
        search_result = modeller.ResultStruct().dump(aux)
        return search_result
