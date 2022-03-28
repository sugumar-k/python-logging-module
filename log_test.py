import logging 

#now we will Create and configure logger 
logging.basicConfig(filename="log_test.log",
                    level=logging.DEBUG, 
					format='%(name)s|%(levelname)s |%(message)s|%(asctime)s',
					filemode='w',datefmt="%d-%m-%y %H-%M-%S") 
def log_test():
    logging.debug("this is a debug message")
    logging.info("this is a information message")
    logging.warning("this is a warning message")
    logging.error("this is a indication of error")
    logging.critical("something critical happened")
log_test()

import os
#reading the log file
file=open("log_test.log","r")
data=file.read()
#counting the occurence
def occurence(a,b):
    occurence_a=data.count(a)
    print("no of occurenceof" ,a,occurence_a)
    occurence_b=data.count(b)
    print("no of occurenceof ",b,occurence_b)
occurence("ERROR","WARNING")

#printing the required log level
file=open("log_test.log","r")
levelname="INFO"
for line in file:
	if levelname in line:
		print(line)