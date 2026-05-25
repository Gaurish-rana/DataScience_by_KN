import logging

# Configure Logging Setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H-%M-%S',
    force=True,
    handlers=[
        logging.FileHandler("app2.log"),
        logging.StreamHandler()
    ]
)


logger=logging.getLogger("Arithmethic App")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def subtract(a,b):
    result=a-b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def multiply(a,b):
    result=a*b
    logger.debug(f"Multiplying {a} x {b} = {result}")
    return result

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"Adding {a} + {b} = {result}")
        return result
    
    except ZeroDivisionError:
        logger.error("Division by Zero Error")
        return None
    

add(10,15)
subtract(15,10)
multiply(10,5)
divide(20,10)
divide(20,0)