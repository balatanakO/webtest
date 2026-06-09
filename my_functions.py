def add(a,b):
	"""返回a+b的结果"""
	return a + b

def check_even(n):
	"""如果n是偶数返回True，否则返回False"""
	return n % 2 == 0

def safe_divide(a, b):
	try:
		result = a / b
		return result
	except ZeroDivisionError:
		return None
