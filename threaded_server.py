import socket
import sys
import time
import datetime
from multiprocessing import Process, Value, Lock 
import psutil
import os

count = 0
cpu_arr = []
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


server_address = ("192.168.1.3", 5001)
#Bind the socket to the port
sock.bind(server_address)

print >>sys.stderr, 'starting up on %s port %s' % server_address

def func(port, val , lock):
	count = 0	
	# Create a UDP/IP socket
	
	with lock:
        	val.value += 1	
	print("value " + str(val.value))	
	while val.value < 2:
		wut = 1
	print("started exec")	
	while True:
		data, address = sock.recvfrom(65000)
		count +=1
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
				print((time.total_seconds() * 1000000))
				#time_arr.append(time.total_seconds() * 1000)
		"""
		if count >=100000:
			cpu = psutil.cpu_percent(interval=1)	
			mem = psutil.virtual_memory()
			finish = datetime.now()
			total = finish - start
			print("Latency: " + str(total.microseconds) + " CPU " + str(cpu) + " mem " + str(mem.percent))			
			return
		"""
	print("count " + str(count))
	return	




if __name__ == "__main__": 
	latency = []	
	v = Value('i', 0)
	lock = Lock()
	procs = []
	
	#gen 5 processes
	for i in range(0 , 2):
		port = 5001
		procs.append(Process(target=func, args=(port , v , lock)))
	
	
	i = 2
	#start time right before starting the 5 threads
	for p in procs: 
		p.start()
		os.system("taskset -p -c %d %d" % (i, p.pid))
		i+= 1
	#for p in procs: p.join()
	#finish time right after last thread finishes
	
