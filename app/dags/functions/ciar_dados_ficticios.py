
# import sys
# sys.path.append(r'C:\Users\josec\Desktop\brasa_dados\local_airflow_python_mysql\temp_env\Lib\site-packages')
import pandas as pd
import os
def creates_dictionaries():
    '''
    Retorna um dicionário de listas em que o primeiro elemento da lista é um dicionário com dados fictícios de uma 
    entidade, e o segundo elemento é o nome do arquivo a ser salvo em formato CVS.
    '''

    clientes = {
        "cod_cliente": [1234567, 2345678, 3456789, 4567890, 5678901, 6789012, 7890123, 8901234, 9012345, 1122334,
                        2233445, 3344556, 4455667, 5566778, 6677889, 7788990, 8899001, 9900112, 1011123, 2122234,
                        3233345, 4344456, 5455567, 6566678, 7677789, 8788890, 9899001, 1000112, 1111223, 1222334],
        "nome": ["Carlos Silva", "Maria Oliveira", "João Santos", "Fernanda Costa", "Paulo Pereira", "Beatriz Gomes", 
                "Lucas Almeida", "Juliana Rocha", "Ana Lima", "Roberto Souza", "Paula Martins", "Ricardo Ribeiro", 
                "Gustavo Nunes", "Camila Cardoso", "Felipe Mendes", "Carla Ferreira", "Marcos Pinto", "Tatiane Alves", 
                "Ricardo Cruz", "Cláudia Silva", "Leandro Souza", "Juliana Gomes", "Arthur Rocha", "Aline Costa", 
                "Paulo Gomes", "Sabrina Santos", "Pedro Lima", "Verônica Rocha", "André Oliveira", "Mariana Pereira"],
        "idade": [28, 34, 45, 39, 23, 29, 31, 42, 35, 26, 38, 33, 30, 40, 41, 32, 27, 33, 36, 29, 37, 35, 33, 31, 29, 36, 25, 32, 39, 34],
        "bairro": ["Savassi", "Centro", "Funcionários", "Santa Efigênia", "Floresta", "Serra", "São Pedro", "Caiçara", "Lourdes", 
                "Anchieta", "Avenida do Contorno", "Sagrada Família", "Barro Preto", "Liberdade", "Pampulha", "Venda Nova", 
                "Jardim Canadá", "Boa Vista", "Buritis", "Gutierrez", "Belvedere", "Vila Clóris", "Jardim Montanhês", "Praia do Sol", 
                "Paquetá", "Nova Suíça", "Pilar", "Castelo", "Alto Barroca", "Carmo Sion"],
        "cidade": ["Belo Horizonte", "Belo Horizonte", "Belo Horizonte", "Belo Horizonte", "Belo Horizonte", "Belo Horizonte", 
                "Belo Horizonte", "Belo Horizonte", "Belo Horizonte", "Belo Horizonte", "Belo Horizonte", "Belo Horizonte", 
                "Belo Horizonte", "Belo Horizonte", "Belo Horizonte", "Belo Horizonte", "Belo Horizonte", "Belo Horizonte", 
                "Belo Horizonte", "Belo Horizonte", "Belo Horizonte", "Belo Horizonte", "Belo Horizonte", "Belo Horizonte", 
                "Belo Horizonte", "Belo Horizonte", "Belo Horizonte", "Belo Horizonte", "Belo Horizonte", "Belo Horizonte"],
        "data_nascimento": ["1980-01-15", "1991-05-23", "1979-09-10", "1985-12-07", "1997-02-18", "1996-04-03", "1994-03-15", 
                            "1983-11-20", "1987-05-25", "1994-01-11", "1990-07-29", "1984-09-05", "1992-12-15", "1982-10-03", 
                            "1980-07-20", "1981-06-11", "1988-09-01", "1995-02-28", "1986-11-10", "1994-04-16", "1989-01-13", 
                            "1987-08-25", "1989-03-14", "1986-04-07", "1992-06-18", "1995-10-03", "1991-08-02", "1992-02-22", 
                            "1985-05-09", "1987-06-30"],
        "contato": ["(31) 999x-8888", "(31) 98x5-4321", "(31) 98x6-5432", "(31) 977x5-4321", "(31) 96x54-3210", "(31) 9x3-2109",
                    "(31) 9x2-1098", "(31) 93x21-0987", "(31) 92x0-9876", "(31) 9x09-8765", "(31) 90x8-7654", "(31) 89x7-6543",
                    "(31) 88x6-5432", "(31) 87x5-4321", "(31) 86x4-3210", "(31) 855x3-2109", "(31) 8x32-1098", "(31) 8x321-0987",
                    "(31) 822x0-9876", "(31) 81x09-8765", "(31) 8x8-7654", "(31) 78x7-6543", "(31) 77x76-5432", "(31) 767x5-4321",
                    "(31) 75x54-3210", "(31) 74x43-2109", "(31) 73x32-1098", "(31) 72x21-0987", "(31) 7x10-9876", "(31) 712x0-9666"]
    }


    produtos = {
        "cod_produto": [1000001, 1000002, 1000003, 1000004, 1000005, 1000006, 1000007, 1000008, 1000009, 1000010,
                        1000011, 1000012, 1000013, 1000014, 1000015, 1000016, 1000017, 1000018, 1000019, 1000020,
                        1000021, 1000022, 1000023, 1000024, 1000025, 1000026, 1000027, 1000028, 1000029, 1000030,
                        1000031, 1000032, 1000033, 1000034, 1000035, 1000036, 1000037, 1000038, 1000039, 1000040,
                        1000041, 1000042, 1000043, 1000044, 1000045, 1000046, 1000047, 1000048, 1000049, 1000050],
        "nome": ["Tesoura", "Clipes", "Lápis Preto", "Caneta Azul", "Caderno Universitário", "Régua", "Marcador de Texto", 
                "Apontador", "Papel A4", "Fita Adesiva", "Papel Cartão", "Caderno Espiral", "Borracha", "Agulha de Costura", 
                "Post-it", "Papel Fotografico", "Pasta de Arquivo", "Envelope", "Papel Sulfite", "Caneta Esferográfica", 
                "Papel Colorido", "Bloco de Notas", "Lápis de Cor", "Canetinha", "Lápis Hidrocor", "Caneta Permanente", 
                "Fita Crepe", "Estilete", "Papel Vegetal", "Folha de papel Couche", "Caixa de lápis", "Caderno Costurado", 
                "Tesoura Escolar", "Clip de Papel", "Tesoura Infantil", "Apontador Elétrico", "Carimbo", "Papelão", 
                "Papel Carta", "Caneta Gel", "Lapiseira", "Pastas Suspensas", "Lixa de Unha", "Papel de Seda", 
                "Cartolina", "Caneta Marker", "Caderno de Desenho", "Caneta Colorida", "Bloco de Rascunho", "Régua de Metal"],
        "custo": [5.90, 1.50, 2.20, 4.00, 8.50, 3.00, 2.80, 1.70, 15.30, 3.50, 10.00, 6.00, 1.50, 7.20, 3.00, 8.90, 4.50, 
                12.50, 0.80, 1.20, 2.50, 1.00, 2.80, 6.00, 1.80, 3.00, 2.00, 3.20, 2.50, 5.30, 0.50, 8.00, 3.00, 1.60, 
                2.40, 5.50, 2.10, 4.20, 4.80, 6.90, 7.30, 10.20, 9.50, 2.90, 4.40, 5.60, 9.80, 6.70, 10.50, 3.10],
        "cod_fornecedor": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 
                        1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 
                        1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 
                        1046, 1047, 1048, 1049, 1050],
        "margem_lucro": [1.5, 2, 3, 1.5, 2, 3, 1.5, 2, 3, 1.5, 2, 3, 1.5, 2, 3, 
                        1.5, 2, 3, 1.5, 2, 3, 1.5, 2, 3, 1.5, 2, 3, 1.5, 2, 3, 
                        1.5, 2, 3, 1.5, 2, 3, 1.5, 2, 3, 1.5, 2, 3, 1.5, 2, 3, 
                        1.5, 2, 3, 1.5, 2,]
    }

    fornecedores = {
        "cod_fornecedor": [1001, 1002, 1003, 1004, 1005],
        "nome": ["Boa Vista Atacado", "Irmãos Santos", "Fornecedora Móveis", "Papers Ltda", "Papéis & Cia"],
        "prazo_entrega_dias": ["2025-01-20", "2025-01-18", "2025-01-25", "2025-01-15", "2025-01-22"],
        "UF": ["SP", "SP", "RJ", "MG", "SP"],
        "cidade": ["São Paulo", "São Paulo", "Rio de Janeiro", "Belo Horizonte", "São Paulo"],
        "bairro": ["Vila Progredior", "Itaim Bibi", "Botafogo", "Centro", "Moema"]
    }

    vendedores = {
        'cod_vendedor':[6258497,5263442,9998754,4568885,2316253,3330025,4500052,1055553,5204897,2223256,1155525,3250005],	
        'nome':['Monique Piva','Miriam Julia','Jozi Palhares','Icaro Mantra','Jose Silverio','Katia Gomes','Laura Piava','Paulo Silva','Paula Asme','Larissa Gusmao','Ines Honestaria','Guliver Bruno'],		
        'idade':[28,34,28,34,28,34,28,34,28,34,28,34],		
        'unidade':['Venda Nova','Centro','Venda Nova','Centro','Venda Nova','Centro','Venda Nova','Centro','Venda Nova','Centro','Venda Nova','Centro'],		
        'cidade':['Belo Horizonte','Belo Horizonte','Belo Horizonte','Belo Horizonte','Belo Horizonte','Belo Horizonte','Belo Horizonte','Belo Horizonte','Belo Horizonte','Belo Horizonte','Belo Horizonte','Belo Horizonte'],		
        'data_nascimento':['1980-01-15','1991-05-23','1980-01-15','1991-05-23','1980-01-15','1991-05-23','1980-01-15','1991-05-23','1980-01-15','1991-05-23','1980-01-15','1991-05-23'],		
        'data_contrato_ini':['2022-01-15','2023-05-23','2021-01-15','2023-05-23','2022-01-15','2021-05-23','2022-01-15','2023-05-23','2019-01-15','2021-05-23','2023-01-15','2022-05-23']
    }

    campanhas = {
        'unidade':['Centro','Venda Nova','Centro','Venda Nova'],
        'nome_campanha':['Aniversário','Compras acima de 100','Aniversário','Compras acima de 100'],
        'desc_campanha':['Cliente ganha desconto no mês de aniverário','Cliente ganha desconto em compras acima de 100 Reais','Cliente ganha desconto no mês de aniverário','Cliente ganha desconto em compras acima de 100 Reais'],
        'desconto':[0.2,0.1,0.2,0.1]
    }

    return {1:[clientes,'clientes.csv'], 
            2:[produtos,'produtos.csv'], 
            3:[fornecedores,'fornecedor.csv'], 
            4:[vendedores,'vendedores.csv'], 
            5:[campanhas,'campanhas.csv']}

def saves_csv_files(path:str):
    print(path,'##### log saves_csv_files 0')
    
    dataframes = creates_dictionaries()

    for file in list(dataframes.keys())[:]:
        df = pd.DataFrame(dataframes[file][0])
        print(dataframes[file][1],'##### log saves_csv_files 1')
        print(os.path.join(path,dataframes[file][1]),'##### log saves_csv_files 2')
        df.to_csv(os.path.join(path,dataframes[file][1]),encoding='latin1',sep=';',index=None)





