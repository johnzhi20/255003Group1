import time
def doeswork():
	# Example work: sum numbers from 1 to 1000000
	total = 0
	for i in range(1, 1000001):
		total += i
	return total

start = time.time()
doeswork()
end = time.time()
elapsed = end - start
print(f"Elapsed time: {elapsed:.6f} seconds")