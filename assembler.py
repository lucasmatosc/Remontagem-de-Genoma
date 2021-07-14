# Crie um programa chamado Assembler capaz de remontar uma sequência genética
# a partir de um arquivo texto contendo os k-mers em ordem lexicográfica. A entrada será
# a saída do programa anterior (preâmbulo) e a saída será um arquivo FASTA como a
# sequencia remontada.

# Leitura do arquivo .txt com os k-mers
arq = open('k20mer.txt', 'r')
seqdiv = arq.read()
arq.close()
