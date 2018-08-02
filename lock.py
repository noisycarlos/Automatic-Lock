import time
import RPi.GPIO as GPIO

pin_unlock = 23
pin_lock = 27
pin_door_mag = 22
pin_button = 17

def unlock(channel = 0):
    print 'Unlocking'
    GPIO.output(pin_unlock, 1)
    time.sleep(1)
    GPIO.output(pin_unlock, 0)
    return 'Door Unlocked'
def lock(channel = 0):
    print 'Locking'
    GPIO.output(pin_lock, 1)
    time.sleep(1)
    GPIO.output(pin_lock, 0)
    return 'Door Locked'
def close_all(channel = 0):
    GPIO.cleanup()
    exit()

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_lock, GPIO.OUT)
GPIO.setup(pin_unlock, GPIO.OUT)