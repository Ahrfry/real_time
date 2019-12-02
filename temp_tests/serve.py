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

if __name__ == "__main__": 

				i = 0
				datetime.timedelta(0, 4, 316543)
				time_arr = []
				tot_count = 0
				count_to = int(sys.argv[1])
				while tot_count < count_to:
								data, address = sock.recvfrom(50)

								#start_time = datetime.datetime.now()
								if len(data) >5:
												end_time = datetime.datetime.now()
												#data = data[(data.find("+") + 1) : -1]
												start_time = float(data) 
												end_time = end_time.strftime('%H:%M:%S.%f')
												end_time = float(end_time.split(":")[2])
												time = (end_time - start_time)*1000000
												print(str(time))
												time_arr.append((time))
												i+=1
												tot_count+=1;


				print("tot count " + str(tot_count))
				interval = max(time_arr)

				num_split = 50

				num_bins = int(round(interval / num_split) + 1)

				time_arr = np.sort(time_arr)

				#print(time_arr[int(round(len(time_arr)*0.99))])
				#print(time_arr[int(round(len(time_arr)*0.95))])
				#print(np.average(time_arr))

				#rint(interval)
				print(num_bins)

				bucket = [0 for i in range(num_bins + 3)]

				for delta in time_arr:
						index = int(delta/num_split)
						bucket[index] += 1

				for item in bucket:
						print(item)
