import cv2
import json
import time

# QR 인식기 초기화
detector = cv2.QRCodeDetector()

# 카메라 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ 카메라를 열 수 없습니다.")
    exit()

print("실행되었습니다")

last_detected = ""  # 이전 QR 내용 저장용
last_time = 0       # 마지막 인식 시간
while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ 프레임을 읽을 수 없습니다.")
        break

    data, bbox, _ = detector.detectAndDecode(frame)

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

cap.release()
cv2.destroyAllWindows()
