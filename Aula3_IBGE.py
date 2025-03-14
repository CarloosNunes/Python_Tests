import requests, json

nome = str(input("Insira um nome:"))

resultado = requests.get(f"https//servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}")

json_dados = json.loads(resultado.text)

print(json_dados[0]['res'][0])

