def prefixToInfix(prefix):
	stack = []
	i = len(prefix) - 1
	while i >= 0:
		if not isOperator(prefix[i]):
			stack.append(prefix[i])
			i -= 1
		else:
			str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
			stack.append(str)
			i -= 1
	
	return stack.pop()

def isOperator(c):
	if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")" or c == "%":
		return True
	else:
		return False


if __name__=="__main__":
	str = "%*/*90-/50+23^1251520"
	val1 = prefixToInfix(str)
	print(val1)
	digit = int(val1)
	print(digit)
	
