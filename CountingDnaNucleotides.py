#Counting DNA Nucleotides (http://rosalind.info/problems/dna/)

dna = str(raw_input());

nucleotides = {}
nucleotides["A"] = 0;
nucleotides["C"] = 0;
nucleotides["G"] = 0;
nucleotides["T"] = 0;

for n in dna:
    nucleotides[n] = nucleotides[n] + 1;
    
print nucleotides["A"], nucleotides["C"], nucleotides["G"], nucleotides["T"]
