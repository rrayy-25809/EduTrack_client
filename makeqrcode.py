import qrcode
import json
from datetime import datetime

# 1. 현재 시간 구하기
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 2. JSON 데이터 만들기
data = {
    "name": "함태준",
    "student_id": "30923",
    "timestamp": now,
    "classroom": "국어3"
}

# 3. JSON 문자열로 변환
json_data = json.dumps(data, ensure_ascii=False)

# 4. QR 코드 생성
qr = qrcode.make(json_data)

# 5. 이미지로 저장
qr.save("qrcode_with_timestamp1.png")

print("QR 코드 생성 완료: qrcode_with_timestamp.png")
