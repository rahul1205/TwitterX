
import sys
from twython import Twython
import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something! Say 'exit' to quit")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
	    pa = pyaudio.PyAudio()
	    print(pa.get_device_count())
	    sys.exit()
            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print("You said {}".format(value).encode("utf-8"))
	    if format(value).encode("utf-8")=="exit":
		sys.exit()
		the_input = raw_input("Do you want to tweet this?(y/n)")
	    if the_input=="y" or the_input=="Y":
		
		#SPECIFY YOUR API END POINTS HERE
		#apiKey = ''
		#apiSecret = ''
		#accessToken = ''
		#accessTokenSecret = ''

		api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

		api.update_status(status=format(value).encode("utf-8"))

		print "Tweeted: " + format(value).encode("utf-8")
		sys.exit()
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
