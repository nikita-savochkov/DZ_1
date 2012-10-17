def fun(str):
	strres = ""
	tmpsym = ""
	flag = False
	for sym in str:
		if tmpsym != sym:
			tmpsym = sym
			flag = True
		elif flag == True:
			flag = False
			if sym == '#':
				assert len(strres) != 0
				strres = strres + strres[-1]
			else:
				strres += sym
	print strres
	return strres

def main():
	#fun("##")
	fun("122345667889")
	fun("123334456")
	fun("111###2222222344##")

main()
