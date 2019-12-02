import socket
import sys
import time
import dateutil.parser
import datetime
import numpy as np

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ("192.168.1.3", 5001)
client_address = ("192.168.1.2", 5001)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
i = 0
datetime.timedelta(0, 4, 316543)
time_arr = []
while len(time_arr) < 10000:
				data, address = sock.recvfrom(50)

				#start_time = datetime.datetime.now()
				#print(data)
				if len(data) > 30:
								end_time = datetime.datetime.now()
								arr = data.split('+')
								arr = arr[1].split(" ")
								time = datetime.datetime.strptime(arr[1], "%H:%M:%S.%f")
								#dateutil.parser.parse(arr[1])
								start_time = time 
								
								end_time = end_time.strftime('%H:%M:%S.%f')
								end_time  = datetime.datetime.strptime(end_time, "%H:%M:%S.%f")
								time = end_time - start_time
								#print((time.total_seconds() * 1000000))
								time_arr.append(time.total_seconds() * 1000000)
				i+=1


interval = max(time_arr)

num_split = 50

#print(time_arr)
num_bins = int(round(interval / num_split) + 1)

time_arr = np.sort(time_arr)

print(time_arr[int(round(len(time_arr)*0.99))])
print(time_arr[int(round(len(time_arr)*0.95))])
print(np.average(time_arr))

print(interval)
print(num_bins)

bucket = [0 for i in range(num_bins + 1)]

for delta in time_arr:
		index = int(delta/num_split)
		bucket[index] += 1

for item in bucket:
		print(item)
