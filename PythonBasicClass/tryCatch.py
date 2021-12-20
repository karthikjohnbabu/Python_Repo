try: #called to handle the risky or error prone code.
    with open('filelog.txt','r')as reader:
        reader.read()

except Exception as e: # called to handle the error message of the try block and the variable 'e' represents the error message by python
    print(e)

finally:
    print("Clear my browser cache, Clear my session ID, Clear my cookies")