import threading
import logging
from fltk import *
import pickle
import time
from pydub.playback import play


def play_song():
    song = pickle.load(open("song.pickle", "rb"))
    play(song)


def make_fltk_dance():
    rects = pickle.load(open("rects.pickle", "rb"))
    windows = []
    for frame in range(len(rects)):
        new_windows = []
        print("Frame", frame)
        for x, y, w, h in rects[frame]:
            # print(x, y, w, h)
            new_windows.append(Fl_Window(x*10, y*10, w*10, h*10))
            new_windows[-1].color(FL_BLACK)
            new_windows[-1].clear_border()
            new_windows[-1].show(sys.argv)
        Fl.check()
        # time.sleep(0.05)
        for i in windows:
            i.hide()
            del i
        windows = new_windows.copy()


t1 = threading.Thread(target=play_song)
t2 = threading.Thread(target=make_fltk_dance)
t1.start()
t2.start()
t1.join()
t2.join()
