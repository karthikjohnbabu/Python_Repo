import logging
logging.basicConfig(filename='log.txt',level=logging.INFO,
                    format='%(asctime)s: %(levelname)s')
logging.info('A new request came')
try:
    x=int(input('Enter first number:'))
    y=int(input('Enter second number:'))
    print('The result is :',x/y)
except ZeroDivisionError as msg:
    print('Cannot divide with Zero')
    logging.exception(msg)
except ValueError as msg:
    print('Provide int values only')
    logging.exception(msg)
logging.info('Request completed')