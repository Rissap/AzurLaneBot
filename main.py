import sys
import time

while True:
	try:
		import test_module
		print("done")
		time.sleep(1)
		del sys.modules["test_module"]
	except Exception as E:
		print(E)

	time.sleep(10)