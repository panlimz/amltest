# **Questionário AML Consulting**

## **Questões**

**A – Com suas palavras explique o que é lavagem de dinheiro.**
<br>**R.** É uma maneira de movimentar dinheiro de origem ilegal de forma que pareça ter origem legal. 

---

**B – O que é Cartão de Pagamento do Governo Federal (CPGF), e qual a sua finalidade.**
<br>**R.** É semelhante ao cartão de crédito de uma pessoa física, porém, destinado a uso do Governo e munido de regras e limites de uso específicos. Tem a finalidade de possibilitar ao servidor pagamentos de despesas próprias de forma mais eficiente e digital, substituindo os cheques. Essas despesas devem ser entendidas por suprimento de fundos (como compras de valor inferior a um limite pré-estabelecido, despesas que exijam pronto pagamento ou despesas em sigilo).

---

**C – Quem pode utilizar o CPGF?**
<br>**R.** Servidores representantes do Governo Federal com autorização a proceder execuções financeiras.

---

**D – Qual a URL onde é possível fazer o download dos arquivos do CPGF?**
<br>**R.** No [Portal da Transparência da Controladoria-geral da União](https://www.portaltransparencia.gov.br/download-de-dados).

---

**E – Qual a URL da paǵina com a descrição dos campos (ou dicionário de dados) da CPGF?**
<br>**R.** O [Dicionário de Dados - CPGF](https://www.portaldatransparencia.gov.br/pagina-interna/603393-dicionario-de-dados-cpgf) também está disponível no mesmo Portal da Transparência..

---

**F – É possível identificar o nome e o documento do portador do CPGF, em todas as movimentações ou há movimentações onde não é possível identificar o portador?**
<br>**R.** Há movimentações sem informações, em outras que são feitas em caráter de sigilo, portanto, há transações sem estes dados identificadores.

---

**G – É possível identificar o Órgão do portador do CPGF?**
<br>**R.** Sim, através do campo _"Nome Órgão Subordinado"_ que no caso é o nome do Órgão de onde pertence a unidade gestora que gerou o cartão. 

---

**H - Qual o nome do Órgão cujo código é 20402?**
<br>**R.** O nome do Órgão 20402 é Ministério da Ciência, Tecnologia, Inovações.

---

**I - É possível identificar o Nome e Documento (CNPJ) dos favorecidos pela utilização do CPGF?**
<br>**R.** Sim, através dos campos _"Nome Favorecido"_ e _"CNPJ ou CPF do Favorecido"_.

---

**J – É possível identificar a data e o valor das movimentações financeiras do CPGF, em todas as movimentações? Ou há movimentações onde não é possível identificar as datas e ou valores?**
<br>**R.** Há movimentações sigilosas em que estes dados não estão completos.

---

**K (código) – Qual a soma total das movimentações utilizando o CPGF?**
<br>**R.** Para o arquivo estudado, referente à Outubro de 2021, a soma das movimentações é R$ 5.619.007,95.

---

**L (código) – Qual a soma das movimentações sigilosas?**
<br>**R.** A soma das movimentações sigilosas é de R$ 3.108.731,15.

---

**M (código) – Qual o Órgão que mais realizou movimentações sigilosas no período e qual o valor (somado)?**
<br>**R.** O órgão que realizou mais movimentações sigilosas foi o Departamento de Polícia Federal, que somou 1327 transações e uma movimentação de R$1.348.380,04.

---

**N (código) – Qual o nome do portador que mais realizou saques no período? Qual a soma dos saques realizada por ele? Qual o nome do Órgão desse portador?**
<br>**R.** O portador que mais realizou saques foi RAFAEL FERREIRA COSTA, com 25 saques que totalizam R$24.520,00, pertencente ao órgão Instituto Chico Mendes de Conservação da Biodiversidade. 

---

**O (código) – Qual o nome do favorecido que mais recebeu compras realizadas utilizando o CPGF?**
<br>**R.** O favorecido conhecido que recebeu mais compras foi MERCADOPAGO.COM REPRESENTACOES LTDA., com 123 compras processadas. Acima dele, há transações de compra com a etiqueta "SEM INFORMAÇÃO", que somam 126 compras.

---

**P - Descreva qual a abordagem utilizada para desenvolver o código para os ítens de K a O.**
<br>**R.** Para a resolução das questões acima, utilizei a linguagem Python, em conjunto com a biblioteca Pandas. Essa biblioteca possibilita a manipulação de DataFrames de forma rápida e eficiente, com uma série de funções _built-in_.
<br>Algumas das referências e funções utilizadas foram:

- for -> estrutura de repetição, que repete uma ação sob determinada condição
- print() -> função que imprime um valor especificado na tela 
- pd.read_csv -> leitura do arquivo csv para manipulação
- df['Column'] -> sintaxe para referenciar uma coluna de um determinado DataFrame
- sum() -> função utilizada para somar itens de uma lista
- float() -> função para converter um dado para o formato float
- list() -> armazenar dados em lista
- .value_counts() -> função que conta os valores de um parâmetro especificado 
- .str.contains() -> função que busca por um valor 'string' dentro de um DataFrame especificado

Através delas, criei algumas variáveis e condições para visualizar os dados do banco de dados conforme a necessidade de cada exercício. Usando o banco principal como parâmetro, armazenando "novos" bancos a partir dele sob determinadas condições e exibindo as informações necessárias. 
<br>Como os filtros de dados podem ser feitos com funções pré-existentes, apenas utilizei os nomes das colunas como parâmetros, e algum critério de comparação onde foi necessário. Por exemplo: (data['CÓDIGO ÓRGÃO'] == 20402), onde busquei informações cujo código do órgão fosse compatível.
<br>Nos exercícios em que foi necessário somar as informações de transações, transformei os dados (que eram strings) em dados numéricos(neste caso, float) utilizando a estrutura de repetição for, para percorrer cada linha da lista necessária.

> Para completar este teste utilizei a documentação do [Pandas](https://pandas.pydata.org/docs/).
