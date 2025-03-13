import requests
from cliquentrega_app.location.models import Cidade


def handle():
    
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'
    response = requests.get(url)
    municipios = response.json()

    for municipio in municipios:
        nome = municipio['nome']
        estado = municipio['microrregiao']['mesorregiao']['UF']['sigla']
        valor = f"{nome.lower().replace(' ', '-')}-{estado.lower()}"
        label = f"{nome}-{estado}"

        Cidade.objects.get_or_create(
            nome=nome,
            estado=estado,
            defaults={'valor': valor, 'label': label}
        )
    print("automacao concluida com sucesso")
