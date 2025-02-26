import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 23
ECHO = 24
print("Distance Measurement In progress")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
def get_distance():
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    while GPIO.input(ECHO) ==0:
        pulse_start_time = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = (pulse_duration * 34300) /2

    return distance
#SERVO
SERVO = 25
GPIO.setup(SERVO, GPIO.OUT)
pwm = GPIO.PWM(SERVO, 50)

def spin_servo(angle):
    duty_cycle = (angle / 18) +2
    GPIO.output(SERVO, True)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)
    GPIO.output(SERVO, False)
    pwm.ChangeDutyCycle(0)
while True:
    dist = get_distance()
    
    if dist > 5 and dist < 16:
        pwm.start(0)

        spin_servo(20)

        time.sleep(1)

        spin_servo(0)

        time.sleep(120)

    time.sleep(0.5)
