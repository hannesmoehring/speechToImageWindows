import datetime
import os
import signal
import threading
import time
import tkinter as tk

from PIL import ImageTk, Image

import audioProcessing
import imageProcessing
import printHandler

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
image_path = os.path.join('images', 'layoutImg.jpg')

LAYOUT = Image.open(image_path)


# Method to start audio processing and update the GUI accordingly
def start_processing():
    recButton.destroy()  # Remove the button

    image = LAYOUT.resize(
        (int(root.winfo_width() * 1), int(root.winfo_height() * 1)))  # Resize image to fit the window
    background_image = ImageTk.PhotoImage(image)
    # Create a Label widget to display the background image

    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image

    status_label.config(text="Processing...", fg="black")  # Processing placeholder in case response is not fast enough
    status_label.lift()
    # Call the audioProcessing.routine() method
    output_text = audioProcessing.routine()
    imageProcessing.genImage(output_text)

    # Update the status label with the output text
    status_label.config(text=output_text, padx=15, pady=15)

    # After 15 seconds, remove the output text and display the image
    threading.Timer(10, show_image).start()
    root.configure()


# Method to display the image after 15 seconds
def show_image():
    status_label.lower()
    # Load and display the image
    image_path = os.path.join('localImgSave', 'Img.jpg')
    image = Image.open(image_path)
    image = image.resize(
        (int(root.winfo_width() * 0.5), int(root.winfo_width() * 0.5)))  # Resize image to fit the window
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo)
    image_label.image = photo
    image_label.configure(pady="30", padx="0")
    image_label.pack()
    os.rename(os.path.join('localImgSave', 'Img.jpg'), os.path.join('localImgSave', 'Img' + str(timestamp) + '.jpg'))
    status_label.lift()
    status_label.place(relx=0.5, rely=0.87, anchor="center")
    time.sleep(3)
    imgpath = printHandler.routine(timestamp)

    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.BOTTOM)

    restart_button = tk.Button(button_frame, text="Restart", command=kill_and_execute, width=20, height=5)
    restart_button.pack(side=tk.LEFT, padx=10, pady=7)  # side="bottom", anchor="center"

    print_button = tk.Button(button_frame, text="Print it!", command=lambda: startPrint(imgpath), width=20, height=5)
    print_button.pack(side=tk.LEFT, padx=10, pady=7)  # side="bottom", anchor="center"

    root.grid_rowconfigure(0, weight=1)


def test_proc():

    time.sleep(1)
    # Create a popup window using Toplevel
    popup_window = tk.Toplevel(root)
    popup_window.after(8000, popup_window.destroy)
    popup_window.title("Processing...")
    popup_window.geometry("400x400")
    popup_window.configure(bg="red")

    # Center the popup window on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 400
    window_height = 400
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    popup_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    popup_window.configure(bg="red")

    # Label to display message in the popup window
    label = tk.Label(popup_window, font=("Arial", 24), bg="white", text="Bereit zum Zuhören!")  # image=tkimg
    label.place(relx=0.5, rely=0.5, anchor="center")

    # Execute the time-consuming task after the popup window is displayed
    popup_window.after(110, start_processing)

    print("Popup window is destroyed.")


def resize(img, x, y):
    img.resize(
        (int(root.winfo_width() * x), int(root.winfo_height() * y)))


# GUI initialization
root = tk.Tk()
root.attributes("-fullscreen", True)
image = LAYOUT
root.after(100, resize(image, 1, 1))
background_image = ImageTk.PhotoImage(image)
# Create a Label widget to display the background image

background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.image = background_image

img = Image.open(os.path.join('images', 'recButton2.png'))
width = int(root.winfo_width() * 0.2)
height = int(root.winfo_height() * 0.2)
if width > 0 and height > 0:
    img = img.resize((width, height))
else:
    ...
    # Handle the case where width or height is zero or negative
    # You can either skip the resize or perform a different action based on your requirements

img = ImageTk.PhotoImage(img)

# TODO: button background is transparent but in gui is white, should be fixed be using canvas

recButton = tk.Button(root, image=img, font=("Arial", 24),
                      command=test_proc)  # command=lambda: [root.configure(bg="red"), start_processing()]
recButton.configure(bd=0, highlightthickness=0, bg="gray")
recButton.place(relx=0.5, rely=0.5, anchor="center")

# Create and configure the status label
status_label = tk.Label(root, text="", font=("Arial", 24), fg="black")
status_label.place(relx=0.5, rely=0.5, anchor="center")
status_label.lower()


def kill_and_execute():
    pid = os.getpid()
    os.kill(pid, signal.SIGTERM)


# Start the GUI event loop
def startGui():
    root.mainloop()


def startPrint(imgpath):
    printHandler.printImg(imgpath),
