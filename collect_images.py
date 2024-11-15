import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import os as oss
import traceback


capture = cv2.VideoCapture(1)
hd = HandDetector(maxHands=1)
hd2 = HandDetector(maxHands=1)

# Folder structure path for storing images
main_folder_path = "AtoZ_3.2"

# Start with character 'A'
c_dir = 'A'

# Set initial parameters
offset = 15
step = 1
flag = False
suv = 0

# Create a blank white image for drawing
white = np.ones((400, 400), np.uint8) * 255
cv2.imwrite("white.jpg", white)


# Function to check and create folder if it doesn't exist
def create_character_folder(character):
    char_folder_path = oss.path.join(main_folder_path, character)
    if not oss.path.exists(char_folder_path):
        oss.makedirs(char_folder_path)
    return char_folder_path


# Ensure initial directory exists and get image count
char_folder_path = create_character_folder(c_dir)
count = len(oss.listdir(char_folder_path))


while True:
    try:
        _, frame = capture.read()
        frame = cv2.flip(frame, 1)
        hands = hd.findHands(frame, draw=False, flipType=True)
        white = cv2.imread("white.jpg")

        if hands:
            hand = hands[0][0]
            x, y, w, h = hand['bbox']
            image = np.array(frame[y - offset:y + h + offset, x - offset:x + w + offset])

            handz, imz = hd2.findHands(image, draw=True, flipType=True)
            if handz:
                hand = handz[0]
                pts = hand['lmList']
                os = ((400 - w) // 2) - 15
                os1 = ((400 - h) // 2) - 15
                for t in range(0, 4, 1):
                    cv2.line(white, (pts[t][0] + os, pts[t][1] + os1), (pts[t + 1][0] + os, pts[t + 1][1] + os1), (0, 255, 0), 3)
                for t in range(5, 8, 1):
                    cv2.line(white, (pts[t][0] + os, pts[t][1] + os1), (pts[t + 1][0] + os, pts[t + 1][1] + os1), (0, 255, 0), 3)
                for t in range(9, 12, 1):
                    cv2.line(white, (pts[t][0] + os, pts[t][1] + os1), (pts[t + 1][0] + os, pts[t + 1][1] + os1), (0, 255, 0), 3)
                for t in range(13, 16, 1):
                    cv2.line(white, (pts[t][0] + os, pts[t][1] + os1), (pts[t + 1][0] + os, pts[t + 1][1] + os1), (0, 255, 0), 3)
                for t in range(17, 20, 1):
                    cv2.line(white, (pts[t][0] + os, pts[t][1] + os1), (pts[t + 1][0] + os, pts[t + 1][1] + os1), (0, 255, 0), 3)

                cv2.line(white, (pts[5][0] + os, pts[5][1] + os1), (pts[9][0] + os, pts[9][1] + os1), (0, 255, 0), 3)
                cv2.line(white, (pts[9][0] + os, pts[9][1] + os1), (pts[13][0] + os, pts[13][1] + os1), (0, 255, 0), 3)
                cv2.line(white, (pts[13][0] + os, pts[13][1] + os1), (pts[17][0] + os, pts[17][1] + os1), (0, 255, 0), 3)
                cv2.line(white, (pts[0][0] + os, pts[0][1] + os1), (pts[5][0] + os, pts[5][1] + os1), (0, 255, 0), 3)
                cv2.line(white, (pts[0][0] + os, pts[0][1] + os1), (pts[17][0] + os, pts[17][1] + os1), (0, 255, 0), 3)

                for i in range(21):
                    cv2.circle(white, (pts[i][0] + os, pts[i][1] + os1), 2, (0, 0, 255), 1)

                skeleton1 = np.array(white)
                cv2.imshow("1", skeleton1)

        frame = cv2.putText(frame, "dir=" + str(c_dir) + "  count=" + str(count), (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 1, cv2.LINE_AA)
        cv2.imshow("frame", frame)
        interrupt = cv2.waitKey(1)
        if interrupt & 0xFF == 27:
            # esc key
            break

        # Move to next character directory
        if interrupt & 0xFF == ord('n'):
            c_dir = chr(ord(c_dir) + 1)
            if ord(c_dir) == ord('Z') + 1:
                c_dir = 'A'
            flag = False
            # Check and create the next folder
            char_folder_path = create_character_folder(c_dir)
            count = len(oss.listdir(char_folder_path))

        # Toggle data capture
        if interrupt & 0xFF == ord('a'):
            flag = not flag
            suv = 0 if flag else suv

        print("=====", flag)
        if flag:

            if suv == 180:
                flag = False
            if step % 3 == 0:
                cv2.imwrite(oss.path.join(char_folder_path, f"{count}.jpg"), skeleton1)

                count += 1
                suv += 1
            step += 1

    except Exception:
        print("No Hand Detected!!")

capture.release()
cv2.destroyAllWindows()