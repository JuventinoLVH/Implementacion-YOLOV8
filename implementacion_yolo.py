import os
from ultralytics import YOLO
import cv2 as cv

HOME = os.getcwd()
YOLO_path = HOME + "/runs/detect/train/weights/best.pt"


modelo = YOLO(YOLO_path)
webcam = cv.VideoCapture(0)
while(True):
    exito , frame = webcam.read()
    if not exito :
        break
    resultado = rame_clasificado = modelo(frame,mode="predict",show = True)     
webcam.release()
cv.destroyAllWindows()

