import cv2
import os
import tkinter.filedialog
from tkinter import ttk, messagebox
from tkinter import *


video_list = []


def duration_calculate(filename):
    video = cv2.VideoCapture(filename)
    basename = os.path.basename(filename)

    # info gather
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)

    # calculations
    total_seconds = frame_count / fps

    hour = int(total_seconds / 3600)
    minute = int(total_seconds / 60)
    second = int(total_seconds % 60)
    remainder_frame = int(frame_count % fps)

    timecode = [hour, minute, second, remainder_frame]

    # cleanup
    i = 0
    for item in timecode:
        if item == 0:
            timecode[i] = str("00")
        if item < 10:
            timecode[i] = str("0") + str(item)
        i += 1

    # export
    formatted_value = \
        f"""{basename}
    {timecode[0]}:{timecode[1]}:{timecode[2]}:{timecode[3]}
    
"""
    return formatted_value


def add_file():
    file = tkinter.filedialog.askopenfilenames(title='Choose Files')
    root.splitlist(file)
    global video_list
    video_list = file

    for item in video_list:
        item = os.path.basename(item)
        file_list.insert(END, item)

    return video_list


def start_process():
    if len(video_list) < 1:
        messagebox.showinfo("Message", "Please add video files")
    else:
        save_path = tkinter.filedialog.asksaveasfilename(title='Choose Folder') + ".txt"
        if save_path == ".txt":
            return
        else:
            duration_text = ""

            for item in video_list:
                duration_calculate(item)
                duration_text = duration_text + duration_calculate(item)

            # write to disk
            with open(save_path, 'w') as f:
                f.write(duration_text)

            messagebox.showinfo("Message", "Timecodes successfully saved to destination")


# GUI
root = Tk()
root.title("Timecode Exporter")

my_label = Label(root, text="Files")
my_label.pack()

file_list = Listbox(root)
file_list.pack()

add_button = ttk.Button(root, text="Add Files", command=add_file)
add_button.pack(side=LEFT)

save_button = ttk.Button(root, text="Save Timecodes", command=start_process)
save_button.pack(side=LEFT)

root.mainloop()
