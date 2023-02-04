import socket  # importing socket module to get the hostname or system name

from datetime import datetime  # importing datetime module to get the current datetime of the system


def my_brand():  # defining my_brand() function to accept assignment name as an argument
    res = "=*=*=*= " + socket.gethostname() + " =*=*=*=", \
          "=*=*=*= Course 2023S-SSW567-WS =*=*=*=", \
          "=*=*=*= Assignment Name:" + "HW 02a - Testing a legacy program and reporting on testing results" + " =*=*=*=", \
          "=*=*=*= Current date and time: " + current_date_time + " =*=*=*= "
    return res  # returning the result


#assign_name = input("Enter Assignment Name: ")  # To input the assignment name
current_date_time = datetime.now().strftime("%m-%d-%y %H:%M:%S")  # To get the current datetime from datetime module
print(my_brand())  # calling my_brand() function and printing the output to console
