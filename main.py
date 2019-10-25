from configparser import ConfigParser
from onctz.api.app import run_api

config = ConfigParser()
config.read('conf.ini')
"""for key in config['LOGIN']:
    print(key, "= ", config['LOGIN'][key])
"""

run_api()


# pilot.arisp('144.854.658.56')
# pilot.arpenp('985565284')
# pilot.cadesp('1484894984949')
# pilot.censec('144.854.658.56')
# pilot.sivec_nome('pedro')
# pilot.sivec_sap('12345')
# pilot.infocrim()
# pilot.siel('pedro', '21314')
# pilot.jucesp('dasidjsa')
# pilot.detran_condutor('144.854.658.56')
# pilot.detran_veiculo('144.854.658.56', 'pxyz')
# pilot.detran_cnh('144.854.658.56')
# pilot.infoseg('144.854.658.56') # nao testado
# pilot.caged_responsavel("23918329108")
# pilot.caged_empresa("213132322131")
# pilot.caged_trabalhador("32131321")
# pilot.google('pedro')
# sleep(4)

