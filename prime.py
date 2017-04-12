import time
start_time = time.time()
i = 2
while(i < 1000000):
	j = 2
	while(j <= (i / j)):
		if not(i % j): break
		j = j + 1
	if (j > i / j) : print i, " is prime"
	i = i + 1
print ("The program execution time was %s seconds" % (time.time() - start_time))