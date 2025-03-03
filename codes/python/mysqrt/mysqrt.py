x=2.0
s=1.0
kmax=15
for i in range(kmax):
	s=0.5*(s+(x/s))
print(s)