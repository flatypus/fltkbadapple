from pydub import AudioSegment
from pydub.playback import play
import pickle

song = AudioSegment.from_mp3("badapple.mp3")
pickle.dump(song, open("song.pickle", "wb"))
