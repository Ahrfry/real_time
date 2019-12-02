import socket
import sys
import time
from multiprocessing import Process, Value, Lock , Manager
import os
import datetime

num_threads = 2 

cli_time = []

tot_rcved = 0

def client(val, lock , port, time_cli):
				sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

				server_address = ("192.168.1.2", port)
				message = "devideId:5001,temp:20,time+"

				with lock:
						val.value += 1

				while val.value < num_threads:
						pass
		
		
				# Send data
				print >>sys.stderr, 'sending "%s"' % message
				count = 0
				
				tot_sent = 0
				t_end = time.time() + 2
				count_to = 0
				while tot_sent < 100000:
								for w in range(0 , count_to):
										test = count_to*10
										test = test / (count_to + 1)
								if time.time() >= t_end:
										print(str(count))
										count = 0
										t_end = time.time() + 2
										count_to = 0
								sent = sock.sendto(message, server_address)
								time_cli.append(1)
								count += 1
								tot_sent += 1
								#message = "devideId:5001,temp:20,time+"
				print("total sent " + str(len(time_cli)))
				return time_cli



def server(val , lock , port , time_svr):
				sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

				server_address = ("192.168.1.3", port)
				sock.bind(server_address)
				count = 0	
				# Create a UDP/IP socket

				with lock:
						val.value += 1	
				while val.value < 2:
						wut = 1
				
				while count < 100000:
						data, address = sock.recvfrom(65000)
						end_time = datetime.datetime.now()
						time_srv.append(end_time)
						count +=1
				print("total received " + str(len(time_srv)))
				return time_srv	




if __name__ == "__main__": 
  
				v = Value('i', 0)
				tot = 100000
				lock = Lock()
				procs = []
				with Manager() as manager:
								time_cli = manager.list()
								time_srv = manager.list()
								for i in range(0 , num_threads):
										port = 5001
										if i == 0:
												p = Process(target=client, args=(v, lock , port , time_cli))
										else:
												p = Process(target=server, args=(v, lock , port , time_srv))
										procs.append(p)
										p.start()
								
								i = 0
								for p in procs: 
										os.system("taskset -p -c %d %d" % ((i % 4), p.pid))
										i += 1
								
								for p in procs:
										p.join()
								print("cli size " +  str(len(time_cli)) + "srv size " +  str(len(time_srv)))

