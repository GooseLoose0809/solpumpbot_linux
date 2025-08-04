from flask import Flask
import pyautogui
import time
import threading

app = Flask(__name__)

BTN_IMAGE = "approve.png"

def click_approve():
    print("[*] Searching for approve button...")
    for i in range(20):
        location = pyautogui.locateOnScreen(BTN_IMAGE, confidence=0.8)
        if location:
            print("[+] Approve button found.")
            pyautogui.click(pyautogui.center(location))
            return
        time.sleep(0.5)
    print("[-] Approve button not found.")

@app.route("/", methods=["GET"])
def trigger_click():
    threading.Thread(target=click_approve).start()
    return "Triggered", 200

if __name__ == "__main__":
    print("[*] Listening on http://0.0.0.0:6969 (forever)")
    app.run(host="0.0.0.0", port=6969)
