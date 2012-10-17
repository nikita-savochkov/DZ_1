def gnome(massiv):
	index = 0
	flag = False
	assert len(massiv)>=2
		
	
	while True:
		if flag == False:
			while index < len(massiv):
				if index==len(massiv)-1:
					break
				if massiv[index] > massiv[index+1]:
					tmp=massiv[index]
					massiv[index]=massiv[index+1]
					massiv[index+1]=tmp
					if index > 0:
						index-=1
					flag = True
				else:
					if index < len(massiv):
						index+=1
		else:
			while index > 0:
				if index==len(massiv)-1:
					break
				if massiv[index] > massiv[index+1]:
					tmp=massiv[index]
					massiv[index]=massiv[index+1]
					massiv[index+1]=tmp
					if index > 0:
						index-=1
				else:
					if index < len(massiv):
						index+=1
					flag = False
					
		if index==len(massiv)-1:
			break
	return massiv
def test_gnome():
	assert gnome([8,1,3,4,1,8,2,5])==[1, 1, 2, 3, 4, 5, 8, 8]
	assert gnome([1,2,3])==[1,2,3]
	assert gnome([-1,-2,-3])==[-3,-2,-1]
	assert gnome([12,5])==[5,12]
	#assert readSimb([])==[] #Error
	assert gnome([0,0])==[0,0]
	assert gnome(["b","a"])==["a","b"]
	assert gnome(["cba","abc"])==["abc","cba"]
	assert gnome(["abd","abc"])==["abc","abd"]
	assert gnome(["abd",4])==[4,"abd"]
	assert gnome(["",4])==[4,""]
	assert gnome([4,False])==[False,4]
	assert gnome([True,False,True])==[False,True,True]
	
	print "OK!"
	
def main():
	test_gnome()
main()