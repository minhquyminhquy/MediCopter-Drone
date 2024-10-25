from gpiozero import Servo 
import time 
 
servo_pin1 = 17
servo_pin2 = 18  
servo1 = Servo(servo_pin1) 
servo2 = Servo(servo_pin2) 

def set_position_servo(): 
    pos =(180/180) * 2 - 1
    back_pos = (10/180) * 2 - 1
    servo1.value = back_pos  
    servo2.value = pos
    time.sleep(0.5) 
    servo1.value = pos
    servo2.value = back_pos 
    time.sleep(0.5) 

set_position_servo()
#servo1.detach()
#ervo2.detachriMA0"2 
