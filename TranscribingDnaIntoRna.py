#Transcribing DNA into RNA (http://rosalind.info/problems/rna/)

dna = str(raw_input());
rna = [];

for n in dna:
    if n == 'T':
        rna.append('U');
    else:
        rna.append(n);
        
print ''.join(rna);
