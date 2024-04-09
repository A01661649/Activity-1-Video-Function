import cv2
import os

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter('actividad.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))
while True:
    ret, frame = cap.read()
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
    writer.write(frame)
    cv2.imshow('frame', frame)

cap.release()
writer.release()
cv2.destroyAllWindows()

reversa = cv2.VideoCapture('actividad.mp4')

check, vid = reversa.read()
frame_list = []
while(check == True):
    check, vid = reversa.read()
    frame_list.append(vid)
frame_list.pop()
frame_list.reverse()

for frame in frame_list:
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break

width = int(reversa.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(reversa.get(cv2.CAP_PROP_FRAME_HEIGHT))
video = cv2.VideoWriter('actividad_reversa.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))

for i in range (0, len(frame_list)):
    video.write(frame_list[i])


reversa.release()
video.release()
cv2.destroyAllWindows()

ambos = cv2.VideoWriter('actividad_ambos.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))

long = len(frame_list)

for i in range(long// 2):
    frame_list[i], frame_list[long - i - 1] = frame_list[long - i - 1], frame_list[i]

for i in range (0, long):
    ambos.write(frame_list[i])

for i in range(long// 2):
    frame_list[i], frame_list[long - i - 1] = frame_list[long - i - 1], frame_list[i]

for i in range (1, long):
    ambos.write(frame_list[i])


ambos.release()
cv2.destroyAllWindows()