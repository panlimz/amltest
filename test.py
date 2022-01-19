import pandas as pd

#Lendo o CSV e armazenando-o para consulta
data = pd.read_csv('src/202110_CPGF.csv', sep=';', encoding='latin-1', )


#Resolução da Questão "H"
orgname = data[(data['CÓDIGO ÓRGÃO'] == 20402)]
print('O órgão de código 20402 é:' )
print(orgname.head(1))


#Resolução da Questão "K"
#Listando todas as transações
transvaluelist = list(data['VALOR TRANSAÇÃO'])

#Alterando a vírgula do decimal em cada item da lista e os transformando em formato .float
for i in range(len(transvaluelist)):
    transvaluelist[i] = transvaluelist[i].replace(',', '.')
    transvaluelist[i] = float(transvaluelist[i])
#armazenando a soma de todos os valores em uma variável, e a formatando para mostrar 2 dígitos finais
sumtrans = sum(transvaluelist)
sumtrans = "{:.2f}".format(sumtrans)
print("A soma de todas as transações é:", sumtrans)


#Resolução da Questão "L, seguindo o mesmo parâmetro acima"
secrettrans = data[(data['NOME PORTADOR'] == 'Sigiloso')]
secrettranslist = list(secrettrans['VALOR TRANSAÇÃO'])
for i in range(len(secrettranslist)):
    secrettranslist[i] = secrettranslist[i].replace(',', '.')
    secrettranslist[i] = float(secrettranslist[i])
sumsectrans = sum(secrettranslist)
sumsectrans = "{:.2f}".format(sumsectrans)
print("A soma de todas as transações sigilosas é:", sumsectrans)


#Resolução da Questão "M"
#Organizando a base por nomes, e contando quantas linhas existem pra cada uma
secretnamesg = secrettrans.groupby(['NOME ÓRGÃO'])
namesocount = secretnamesg.count()
print(namesocount['VALOR TRANSAÇÃO'])
#Utilizando a mesma lógica acima para transformar cada transação em float e somando-as
poltrans = data[(data['NOME ÓRGÃO'] == 'Departamento de Polícia Federal')]
poltranslist = list(poltrans['VALOR TRANSAÇÃO'])
for i in range(len(poltranslist)):
    poltranslist[i] = poltranslist[i].replace(',', '.')
    poltranslist[i] = float(poltranslist[i])
sumpoltrans = sum(poltranslist)
sumpoltrans = "{:.2f}".format(sumpoltrans)
print("A soma de todas as transações sigilosas da Polícia é:", sumpoltrans)


#Resolução da Questão "N"
#Filtrando as transações que contém 'saque' e retornando as informações contadas
psaque = data[data['TRANSAÇÃO'].str.contains(r'SAQUE')]
people = psaque[['NOME PORTADOR','NOME ÓRGÃO']].value_counts()
print(people)
#Contando as transações do portador
maxsaq = data[data['NOME PORTADOR'] == 'RAFAEL FERREIRA COSTA']
rsaqlist = list(maxsaq['VALOR TRANSAÇÃO'])
for i in range(len(rsaqlist)):
    rsaqlist[i] = rsaqlist[i].replace(',', '.')
    rsaqlist[i] = float(rsaqlist[i])
sumsaqtrans = sum(rsaqlist)
sumsaqrans = "{:.2f}".format(sumsaqtrans)
print("A soma de todas as transações do portador é:", sumsaqtrans)


#Resolução da Questão "O"
#Filtrando as transações que contém 'comp' e retornando as informações contadas
pcomp = data[data['TRANSAÇÃO'].str.contains(r'COMP')] 
people = pcomp['NOME FAVORECIDO'].value_counts()
print(people)