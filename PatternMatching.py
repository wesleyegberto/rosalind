#Pattern Matching Problem (http://rosalind.info/problems/1c/)
#input:
#ATAT
#GATATATGCATATACTT
#output:
#1 3 9

pattern = input();
text = input();

lenPat = len(pattern);

answer = [];

#count the pattern
answer = [str(i) for i in range(len(text)) if text[i:i + lenPat] == pattern];
print ' '.join(answer);
