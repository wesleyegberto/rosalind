#Frequent Words Problem (http://rosalind.info/problems/1a/)
#Input:
#ACGTTGCATGTCGCATGATGCATGAGAGCT
#4
#Output:
#CATG GCAT
#To exec use: python FindKmers.py < rosalind_1a.txt

text = str(input());
k = int(input());
size = len(text);

kmers = {}; # Dictionary to kmers - frequency

for i in range(size - k + 1):
    item = text[i:i + k];
    if item in kmers:
        kmers[item] += 1;
    else:
        kmers[item] = 1;

maxOccur = max(kmers.values()); #gets the highest value of dictonary

#The following code can be change to: answer = [kmer for kmer, freq in kmers.items() if freq == maxOccur]; print ' '.join(answer);
answer = "";
for key, value in kmers.items():
    if value == maxOccur:
        answer += key + " ";
        
print answer;
