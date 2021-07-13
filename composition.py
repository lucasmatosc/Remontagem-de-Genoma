# Crie um programa chamado kdMer. Tal programa tem como entrada uma sequencia
# genômica no formado FASTA, o tamanho da leitura (k) e a distância entre as leituras 
# (d). A partir desse programa, ele gera, em ordem lexicográfica o (k,d) mers, em um 
# arquivo texto. Supondo que k = 50 e d = 20, o arquivo de saída do programa será 
# k50d20mer.txt. A entrada deverá ter o seguinte formato:

# INPUT - arquivo fasta com o seguinte leiaut:
# >k=999d=999
# Sequencia de Nucleotideos
# OUTPUT – arquivo texto com os kdmers em ordem lexicográfica: 

#Leitura do arquivo .fasta 
arq = open('sequencia nucleotideos.txt', 'r')
sequencia = arq.read()
arq.close()

#Determinação do k
print("Digite um valor de k: ")
k = int(input())

dl1 = 0
dl2 = k

aux = ""
#Separação da sequência de acordo com o valor de k
for letter in range(len(sequencia)):
    aux = aux + (sequencia[dl1:dl2] + " ")
    dl1 = dl1 + k
    dl2 = dl2 + k

aux2 = aux.split()

#Ordenação em ordem lexicográfica 
kmers = sorted(aux2)

print(kmers)

#Escrita dos kmers no arquivo texto
arq2 = open('k20mer.txt', 'w')
arq2.write(str(kmers))
arq2.close()