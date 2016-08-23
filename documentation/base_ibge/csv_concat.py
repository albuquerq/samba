

import argparse
import csv

parser = argparse.ArgumentParser(description='Carrega os dados do IBGE para o banco de dados de municípios do samba.')
parser.add_argument('file1', metavar='CSV_FILE1', type=str, help='Caminho para o arquivo csv com dados das cidades.')
parser.add_argument('file2', metavar='CSV_FILE2', type=str, help='Caminho para o arquivo csv com coordenadas das cidades.')

args = parser.parse_args()
print(args)

if args.file1 == '' or args.file2 == '':
	print('Erro, passe os nomes dos arquivos corretamente')

map_coords = {}

linha1 = None

with open(args.file2, encoding='utf-8') as file2:
	reader_coords = csv.reader(file2)
	linha1 = reader_coords.__next__()[1:]

	for record in reader_coords:
		map_coords[record[0]] = [record[1], record[2], record[3]]
	
saida = open('result.csv', 'w', encoding='utf-8')
wcsv = csv.writer(saida)

with open(args.file1, encoding='utf-8') as file1:
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

	reader = csv.reader(file1)

	linha1 = (reader.__next__() + linha1)
	wcsv.writerow(linha1)

	for row in reader:
		ext = map_coords.get(row[attr['MUNICIPIO_COD2']], [0,0,0])
		wcsv.writerow(row+ext)

