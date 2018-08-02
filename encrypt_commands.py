#use this to encrypt the commands. Make sure the secrets match

import jwt, datetime

secret = 'abcdef123456789'

command = raw_input('Command: ')

result = jwt.encode({'command':command,'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=10)}, secret)
print(result)
