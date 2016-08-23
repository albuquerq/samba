
import csv
import argparse
import json

parser = argparse.ArgumentParser(description='Carrega os dados do IBGE para o banco de dados de municípios do samba')
parser.add_argument('file', metavar='CSV_FILE', type=str, help='Caminho para o arquivo csv')

args = parser.parse_args()

attr = {
	'UF_COD': 0,
	'UF_NOME': 1,
	'MESOREGIAO_COD': 2,
	'MESOREGIAO_NOME': 3,
	'MICROREGIAO_COD': 4,
	'MICROREGIAO_NOME': 5,
	'MUNICIPIO_COD1': 6,
	'MUNICIPIO_COD2': 7,
	'MUNICIPIO_NOME':8,
}

if args.file:
	with open(args.file, encoding='utf-8') as csvfile:
		reader = csv.reader(csvfile)
		reader.__next__() #pula a primeira linha
		
		pk = 1
		pk_uf = 1
		municipios = []
		ufs = []
		ufs_map = {}

		for linha in reader:
			if not linha[attr['UF_NOME']] in ufs_map:
				uf = {
					'model': 'geo.UF',
					'pk': pk_uf,
					'fields': {
						'regiao': linha[attr['MESOREGIAO_NOME']],
						'nome': linha[attr['UF_NOME']],
					},
				}
				ufs.append(uf)
				ufs_map[linha[attr['UF_NOME']]] = pk_uf
				pk_uf += 1
				
			muni = {
				'model': 'geo.Municipio',
				'pk': pk, 
				'fields': {
					'nome': linha[attr['MUNICIPIO_NOME']],
					'descricao': 'Cidade de {}'.format(linha[attr['MUNICIPIO_NOME']]),
					'lat': 1.0,
					'lng': 1.0,
					'cod_ibge': linha[attr['MUNICIPIO_COD2']],
					'UF_id': ufs_map[linha[attr['UF_NOME']]]
				}
			}
			municipios.append(muni)
			pk += 1

		data = json.dumps(municipios+ufs)
		with open('initial_data.json', 'w') as file:
			file.write(data)

else:
	print("Passe um arquivo CSV válido!")