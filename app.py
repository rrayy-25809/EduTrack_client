import threading
import time
import json
import cv2
import requests
import gpiozero

from capture_qrcode import capture_qrcode
import get_rfid
import send_to_server

# 기본 변수 설정
cap = cv2.VideoCapture(0) # 카메라 열기
detector = cv2.QRCodeDetector() # QR 인식기 초기화
qr_detector = capture_qrcode(cap, detector) # QR 인식 객체 생성
