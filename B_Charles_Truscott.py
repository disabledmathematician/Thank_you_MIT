def Charles(L):
	l = L[0:len(L)//2]
	r = L[len(L)//2:len(L)]
	if len(L) == 2:
		print(L)
	else:
		Charles(l)
		Charles(r)
	
	

B = [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1]
print(len(B))
print(4 * 16)

if __name__ == "__main__": Charles(B)