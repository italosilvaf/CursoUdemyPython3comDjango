
import os
import shutil

caminho_original = r"C:\Users\Usuario\Pictures\Saved Pictures"
caminho_novo = r"C:\Users\Usuario\Pictures\Saved Pictures\Testes Python"

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')
    print()

for root, dirs, files, in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if '.jpg' or '.jepg' or '.png' in file:
            shutil.move(old_file_path, new_file_path)  # para copiar é so substituir "move" por "copy"
            print(f'Arquivo {file} copiado com sucesso.')





