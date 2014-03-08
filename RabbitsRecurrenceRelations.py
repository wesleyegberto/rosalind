#Rabbits and Recurrence Relations (http://rosalind.info/problems/fib/)

def fib(n, k):
	if n <= 0:
		return 0;
	if n == 1:
		return 1;
	# slower
	#tot = 0;
	#for j in range(k):
	#	tot += fib(n - 2, k);
	#tot += fib(n - 1, k);
	# faster
	return fib(n - 1, k) + (fib(n - 2, k) * k);

n = int(raw_input());
k = int(raw_input());
print fib(n, k);