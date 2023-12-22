#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp

Nfing = 5
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 5:
                    id5 = int(id)
                    cx5 = cx
                if id == 8:
                    id8 = int(id)
                    cy8 = cy
                if id == 7:
                    id7 = int(id)
                    cy7 = cy
                if id == 12:
                    id12 = int(id)
                    cy12 = cy
                if id == 11:
                    id11 = int(id)
                    cy11 = cy
                if id == 16:
                    id16 = int(id)
                    cy16 = cy
                if id == 15:
                    id15 = int(id)
                    cy15 = cy
                if id == 17:
                    id17 = int(id)
                    cx17 =cx
                if id == 19:
                    id19 = int(id)
                    cy19 = cy
                if id == 20:
                    id20 = int(id)
                    cy20 = cy
                    if cx5 > cx17: #Right
                        if  cy20 > cy19:
                            Nfing = 0
                        elif cy16 > cy15:
                            Nfing = 1
                        elif cy12 > cy11:
                            Nfing = 2
                        elif cy8 > cy7:
                          Nfing = 3
                        elif cx4 < cx3:
                          Nfing = 4
                        else:
                          Nfing = 5
                    else: #Left
                        if  cy20 > cy19:
                            Nfing = 0
                        elif cy16 > cy15:
                            Nfing = 1
                        elif cy12 > cy11:
                            Nfing = 2
                        elif cy8 > cy7:
                          Nfing = 3
                        elif cx4 > cx3:
                          Nfing = 4
                        else:
                          Nfing = 5

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.putText(img, str(int(Nfing)), (90, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()