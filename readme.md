# Mouse Activity Script

This Python script continuously moves the mouse cursor to keep the system from entering an idle state. It also detects any keyboard or mouse activity and stops the script once such activity is detected.

## Features

- **Continuous Mouse Movement:** The script moves the mouse cursor back and forth every second to prevent the system from considering it idle.
- **Activity Detection:** The script monitors keyboard presses (specifically the "Escape" key) and mouse button clicks. If any of these activities are detected, the script stops running.
- **Multithreading:** The script uses multithreading to run the mouse movement and activity detection simultaneously.

## Prerequisites

Ensure you have Python installed on your system. You also need to install the following Python libraries:

- `pyautogui`: Used for controlling the mouse.
- `keyboard`: Used for detecting keyboard input.
- `mouse`: Used for detecting mouse input.

You can install the required libraries using pip:

\`\`\`bash
pip install pyautogui keyboard mouse
\`\`\`

## How to Use

1. **Run the Script:**

   Execute the script in your Python environment:

   \`\`\`bash
   python script_name.py
   \`\`\`

   Replace \`script_name.py\` with the name of your Python file.

2. **Mouse Movement:**

   The script will start moving the mouse cursor back and forth every second.

3. **Activity Detection:**

   - Press the \`Escape\` key, click any mouse button, or manually move the mouse to stop the script.
   - The script will detect this activity and stop automatically, printing a message indicating that the script has stopped.

## How It Works

- **Thread 1:** The \`move_mouse()\` function runs in a separate thread and is responsible for moving the mouse cursor by 10 pixels to the right and then back to the left every second.
- **Thread 2:** The \`detect_activity()\` function runs in another thread, constantly checking for keyboard or mouse activity. If activity is detected, the \`running\` flag is set to \`False\`, stopping both threads.

## Example Output

\`\`\`
Mouse movement script started. Press any key or move the mouse to stop.
Mouse or keyboard activity detected. Stopping the script.
Script stopped.
\`\`\`

## Notes

- The script will stop as soon as it detects any of the following:
  - The \`Escape\` key is pressed.
  - The left or right mouse button is clicked.
  - The mouse is manually moved from its previous position.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code as you see fit.

---

This script is ideal for scenarios where you need to keep your computer awake without manual intervention, such as during long-running processes or downloads.