import json
import time
import cv2

class capture_qrcode:
    def __init__(self, cap:cv2.VideoCapture, detector:cv2.QRCodeDetector):
        self.cap = cap # 카메라 객체
        self.detector = detector # QR 인식기 객체

        self.last_detected = ""  # 이전 QR 내용 저장용
        self.last_time = 0       # 마지막 인식 시간

        if not self.cap.isOpened():
            print("❌ 카메라를 열 수 없습니다.")
            raise Exception("카메라를 열기 실패")

    def capture(self):
        ret, frame = self.cap.read()
        if not ret:
            print("❌ 프레임을 읽을 수 없습니다.")
            raise Exception("프레임 읽기 실패")

        data = self.detector.detectAndDecode(frame)[1]

        if data:
            current_time = time.time()
            if data != last_detected or (current_time - last_time > 5):  # 5초 이내 중복 방지
                print("\n✅ QR 코드 인식됨:")
                try:
                    parsed = json.loads(data)
                    for i, j in parsed.items():
                        print(f"  {i}: {j}")
                except json.JSONDecodeError:
                    print("⚠️ JSON 형식이 아닙니다.")

                last_detected = data
                last_time = current_time
                time.sleep(2)  # 2초 대기 (중복 감지 방지)

# cap.release()
# cv2.destroyAllWindows()
