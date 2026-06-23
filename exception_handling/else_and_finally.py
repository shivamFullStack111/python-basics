m = 4
n = 0

try:
    print(m/n)
    
except Exception as error:
    print(f"Error: {error}")
    
else:                           # Else runs if the exception block is not executed.                    
    print("No exception")     
    
finally:                        # Finally block always run
    print("code executed")      