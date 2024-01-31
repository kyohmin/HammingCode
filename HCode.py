# Recieve Correct input
def inputChecker():
    global inputNum
    global listNum
    global typeInput

    print("=================================\n")
    print("Choose the type of hamming Code\n\t1. Even Parity Code\n\t2. Odd Parity Code")
    typeInput = input("Your Choice : ")
    while not typeInput.isdigit() or int(typeInput) < 0 or int(typeInput) > 2:
        print("=================================\n")
        print("Choose the type of hamming Code\n\t1. Even Parity Code\n\t2. Odd Parity Code")
        print("====Entered Wrong Value, Please Try Again===")
        typeInput = input("Your Choice : ")

    inputNum = input("Enter the Binary Code : ")
    listNum = list(inputNum)
    while not inputNum.isdigit():
        print("\n=================================\n")
        print("====Entered Wrong Value, Please Try Again===")
        inputNum = input("Enter the Binary Code : ")
        listNum = list(inputNum)
    
    for i in range(2,10):   # Finds if there is # 2 - 9 in the list
        while str(i) in listNum:
            print("\n=================================\n")
            print("====Entered Wrong Value, Please Try Again===")
            inputNum = input("Enter the Binary Code : ")
            listNum = list(inputNum)
        
    print("=================================\n")

# Parity # Finder
def pFinder():
	global p
	p = 2 # Minimum # of parity

	while True:
		if ((2**p) - p - 1) >= len(inputNum):
			break

		p += 1
	return p

# Change list to String
def listToString(a):
    strVal = ''

    for i in a:
        strVal += i
    return strVal

# Inserts Trash Value for Calculation
def trashValInput():
	for i in range(1, p+1):
		if i == 1:
			listNum.append('4')
		else:
			d = 2**(i-1)
			d *= -1
			listNum[d+1:d] = '4'

# Calculates then changes to a digit according to needs
def digitChanger():
	global result
	for i in range(p):
		n = 2**i
		m = n
		r = n
		sumNum = 0
		for j in range(1, n+1):
			strValue = listNum[m*-1::r*-2]
			strValue = listToString(strValue)
			for o in strValue:
				sumNum += int(o)

			if n == j:
				if int(typeInput) == 1:
					if (sumNum % 2) == 0:
						listNum[n*-1] = '0'
					else:
						listNum[n*-1] = '1'
				elif int(typeInput) == 2:
					if (sumNum % 2) == 0:
						listNum[n*-1] = '1'
					else:
						listNum[n*-1] = '0'
			m += 1
	result = listToString(listNum)

# Main
def main():
	inputChecker()
	pFinder()
	trashValInput()
	digitChanger()
	print("Result : \n ", result)

# Program
main()