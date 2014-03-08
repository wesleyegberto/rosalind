#Computing GC Content (http://rosalind.info/problems/gc/)
#input
#>Rosalind_6404
#CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
#TCCCACTAATAATTCTGAGG
#>Rosalind_5959
#CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
#ATATCCATTTGTCAGCAGACACGC
#>Rosalind_0808
#CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
#TGGGAACCTGCGGGCAGTAGGTGGAAT
#output
#Rosalind_0808
#60.919540

file = open("input.txt", "r");

dna = {}
prev = "";
for line in file.read().splitlines(): #does not take \n in line
	if line[0] == '>':
		prev = line[1:];
		dna[prev] = "";
	else:
		dna[prev] += line;

keyMax = "";
valMax = 0;

for key, val in dna.items():
	occur = 0.0;
	for n in val:
		if n == 'G' or n == 'C':
			occur += 1;
	dna[key] = occur / len(val) * 100;
	if(dna[key] > valMax):
		keyMax = key;
		valMax = dna[key];

print keyMax;
print valMax;
file.close();