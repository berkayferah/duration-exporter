import cv2

path = "./venv/Videos/Sogan Acisi Belgesel.mp4"


def with_opencv(filename):
    video = cv2.VideoCapture(filename)

    # info gather
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)

    # final calculations
    total_seconds = frame_count / fps
    hour = int(total_seconds / 3600)
    minute = int(total_seconds / 60)
    second = int(total_seconds % 60)
    remainder_frame = int(frame_count % fps)

    for item in hour, minute, second, remainder_frame:
        if item == 0:
            item = 00

    formatted_value = f"{hour}:{minute}:{second}:{remainder_frame}"

    print(formatted_value)
    return formatted_value


with_opencv(path)
