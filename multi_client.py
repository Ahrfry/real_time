import socket
import sys
import time
from multiprocessing import Process, Value, Lock
import os
import datetime

num_threads = 2

def func(val, lock , port):
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
   
  t_end = time.time() + 5
  count_to = 200
  while True:
    for w in range(0 , count_to):
		  test = count_to*10
		  test = test / (count_to + 1)
    if time.time() >= t_end:
		  print(str(count))
		  count = 0
		  t_end = time.time() + 5
		  t  = datetime.datetime.now()
		  count_to -= 10
		  message  = message + t.strftime('%Y-%m-%d %H:%M:%S.%f')				
    else:
				message = "devideId:5001,temp:20,time+"
    sent = sock.sendto(message, server_address)
    count +=1
		
    """
		t  = datetime.now()
    message  = message + t.strftime('%Y-%m-%d %H:%M:%S.%f')
    """
    sent = sock.sendto(message, server_address)
    count += 1
    #message = "devideId:5001,temp:20,time+"
  print("count " + str(count))






if __name__ == "__main__": 
  
  v = Value('i', 0)
  lock = Lock()
  procs = []
  for i in range(0 , num_threads):
    port = 5001
    p = Process(target=func, args=(v, lock , port))
    procs.append(p)
  
  i = 0
  for p in procs: 
    p.start()
    os.system("taskset -p -c %d %d" % ((i % 4), p.pid))
    i += 1


# Receive response
#print >>sys.stderr, 'waiting to receive'
#data, server = sock.recvfrom(65000)
#print >>sys.stderr, 'received "%s"' % data

#print >>sys.stderr, 'closing socket'
