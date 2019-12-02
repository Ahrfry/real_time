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
server_address = ("192.168.1.2", 5001)
sock.setblocking(0)
count = 0

if __name__ == "__main__":
	
				port = int(sys.argv[3])
				
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

								start = datetime.datetime.now()
								t_end = time.time() + 1
								count_stamp = 0 
								while j < i:
												for w in range(0 , count_to):
														test = count_to*10
														test = test / (count_to + 1)
												
												if time.time() >= t_end:
														print(str(count))
														count = 0
														#count_to = count_arr[c_index];
														c_index +=1
														if c_index > 4:
																c_index = 0
														t_end = time.time() + 0.01 
														t  = datetime.datetime.now()
														#count_to -= 10
														message  = message + t.strftime('%Y-%m-%d %H:%M:%S.%f')				
												else:
														message = "devideId:5001,temp:20,time+"
												
												#t  = datetime.datetime.now()
												#message  = message + t.strftime('%Y-%m-%d %H:%M:%S.%f')				
												sent = sock.sendto(message, server_address)
												
												message = "devideId:5001,temp:20,time+"
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

