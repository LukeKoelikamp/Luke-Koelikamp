from json import loads

def handle_response(message):
    print(message)
    messageValue = message
    return f'SQS sent \'{messageValue}\''
