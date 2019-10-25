data = {
        "cartorioRegistro": "S\ufffdo Paulo - 8\ufffd Subdistrito - Santana",
        "dataCasamento": "19/03/2015",
        "dataEntrada": "23/03/2015",
        "dataRegistro": "19/03/2015",
        "nomeConjuge1": "Antonio TORRES Coutinho",
        "nomeConjuge2": "Ellen MARCIA FERNANDES SILVEIRA",
        "novoNomeConjuge1": "",
        "novoNomeConjuge2": "Ellen MARCIA FERNANDES SILVEIRA Coutinho",
        "numeroCns": "11914-9",
        "uf": "SP"
      }

template = (" \n"
            "        <article class=\"message\">\n"
            "        <div class=\"message-header\">\n"
            "          <p>Arpenp</p>\n"
            "        </div>\n"
            "        <div class=\"message-body\">\n"
            "          <ul>\n"
            "            <li>Registro cartório: {cartorioRegistro}</li>\n"
            "            <li>Numero CNS: {numeroCns}</li>\n"
            "            <li>UF: {uf}</li>\n"
            "            <li>Nome Conjuge1: {nomeConjuge1}</li>\n"
            "            <li>Novo Nome Conjuge1: {novoNomeConjuge1}</li>\n"
            "            <li>Nome Conjuge2: {nomeConjuge2}</li>\n"
            "            <li>Novo Nome Conjuge2: {novoNomeConjuge2}</li>\n"
            "            <li>Data Casamento: {dataCasamento}</li>\n"
            "            <li>Data Entrada: {dataEntrada}</li>\n"
            "            <li>Data Registro: {dataRegistro}</li>\n"
            "          </ul>\n"
            "        </div>\n"
            "      </article>").format(**data)

print(template)
