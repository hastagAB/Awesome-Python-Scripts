import pyautogui
import webbrowser
import schedule
import time

def joinGoogleMeet(meeting_id):
    webbrowser.open_new_tab(
        f"https://meet.google.com/{meeting_id}".replace("'", ""))
    time.sleep(10)

    pyautogui.click()
    pyautogui.hotkey('ctrl', 'd')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'e')

    finaljoinBTN = pyautogui.locateCenterOnScreen(
        "assets/finalJoinMeet.png")
    pyautogui.moveTo(finaljoinBTN)
    pyautogui.click()

if __name__ == '__main__':
    # meeting_id = input("Meeting ID: ")
    # joinGoogleMeet(meeting_id)

    with open('meeting_ids.txt', 'r') as f:
        ids = f.readlines()
    with open('meeting_times.txt', 'r') as j:
        time = j.readlines()

    # You can add more number of scheduled meetings using the line below,
    # replacing 'x' with the value of the meeting id and time in their respective times

    # schedule.every().day.at(time[x]).do(joinGoogleMeet(ids[x]))

    schedule.every().day.at(time[0]).do(joinGoogleMeet(ids[0]))
    schedule.every().day.at(time[1]).do(joinGoogleMeet(ids[1]))
    schedule.every().day.at(time[2]).do(joinGoogleMeet(ids[2]))
