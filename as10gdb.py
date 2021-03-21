import binascii
import _thread
import time
import socket
import psycopg2


HOST1 = '100.10.0.11'
HOST2 = '100.10.0.12'
PORT1 = 993
PORT2 = 994
PORTS1 = 881
PORTS2 = 883


#Database Connection
conn = psycopg2.connect(host="131.180.165.5",database="crpg", user="postgres", password="crpg")
conn.autocommit = True
cursor = conn.cursor()

# Define a function for the thread
def serverOne():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST1, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f,g,h = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g,
        		h
    		)

			cursor.execute(" INSERT INTO s10m1(dtime, cb_ctrl, cb_res, f_res, i_res, p_res, q_res, v_res) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", inserted_values)

			print("1")

def serverTwo():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST2, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f,g = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g
    		)

			cursor.execute(" INSERT INTO s10m2(dtime, cb_ctrl, cb_res, i_res, p_res, q_res, v_res) VALUES (%s,%s,%s,%s,%s,%s,%s)", inserted_values)

			print("2")


# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   _thread.start_new_thread( serverTwo, ( ) )

except:
   print ("Error: unable to start thread")

while 1:
   pass