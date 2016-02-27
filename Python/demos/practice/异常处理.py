#! /usr/bin/python
s=input("Input your age:")
if s =="":
    raise Exception("Input must no be empty.")

try:
    i=int(s)
except Exception as err:
    print(err)
finally: # Clean up action
    print("Goodbye!")
