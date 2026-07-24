import pyautogui
import pyscreeze
import time
from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

print("Step 1: Open the browser..")
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.typewrite('chrome\n', interval=0.1)
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

print("Step 2: Open the Weather wesite ..")
# pyautogui.hotkey('ctrl', 't') # open a new tab in the browser
pyautogui.typewrite('https://wttr.in/?format=4\n', interval=0.1)
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)

print("Step 3: Take screenshot..")
pyautogui.screenshot().save(f'daily_report_screenshot_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png')
time.sleep(1)


print("Step 4: Copy the data..")
pyautogui.hotkey('ctrl', 'a')  # Select all content
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')  # Copy the selected content
time.sleep(1)

print("Step 5: Open Excel and paste the data..")
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.typewrite('excel\n', interval=0.1)
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)

'''Create a new row containing three things: today's date & time, the fetched data, and your own
short comment (for example, “Good for outdoor activities”).
'''

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# Assuming the fetched data is in the clipboard, we can paste it in the new row 
pyautogui.typewrite(current_datetime + '\t' + "Good for outdoor activities", interval=0.1) 
pyautogui.press('enter')  # Move to the next row after entering the data
pyautogui.hotkey('ctrl', 'v')
time.sleep(5)
save_path = f"D:\\GenAI\\Git_VScode_Week1_Day3_Project\\pyautogui_automation\\Daily_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

print("Step 6: Save Excel file..    ")
pyautogui.hotkey('Fn', 'f12')
time.sleep(5)
pyautogui.typewrite(save_path, interval=0.1)
pyautogui.press('enter')
time.sleep(5)

print("Step 7: Close the Excel file..")
time.sleep(1)
pyautogui.hotkey('Alt', 'f4')

print("Step 8: Close the Browser..")
time.sleep(1)
pyautogui.hotkey('Alt', 'f4')