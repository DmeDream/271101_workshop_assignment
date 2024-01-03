import cv2
import mediapipe as mp
import time
import pyfirmata

time.sleep(2.0)

mp_draw=mp.solutions.drawing_utils #use function drawing_utils to draw straight connect landmark point
mp_hand=mp.solutions.hands #use function hands to find hand on camera


tipIds=[4,8,12,16,20] # media-pipe position  of fingertips

def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        # print("Input is an integer number. Number = ", val)
        bv = True
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            # print("Input is a float  number. Number = ", val)
            bv = True
        except ValueError:
            # print("No.. input is not a number. It's a string")
            bv = False
    return bv

cport = input('Enter the camera port: ')
while not (check_user_input(cport)):
    print('Please enter a number not string')
    cport = input('Enter the camera port: ')

comport = input('Enter the arduino board COM port: ')
while not (check_user_input(comport)):
    print('Please enter a number not string')
    comport = input('Enter the arduino board COM port: ')

board=pyfirmata.Arduino('COM'+comport)
led_1=board.get_pin('d:13:o') #Set pin to output
led_2=board.get_pin('d:12:o')
led_3=board.get_pin('d:11:o')
led_4=board.get_pin('d:10:o')
led_5=board.get_pin('d:9:o')

#### LED write function

## controller.py ##

def led(total,led_1,led_2,led_3,led_4,led_5):#creat condition to controll digital out put
    if total==0:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif total==1:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif total==2:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif total==3:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    elif total==4:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    elif total==5:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)



######



video=cv2.VideoCapture(int(cport)) #OpenCamera at index position 0

with mp_hand.Hands(min_detection_confidence=0.5,
               min_tracking_confidence=0.5) as hands:#(min_detection_confidence, min_tracking_confidence) are Value to considered for detect and tracking image
    while True:
        ret,image=video.read() #Read frame in camera video
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  #convert color BGR to RGB
        image.flags.writeable=False  #to improve nothing drawed in image
        results=hands.process(image) #process image
        image.flags.writeable=True #can drawing  image
        image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  #convert color RGB to BGR
        lmList=[]
        total = 0
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands=results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h,w,c=image.shape
                    cx,cy= int(lm.x*w), int(lm.y*h)
                    Nfing = 0
                    if id == 20:
                        id20 = int(id)
                        cx20 = cy
                    if id == 18:
                        id18 = int(id)
                        cx18 = cy
                    if id == 16:
                        id16 = int(id)
                        cx16 = cy
                    if id == 14:
                        id14 = int(id)
                        cx14 = cy
                    if id == 12:
                        id12 = int(id)
                        cx12 = cy
                    if id == 10:
                        id10 = int(id)
                        cx10 = cy
                    if id == 8:
                        id8 = int(id)
                        cx8 = cy
                    if id == 6:
                        id6 = int(id)
                        cx6 = cy
                    if id == 4:
                        id4 = int(id)
                        cx4 = cx
                    if id == 3:
                        id3 = int(id)
                        cx3 = cx
                finger = ["THUMB", "Index finger","Middle finger","Ring finger","Pinky Finger"]   
                if cx20 < cx18 :
                    cv2.putText(image, str(finger[4]),(50, 200), cv2.FONT_HERSHEY_PLAIN, 2.1,
                    (200, 160, 10), 2)
                    led_5.write(1)
                    Nfing = Nfing+1
                if cx16 < cx14:
                    cv2.putText(image, str(finger[3]),(50, 250 ), cv2.FONT_HERSHEY_PLAIN,2.1,
                    (160, 160, 20), 2)
                    led_4.write(1)
                    Nfing = Nfing+1
                if cx12 < cx10 :
                    cv2.putText(image, str(finger[2]),(50, 300), cv2.FONT_HERSHEY_PLAIN, 2.1,
                    (120, 160, 30), 2)
                    led_3.write(1)
                    Nfing = Nfing+1
                if cx8 < cx6 :
                    cv2.putText(image, str(finger[1]),(50, 350), cv2.FONT_HERSHEY_PLAIN, 2.1,
                    (80, 160, 40), 2)
                    led_2.write(1)
                    Nfing = Nfing+1
                cv2.putText(image, str(Nfing),(50, 450), cv2.FONT_HERSHEY_PLAIN, 2.1,
                      (40, 160, 50), 2)
                if cx4 > cx3:
                    cv2.putText(image, str(finger[0]),(50, 400), cv2.FONT_HERSHEY_PLAIN, 2.1,
                    (40, 160, 50), 2)
                    led_1.write(1)
                    Nfing = Nfing+1
                if cx20 > cx18 :
                    led_5.write(0)
                if cx16 > cx14:
                    led_4.write(0)
                if cx12 > cx10 :
                    led_3.write(0)
                if cx8 > cx6 :
                    led_2.write(0)
                if cx4 < cx3:                    
                    led_1.write(0)
                
                    
            


        cv2.imshow("Frame",image)  #show edited image
        k=cv2.waitKey(1)
        if k==ord('q'):  #press "q" to exit programe
            break
video.release()
cv2.destroyAllWindows()