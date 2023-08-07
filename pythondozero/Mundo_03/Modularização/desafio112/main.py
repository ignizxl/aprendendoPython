# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(), 
# mas com uma validação de dados para aceitar apenas valores que seja monetários.

from utilidadesCEV.moedas import resumo

from utilidadesCEV.dado import leiaDinheiro

preco = leiaDinheiro('Digite um preço: R$')
taxaDeAumento = int(input('Digite um taxa de aumento: '))
taxaDeReducao = int(input('Digite um taxa de redução: '))

resumo(preco, taxaDeAumento, taxaDeReducao)