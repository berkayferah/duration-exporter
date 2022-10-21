import cv2
import os

path = "./venv/Videos/Sogan Acisi Belgesel.mp4"
path2 = "./venv/Videos/device.mov"

list1 = [path, path2]


def duration(filename):
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


final_text = ""

for item in list1:
    duration(item)
    final_text = final_text + duration(item)

print(final_text)

with open('duration.txt', 'w') as f:
    f.write(final_text)
