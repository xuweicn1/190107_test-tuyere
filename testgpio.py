import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)


def fn_1(x,y):
    GPIO.output(18,1)
    print('正转到风口最大处...')
    time.sleep(x)
    GPIO.output(18,0)
    GPIO.output(23,1)
    print('反转缩小通风口...')
    time.sleep(y)
    GPIO.output(23,0)


if __name__ == '__main__':

    GPIO.output(18,0)
    GPIO.output(23,0)

    L = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    
    fn_1(53,L[9]*53)
    print("开口10%")
    time.sleep(2)
    
    fn_1(53,L[8]*53)
    print("开口20%")
    time.sleep(2)
    
    fn_1(53,L[7]*53)
    print("开口30%")
    time.sleep(2)
    
    fn_1(53,L[6]*53)
    print("开口40%")
    time.sleep(2)
    
    fn_1(53,L[5]*53)
    print("开口50%")
    time.sleep(2)
    
    fn_1(53,L[4]*53)
    print("开口60%")
    time.sleep(2)
    
    fn_1(53,L[3]*53)
    print("开口70%")
    time.sleep(2)
    
    fn_1(53,L[2]*53)
    print("开口80%")
    time.sleep(2)
    
    fn_1(53,L[1]*53)
    print("开口90%")
    time.sleep(2)
    
    fn_1(53,L[0]*53)
    print("开口100%")
    time.sleep(2)
    