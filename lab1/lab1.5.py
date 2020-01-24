def t():
	return 5/0

try:
	t()
except ZeroDivisionError:
	print ("division by zero!")
except Exception:
	print ('caught an Exception')
finally:
	print ('in filnally block for clearup')