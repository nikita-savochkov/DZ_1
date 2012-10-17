def delitel(num):
	if num<=0:
		print "this number can not be factored "+str(num)+""
		return []
	masiv=[]
	i=2
	tmp=num
	while i<=num/2:
		if tmp%i == 0:
			while True:
				if tmp%i==0:
					tmp=tmp/i
					masiv.append(i)
				else:
					break
		i+=1
	if len(masiv)==0:
		masiv.append(num)
	print masiv
	return masiv

def test_delitel():
	assert delitel(7) == [7]
	assert delitel(10) == [2,5]
	assert delitel(20) == [2,2,5]
	assert delitel(23) == [23]
	assert delitel(25) == [5,5]
	assert delitel(49) == [7,7]
	assert delitel(50) == [2,5,5]
	assert delitel(11*13)==[11,13]
	assert delitel(0) == []
	assert delitel(-134) == []
	print "OK!"

def main():
	test_delitel()

main()
