import socket , pickle
import sys
import time
import signal
import datetime
import psutil
import os
import struct
import random
import dateutil.parser
count = 0

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("192.168.1.3", 5001)
client_address = ("192.168.1.2", 5001)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
count = 0

if __name__ == "__main__":
	
				port = int(sys.argv[3])
				
				t = []
				size = []
				j = 0
				i = int(sys.argv[1])
				count_to = int(sys.argv[2])
				message = "devideId:5001,temp:20,time+"
				count_arr = []
				count_arr.append(200)
				count_arr.append(10)
				count_arr.append(300)
				count_arr.append(50)
				count_arr.append(30)
				count_arr.append(100)
				c_index = 0;
				print(len(message))
				try:

								start  = datetime.datetime.now()
								t_end = time.time() + 1
								count_stamp = 0 
								while j <= i:
												
												for w in range(0 , count_to):
														test = count_to*10
														test = test / (count_to + 1)
												
												
												#start_time  = datetime.datetime.now()
												sent = sock.sendto(message, client_address)
												data, address = sock.recvfrom(50)
												#end_time = datetime.datetime.now()
												#time = end_time - start_time
												#print((time.total_seconds() * 1000000))

												j += 1
												count +=1
				except KeyboardInterrupt:
								finish = datetime.datetime.now()
								tot = finish - start 
								thru = j / tot.total_seconds()
								print("throuput " +  str(thru) + " count "  + str(j))
								# Receive response
								#print >>sys.stderr, 'waiting to receive'
								#data, server = sock.recvfrom(65000)
								#print >>sys.stderr, 'received "%s"' % data

								#print >>sys.stderr, 'closing socket'
				sock.close()

