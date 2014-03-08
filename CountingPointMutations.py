#Counting Point Mutations (http://rosalind.info/problems/hamm/)
#input
#GAGCCTACTAACGGGAT
#CATCGTAATGACGGCCT
#output
#7

dna1 = raw_input();
dna2 = raw_input();

dH = 0; #Hamming distance

for i in range(len(dna1)):
	if dna1[i] != dna2[i]:
		dH += 1;

print dH;