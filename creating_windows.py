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
    white_rects = pickle.load(open("rects_white.pickle", "rb"))
    windows = {}
    white_windows = {}
    for frame in range(0, len(rects)):
        print("Frame", frame)
        for i in list(windows.keys()):
            if not i in rects[frame]:
                windows[i].hide()
                del windows[i]

        for i in list(white_windows.keys()):
            if not i in white_rects[frame]:
                white_windows[i].hide()
                del white_windows[i]

        def black():
            for x, y, w, h in rects[frame][::-1]:
                if (x, y, w, h) in windows.keys():
                    continue
                # print(x, y, w, h)
                windows[(x, y, w, h)] = Fl_Window(x*15, (y)*15, w*15, (h-1)*15)
                # new_windows[-1].color(FL_BLACK)
                windows[(x, y, w, h)].color(FL_WHITE)
                # set border color to black
                # windows[(x, y, w, h)].clear_border()  # remove border
                windows[(x, y, w, h)].show(sys.argv)

        def white():
            for x, y, w, h in white_rects[frame][::-1]:
                if (x, y, w, h) in white_windows.keys():
                    continue
                white_windows[(x, y, w, h)] = Fl_Window(
                    x*15, (y)*15, w*15, (h-1)*15)
                white_windows[(x, y, w, h)].color(FL_BLACK)
                white_windows[(x, y, w, h)].show(sys.argv)

        if (len(rects[frame]) > len(white_rects[frame])):
            white()
            black()
        else:
            black()
            white()
        # take a screenshot
        Fl.check()
        time.sleep(0.1)
        pyautogui.screenshot(f"screenshots/{frame}.png")


# t1 = threading.Thread(target=play_song)
t2 = threading.Thread(target=make_fltk_dance)
# t1.start()
t2.start()
# t1.join()
t2.join()
