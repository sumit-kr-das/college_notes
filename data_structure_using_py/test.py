
def isOperand(x):
	return ((x >= 'a' and x <= 'z') or
			(x >= 'A' and x <= 'Z'))


def getInfix(exp) :
	s = []
	for i in exp:	
	
		# Push operands
		if (isOperand(i)) :		
			s.insert(0, i)

		else:
		
			op1 = s[0]
			s.pop(0)
			op2 = s[0]
			s.pop(0)
			s.insert(0, "(" + op2 + i +
							op1 + ")")
			

	return s[0]


if __name__ == '__main__':

	exp = "90-5023+/12^*5/15*20%"
	print(getInfix(exp.strip()))

