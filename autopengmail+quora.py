import subprocess,pyautogui,time
subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe"])
time.sleep(1)
pyautogui.hotkey('ctrl','shift','N')
pyautogui.typewrite('www.gmail.com')
pyautogui.press('enter')
time.sleep(3)
pyautogui.typewrite('<your email id here>')
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite('<your password here>')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','t')
pyautogui.typewrite('www.quora.com')
pyautogui.press('enter')





