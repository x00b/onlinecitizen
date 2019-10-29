from onctz.metadata import pilot, conf
from multiprocessing import Process


class Orchestrator:
    def __init__(self):
        self.pool = []
        return

    def define_services(self, services, search_hash):
        for i in range(len(pilot.services_list)):
            if services[i] is not None:
                self.service_thread(pilot.services_list[i], search_hash, services[i])

    def service_thread(self, service_name, search_hash, target):
        if service_name == 'arpenp':
            proc = Process(target=conf.engine.arpenp_search, args=(pilot, search_hash, target))
            self.pool.append(proc)
            proc.start()
        elif service_name == 'cadesp':
            proc = Process(target=conf.engine.cadesp_search, args=(pilot, search_hash, target))
            self.pool.append(proc)
            proc.start()
        elif service_name == 'caged_resp':
            proc = Process(target=conf.engine.cagedresp_search, args=(pilot, search_hash, target))
            self.pool.append(proc)
            proc.start()
        elif service_name == 'caged_trab':
            proc = Process(target=conf.engine.cagedtrab_search, args=(pilot, search_hash, target))
            self.pool.append(proc)
            proc.start()
        elif service_name == 'caged_emp':
            proc = Process(target=conf.engine.cagedemp_search, args=(pilot, search_hash, target))
            self.pool.append(proc)
            proc.start()
        elif service_name == 'censec':
            proc = Process(target=conf.engine.censec_search, args=(pilot, search_hash, target))
            self.pool.append(proc)
            proc.start()
        elif service_name == 'detran_cnh':
            proc = Process(target=conf.engine.detrancnh_search, args=(pilot, search_hash, target))
            self.pool.append(proc)
            proc.start()
        elif service_name == 'infocrim':
            proc = Process(target=conf.engine.infocrim_search, args=(pilot, search_hash))
            self.pool.append(proc)
            proc.start()
        elif service_name == 'jucesp':
            proc = Process(target=conf.engine.jucesp_search, args=(pilot, search_hash, target))
            self.pool.append(proc)
            proc.start()
        elif service_name == 'siel':
            proc = Process(target=conf.engine.siel_search, args=(pilot, search_hash, target))
            self.pool.append(proc)
            proc.start()
        elif service_name == 'sivec_nome':
            proc = Process(target=conf.engine.sivecnome_search, args=(pilot, search_hash, target))
            self.pool.append(proc)
            proc.start()
        elif service_name == 'sivec_sap':
            proc = Process(target=conf.engine.sivecsap_search, args=(pilot, search_hash, target))
            self.pool.append(proc)
            proc.start()
        elif service_name == 'arisp':
            proc = Process(target=conf.engine.arisp_search, args=(pilot, search_hash, target))
            self.pool.append(proc)
            proc.start()

    def conclude(self):
        for proc in self.pool:
            proc.join()
