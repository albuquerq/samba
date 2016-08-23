# Documentação do Samba

## Organização da documentação

A pasta **diagrams** contêm os diagramas de modelagem da aplicação.\
A pasta **base_ibge** contêm arquivos de dados extraídos das bases do IBGE e scripts de conversão para formatos aceitos pelo Django.

## Ferramentas Utilizadas

* Diagramas: [Dia](https://sourceforge.net/projects/dia-installer/)

## Scripts

### make_initial_data.py

Gera um arquivo de inicialização que pode ser carregado pelo comando `python manage.py loaddata` seguido do nome do arquivo gerado.

cmd `$python make_initial_data.py`

```bash
	$python make_initial_data.py path/to/file.csv
```
> Use `python make_initial_data.py -h` para obter ajuda.
