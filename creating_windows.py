import threading
from fltk import *
import pickle
from pydub.playback import play
import pyautogui
import time


def play_song():
    song = pickle.load(open("song.pickle", "rb"))
    play(song)


def make_fltk_dance():
    rects = pickle.load(open("rects.pickle", "rb"))
    windows = []
    for frame in range(len(rects)):
        new_windows = []
        print("Frame", frame)
        for x, y, w, h in rects[frame][::-1]:
            # print(x, y, w, h)
            new_windows.append(Fl_Window(x*10, y*10, w*10, h*10))
            # new_windows[-1].color(FL_BLACK)
            new_windows[-1].color(FL_WHITE)
            # set border color to black

            # new_windows[-1].clear_border() # remove border
            new_windows[-1].show(sys.argv)
        # take a screenshot
        Fl.check()
        time.sleep(0.05)
        for i in windows:
            i.hide()
            del i
        pyautogui.screenshot(f"screenshots/{frame}.png")
        windows = new_windows.copy()


# t1 = threading.Thread(target=play_song)
t2 = threading.Thread(target=make_fltk_dance)
# t1.start()
t2.start()
# t1.join()
t2.join()
