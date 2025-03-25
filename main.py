#GUI를 구현한 클라이언트 코드
import tkinter as tk
from tkinter import messagebox
import requests
import json

URL = 'http://127.0.0.1:5000/send-json'

def send_to_server():
    client_name = entry_client.get()
    message_text = entry_message.get()
    student_id = entry_id.get()

    if not client_name or not message_text or not student_id:
        messagebox.showwarning("입력 오류", "모든 필드를 입력해주세요.")
        return

    data = {
        "client": client_name,
        "message": message_text,
        "학번": student_id
    }

    try:
        response = requests.post(URL, json=data)
        response.raise_for_status()
        result = response.json()
        output_text.set(json.dumps(result, ensure_ascii=False, indent=2))
    except requests.exceptions.RequestException as e:
        messagebox.showerror("요청 실패", str(e))


# GUI 생성
window = tk.Tk()
window.title("JSON 클라이언트")
window.geometry("400x400")

# 입력 필드
tk.Label(window, text="이름:").pack()
entry_client = tk.Entry(window, width=40)
entry_client.pack()

tk.Label(window, text="메시지:").pack()
entry_message = tk.Entry(window, width=40)
entry_message.pack()

tk.Label(window, text="학번:").pack()
entry_id = tk.Entry(window, width=40)
entry_id.pack()

# 전송 버튼
tk.Button(window, text="서버에 전송", command=send_to_server).pack(pady=10)

# 응답 출력창
tk.Label(window, text="서버 응답:").pack()
output_text = tk.StringVar()
output_box = tk.Label(window, textvariable=output_text, bg="white", width=50, height=10, anchor="nw", justify="left", relief="solid")
output_box.pack(padx=10, pady=5, fill="both", expand=True)

# 실행
window.mainloop()