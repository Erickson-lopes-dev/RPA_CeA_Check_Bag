import os

pasta = os.path.join(os.getcwd(), 'RPA_Selenium')

[print(arquivos) for diretorio, subpastas, arquivos in os.walk(pasta)]

# for diretorio, subpastas, arquivos in os.walk(pasta):
#     for arquivo in arquivos:
#         print(os.path.join(diretorio, arquivo))