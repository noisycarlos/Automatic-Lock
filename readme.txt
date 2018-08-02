The Main Module is 'auto_lock.py'

Lock.py has the functions that control the lock itself via the relays.
You can use encrypt_command.py to encrypt commands into JWT. By default they expire after 10 seconds.

Additional Dependencies Installed:
pyjwt (just enter the next line into Raspberry Pi command line):
pip install pyjwt

If you get an error, because you don't have PIP, try this first:
sudo apt-get install python-pip

To Launch the Python script when the Raspberry Pi boots up you can follow this tutorial:
https://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/
