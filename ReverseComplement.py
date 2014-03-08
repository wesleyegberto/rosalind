#Reverse Complement Problem (http://rosalind.info/problems/1b/) or #Complementing a Strand of DNA (http://rosalind.info/problems/revc/)
#input:
#AAAACCCGGT
#output:
#ACCGGGTTTT
#To exec use: python ReverseComplement.py < rosalind_1b.txt

text = str(raw_input());
reverse = "";

for n in text:
    #n = text[i:i + 1]
    if n == 'A':
        reverse = "T" + reverse;
    elif n == 'T':
        reverse = "A" + reverse;
    elif n == 'C':
        reverse = "G" + reverse;
    elif n == 'G':
        reverse = "C" + reverse;

print reverse;
