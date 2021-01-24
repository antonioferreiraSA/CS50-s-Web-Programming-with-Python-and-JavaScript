 def announce(f):
     def wrapper():
         print("About to ru the function..")
         f()
         print("Done with the function")