#!/user/bin/env python3
from opcua import Client
from opcua import ua
import socket
import binascii
import _thread
import time
from datetime import datetime


HOST = ''
PORT1 = 991
PORT2 = 992
PORT3 = 993
PORT4 = 994


#OPC ACCESS
url = "opc.tcp://131.180.165.15:8899/freeopcua/server/"
client = Client(url)
client.connect()
print("connected to OPC UA Server")
val1 = client.get_node("ns=2;i=483")
val2 = client.get_node("ns=2;i=484")
val3 = client.get_node("ns=2;i=485")
val4 = client.get_node("ns=2;i=486")
val5 = client.get_node("ns=2;i=487")
val6 = client.get_node("ns=2;i=488")
val7 = client.get_node("ns=2;i=489")
val8 = client.get_node("ns=2;i=490")
val9 = client.get_node("ns=2;i=491")
val10 = client.get_node("ns=2;i=492")
val11 = client.get_node("ns=2;i=493")
val12 = client.get_node("ns=2;i=494")
val13 = client.get_node("ns=2;i=495")


# Define a function for the thread
def serverOne():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
		s1.bind(('',PORT1))
		s1.listen()
		conn1, addr = s1.accept()
		value=0
		with conn1:
			print('Server 1 from:',addr)
			while True:
				a = 1
				value = 2

				try: 
				#Update OPC value
					value1 = val1.get_value()
					value2 = val2.get_value()
					value3 = val3.get_value()
					value4 = val4.get_value()
					value5 = val5.get_value()
					value6 = val6.get_value()
					value7 = val7.get_value()
					value8 = val8.get_value()
					value9 = val9.get_value()
					value10 = val10.get_value()
					value11 = val11.get_value()
					value12 = val12.get_value()
					value13 = val13.get_value()
					dt = datetime.now()

					#covert inetger to string
					#stringd = str(value)

					stringd = str(dt)+"+"+str(value1)+"+"+str(value2)+"+"+str(value3)+"+"+str(value4)+"+"+str(value5)+"+"+str(value6)+"+"+str(value7)+"+"+str(value8)+"+"+str(value9)+"+"+str(value10)+"+"+str(value11)+"+"+str(value12)+"+"+str(value13)

					#convert string to bytes data
					data1 = stringd.encode()

					#send data back to client
					conn1.sendall(data1)

					#print('S1:',data1)
					time.sleep(1)

				except Exception:
						print("One")
						pass

				

# Define a function for the thread
def serverOneCC():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
		s1.bind(('',PORT3))
		s1.listen()
		conn1, addr = s1.accept()
		value=0
		with conn1:
			print('Server 1 from:',addr)
			while True:
				a = 1
				value = 2

				try:
					#Update OPC value
					value1 = val1.get_value()
					value2 = val2.get_value()
					value3 = val3.get_value()
					value4 = val4.get_value()
					value5 = val5.get_value()
					value6 = val6.get_value()
					value7 = val7.get_value()
					value8 = val8.get_value()
					value9 = val9.get_value()
					value10 = val10.get_value()
					value11 = val11.get_value()
					value12 = val12.get_value()
					value13 = val13.get_value()
					dt = datetime.now()

					#covert inetger to string
					#stringd = str(value)

					stringd = str(dt)+"+"+str(value1)+"+"+str(value2)+"+"+str(value3)+"+"+str(value4)+"+"+str(value5)+"+"+str(value6)+"+"+str(value7)+"+"+str(value8)+"+"+str(value9)+"+"+str(value10)+"+"+str(value11)+"+"+str(value12)+"+"+str(value13)


					#convert string to bytes data
					data1 = stringd.encode()

					#send data back to client
					conn1.sendall(data1)

					#print('S1:',data1)
					time.sleep(1)

				except Exception:
						print("OneCC")
						pass


# Define a function for the thread
def serverTwo():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.bind(('',PORT2))
		s2.listen()
		conn2, addr = s2.accept()
		valueb=0
		with conn2:
			print('Server 2 from:',addr)
			while True:
				b = 1
				value = 2
				data2 = conn2.recv(1024)
				data3 = data2.decode("utf-8")

				try: 
					a,b = data3.split("+")

					if '.' in b:
						value = float(b)
					else:
						value = int(b)
					check = int(a)
					if check == 483:
						val1.set_value(value, ua.VariantType.Int16)
						print('Value 483 set to:',value)
					elif check == 484:
						val2.set_value(value, ua.VariantType.Int16)
						print('Value 484 set to:',value)
					elif check == 485:
						val3.set_value(value, ua.VariantType.Float)
						print('Value 485 set to:',value)
					elif check == 486:
						val4.set_value(value, ua.VariantType.Float)
						print('Value 486 set to:',value)
					elif check == 487:
						val5.set_value(value, ua.VariantType.Float)
						print('Value 487 set to:',value)
					elif check == 488:
						val6.set_value(value, ua.VariantType.Float)
						print('Value 488 set to:',value)
					elif check == 489:
						val7.set_value(value, ua.VariantType.Float)
						print('Value 489 set to:',value)
					elif check == 490:
						val8.set_value(value, ua.VariantType.Float)
						print('Value 490 set to:',value)
					elif check == 491:
						val9.set_value(value, ua.VariantType.Int16)
						print('Value 491 set to:',value)
					elif check == 492:
						val10.set_value(value, ua.VariantType.Int16)
						print('Value 492 set to:',value)
					elif check == 493:
						val11.set_value(value, ua.VariantType.Int16)
						print('Value 493 set to:',value)
					elif check == 494:
						val12.set_value(value, ua.VariantType.Int16)
						print('Value 494 set to:',value)
					elif check == 495:
						val13.set_value(value, ua.VariantType.Float)
						print('Value 495 set to:',value)
					else:
							print(".")

				except Exception:
						print("Two")
						pass

def serverTwoCC():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.bind(('',PORT4))
		s2.listen()
		conn2, addr = s2.accept()
		valueb=0
		with conn2:
			print('Server 2 from:',addr)
			while True:
				b = 1
				value = 2
				data2 = conn2.recv(1024)
				data3 = data2.decode("utf-8")

				try:
					a,b = data3.split("+")

					if '.' in b:
						value = float(b)
					else:
						value = int(b)
					check = int(a)
					if check == 483:
						val1.set_value(value, ua.VariantType.Int16)
						print('Value 483 set to:',value)
					elif check == 484:
						val2.set_value(value, ua.VariantType.Int16)
						print('Value 484 set to:',value)
					elif check == 485:
						val3.set_value(value, ua.VariantType.Float)
						print('Value 485 set to:',value)
					elif check == 486:
						val4.set_value(value, ua.VariantType.Float)
						print('Value 486 set to:',value)
					elif check == 487:
						val5.set_value(value, ua.VariantType.Float)
						print('Value 487 set to:',value)
					elif check == 488:
						val6.set_value(value, ua.VariantType.Float)
						print('Value 488 set to:',value)
					elif check == 489:
						val7.set_value(value, ua.VariantType.Float)
						print('Value 489 set to:',value)
					elif check == 490:
						val8.set_value(value, ua.VariantType.Float)
						print('Value 490 set to:',value)
					elif check == 491:
						val9.set_value(value, ua.VariantType.Int16)
						print('Value 491 set to:',value)
					elif check == 492:
						val10.set_value(value, ua.VariantType.Int16)
						print('Value 492 set to:',value)
					elif check == 493:
						val11.set_value(value, ua.VariantType.Int16)
						print('Value 493 set to:',value)
					elif check == 494:
						val12.set_value(value, ua.VariantType.Int16)
						print('Value 494 set to:',value)
					elif check == 495:
						val13.set_value(value, ua.VariantType.Float)
						print('Value 495 set to:',value)
					else:
							print(".")

				except Exception:
						print("TwoCC")
						pass




# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   _thread.start_new_thread( serverOneCC, ( ) )
   _thread.start_new_thread( serverTwo, ( ) )
   _thread.start_new_thread( serverTwoCC, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass