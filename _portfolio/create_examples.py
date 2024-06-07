import csv
import pandas as pd
from re import sub


def snake_case(s):
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
        sub('([A-Z]+)', r' \1',
        s.replace('-', ' '))).split()).lower()


def replace_in_file(file_path, item_dict):
    with open('example.md', 'r') as file:
        file_contents = file.read()
    file_contents = file_contents.replace("+++nome_item+++", str(item_dict["nome_item"]))
    file_contents = file_contents.replace("+++subtitle+++", str(item_dict["subtitle"]))
    file_contents = file_contents.replace("+++link_thumbnail+++", str(item_dict["link_imagem"]))
    file_contents = file_contents.replace("+++link_imagem+++", str(item_dict["link_imagem"]))
    file_contents = file_contents.replace("+++description+++", "NaN")
    file_contents = file_contents.replace("+++valor_original+++", str(item_dict["valor_original"]))
    file_contents = file_contents.replace("+++valor_pedido+++", str(item_dict["valor_pedido"]))
    file_contents = file_contents.replace("+++link_compra+++", str(item_dict["link_compra"]))
    file_contents = file_contents.replace("+++condition+++", str(item_dict["condition"]))
    file_contents = file_contents.replace("+++availability+++", str(item_dict["availability"]))
    file_contents = file_contents.replace("+++link_real_imagem+++", str(item_dict["link_real_imagem"]))

    with open(file_path, 'w') as file:
        file.write(file_contents)


filename = 'items.csv'
df = pd.read_csv(filename, sep='\t')


for row in df.iterrows():
    r = dict(row[1])
    replace_in_file(snake_case(str(r["valor_pedido"]) + "_" + r["nome_item"] + ".md"), r)
