from flask import Flask
import pyautogui
import time
import threading

app = Flask(__name__)

# 💥 Confirmed approve button position
APPROVE_X = 1185
APPROVE_Y = 614

def click_approve():
    print("[*] Clicking approve button at coords (1185, 614)...")
    time.sleep(1)  # 1-second delay before clicking
    pyautogui.moveTo(APPROVE_X, APPROVE_Y)
    pyautogui.click()
    print("[+] Clicked approve.")

@app.route("/", methods=["GET"])
def trigger_click():
    threading.Thread(target=click_approve).start()
    return "Triggered", 200

if __name__ == "__main__":
    print("[*] Listening on http://localhost:6969/")
    app.run(host="0.0.0.0", port=6969)
