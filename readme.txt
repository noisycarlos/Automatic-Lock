The Main Module is 'auto_lock.py'

Lock.py has the functions that control the lock itself via the relays.

You can use encrypt_commands.py to encrypt commands into JWT (Make sure the secret variable matches with the one in auto_lock.py).
JWTs expire after 10 seconds because they're supposed to be sent between machines. But you can change that by changing the 'seconds=10' to whatever you desire.
If you want to remove the expiration altogether, remove the following text from that line: 
'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=10)},

Additional Dependencies Installed:
pyjwt (just enter the next line into Raspberry Pi command line):
pip install pyjwt

If you get an error, because you don't have PIP, try this first:
sudo apt-get install python-pip

To Launch the Python script when the Raspberry Pi boots up you can follow this tutorial:
https://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/
