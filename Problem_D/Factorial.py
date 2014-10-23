def fact(n):
	answer = 1
	if n < 0 :
		raise Exception("Fail")
	else:
		for i in range(1, n+1):
			answer = i*answer
	return answer
	

print fact(0)
