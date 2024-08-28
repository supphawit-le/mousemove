import pyautogui
import keyboard
import mouse
import threading
import time

# Flag to control the loop
running = True

def move_mouse():
    while running:
        pyautogui.moveRel(10, 0, duration=0.1)  # Move mouse right 10 pixels
        pyautogui.moveRel(-10, 0, duration=0.1) # Move mouse left 10 pixels
        time.sleep(1)  # Wait 1 second

def detect_activity():
    global running
    while running:
        if keyboard.is_pressed('esc') or mouse.is_pressed(button='left') or mouse.is_pressed(button='right') :
            print("Mouse or keyboard activity detected. Stopping the script.")
            running = False

if __name__ == "__main__":
    print("Mouse movement script started. Press any key or move the mouse to stop.")

    #prev_mouse_position = [mouse.get_position()]  # Track the last position of the mouse

    # Start the mouse movement thread
    mouse_thread = threading.Thread(target=move_mouse)
    mouse_thread.start()

    # Start the activity detection thread
    detect_thread = threading.Thread(target=detect_activity)
    detect_thread.start()

    # Wait for threads to finish
    mouse_thread.join()
    detect_thread.join()

    print("Script stopped.")
