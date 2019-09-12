import numpy as np
import math       
import sys
import cv2
def calculateFrameStats(source,skip):
    cap = cv2.VideoCapture(source)

    data = {
        "frame_info": []
    }

    lastFrame = None
    while(cap.isOpened()):
        ret, frame = cap.read()
        if frame is None:
            break

        frame_number = cap.get(cv2.CAP_PROP_POS_FRAMES) - 1
        if frame_number % skip == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.resize(gray, None,fx=0.25, fy=0.25, interpolation = cv2.INTER_AREA)
            gray = cv2.GaussianBlur(gray, (9,9), 0.0)

            if lastFrame is not None:
                diff = cv2.subtract(gray, lastFrame)
                diffMag = cv2.countNonZero(diff)
                frame_info = {
                    "frame_number": int(frame_number),
                    "diff_count": int(diffMag)
                }
                data["frame_info"].append(frame_info)
                # cv2.imshow('diff', diff)
                # cv2.waitKey(1)
        lastFrame = gray

    cap.release()
    cv2.destroyAllWindows()
    diff_counts = [fi["diff_count"] for fi in data["frame_info"]]
    data["stats"] = {
        "mean": np.mean(diff_counts),
        "sd": np.std(diff_counts)
    }
    #print (data)
    return data


def detectKeyFrames(source,data,file_name):

    diff_threshold = (data["stats"]["sd"] * 1.85) + data["stats"]["mean"]
    cap = cv2.VideoCapture(source)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = cv2.VideoWriter(file_name, cv2.VideoWriter_fourcc('M','J','P','G'), 3, (frame_width, frame_height))
    for index, fi in enumerate(data["frame_info"]):
        if fi["diff_count"] < diff_threshold:
            continue
        cap.set(cv2.CAP_PROP_POS_FRAMES, fi["frame_number"])
        ret, frame = cap.read()
        if frame is not None:
            #cv2.imshow('extract', frame)
            #cv2.waitKey(0)
            out.write(frame)
    out.release()
    cap.release()
    cv2.destroyAllWindows()

source = sys.argv[1]
out = sys.argv[2]
data = calculateFrameStats(source,4)
detectKeyFrames(source, data, out)