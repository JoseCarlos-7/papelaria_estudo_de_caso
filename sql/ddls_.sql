create table my_database.vendas_tb (
		lote_id varchar(10),
		data_venda datetime,
		cod_venda varchar(16),
		cod_venda_unidade varchar(16),
		cod_cliente varchar(10),
		cod_produto varchar(10),
		cod_fornecedor varchar(10),
		cod_vendedor varchar(10),
        quantidade int
)

create table my_database.produtos_tb (
cod_produto varchar(10),
nome varchar(50),
custo float,
cod_fornecedor varchar(10),
margem_lucro float
)

create table my_database.clientes_tb (
cod_cliente varchar(10),
nome varchar(50),
idade int,
bairro varchar(50),
cidade varchar(50),
data_nascimento datetime,
contato varchar(25)
)

create table my_database.fornecedores_tb (
cod_fornecedor varchar(50),
nome varchar(50),
prazo_entrega_dias int,
UF varchar(5),
cidade varchar(50),
bairro varchar(50)
)

create table my_database.vendedores_tb (
cod_vendedor varchar(50),
nome varchar(50),
idade int,
unidade varchar(50),
cidade varchar(50),
data_nascimento datetime,
data_contrato_ini datetime
)

create table my_database.calendario_tb (
data date, 
dia_da_semana varchar(50), 
mes int, 
nome_mes varchar(50), 
periodo_30_dias_ate_data varchar(50),
periodo_30_antes varchar(50), 
periodo_30_depois varchar(50)
)

create table my_database.campanhas_tb (
unidade varchar(50), 
nome_campanha varchar(50), 
desc_campanha varchar(100),
desconto float
)