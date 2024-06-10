import csv
import pandas as pd
from re import sub
import os


def snake_case(s):
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
        sub('([A-Z]+)', r' \1',
        s.replace('-', ' '))).split()).lower()


def delete_markdown_files():
    # Get the current working directory
    current_dir = os.getcwd()

    # List all files in the current directory
    for filename in os.listdir(current_dir):
        # Check if the file ends with '.md'
        if filename.endswith('.md'):
            # Construct full file path
            file_path = os.path.join(current_dir, filename)
            try:
                # Remove the file
                os.remove(file_path)
            except Exception as e:
                print(f"Failed to delete {filename}: {e}")


def replace_in_file(file_path, item_dict):
    with open('../example.md', 'r') as file:
        file_contents = file.read()
    file_contents = file_contents.replace("+++nome_item+++", str(item_dict["nome_item"]))
    file_contents = file_contents.replace("+++subtitle+++", str(item_dict["subtitle"]))
    file_contents = file_contents.replace("+++link_thumbnail+++", str(item_dict["link_imagem"]))
    file_contents = file_contents.replace("+++link_imagem+++", str(item_dict["link_imagem"]))
    file_contents = file_contents.replace("+++valor_original+++", str(item_dict["valor_original"]))
    file_contents = file_contents.replace("+++valor_pedido+++", str(item_dict["valor_pedido"]))
    file_contents = file_contents.replace("+++link_compra+++", str(item_dict["link_compra"]))
    file_contents = file_contents.replace("+++condition+++", str(item_dict["condition"]))

    availability = str(item_dict["availability"])
    file_contents = file_contents.replace("+++availability_yes_or_no+++", availability)

    text_availability = "<span style='color:red'>Oops, this one is taken! ❌</span>"
    if availability == "Yes":
        text_availability = "<span style='color:green'>Yes, it's still available! ✅</span>"
    file_contents = file_contents.replace("+++availability+++", text_availability)

    file_contents = file_contents.replace("+++link_real_imagem+++", str(item_dict["link_real_imagem"]))

    with open(file_path, 'w') as file:
        file.write(file_contents)


def create_markdowns(csv_file_name="items.csv"):
    df = pd.read_csv(csv_file_name, sep='\t')

    for row in df.iterrows():
        r = dict(row[1])
        s = ""
        if r["availability"] == "Yes":
            s = s + "avail_"
        else:
            s = s + "sold_"
        s = s + snake_case(str(10000-r["valor_pedido"]).rjust(5, "0") + "_" + r["nome_item"] + ".md")
        replace_in_file(s, r)


if __name__ == "__main__":
    delete_markdown_files()
    create_markdowns()
