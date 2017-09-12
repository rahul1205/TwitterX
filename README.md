<h1>SpeakAndTweet</h1>
A command line utility that can be used to tweet an input from microphone. You'll never have to type again.!!!
<hr>

<h3>Requirements</h3><p><b>(As of now, the instruction set added is only for Ubuntu 14.04 and higher)</b></p>
To use all of the functionality of the library, you should have:
    
    Python 2.6, 2.7, or 3.3+ (required)
    PyAudio 0.2.11+ (required only if you need to use microphone input, Microphone)
    PocketSphinx (required only if you need to use the Sphinx recognizer, recognizer_instance.recognize_sphinx)
    Google API Client Library for Python (required only if you need to use the Google Cloud Speech API, recognizer_instance.recognize_google_cloud)
    FLAC encoder (required only if the system is not x86-based Windows/Linux/OS X)


<h4>A hassle free guide to quick install from scratch on Python 2.7.6</h4>
    
   <h5>Installing pip</h5>
    sudo apt-get install python-dev
    easy_install pip
    
   <h5>Installing PyAudio latest Version<h5>
    To correctly upgrade/install PyAudio, download and extract the 0.2.11 version from here http://www.portaudio.com/download.html
    and run the following set of commands from inside the portaudio directory

    ./configure && make
    sudo make install
    sudo pip install pyaudio --upgrade (run this only if you have an older version of pyaudio)
    
   <h5>Installing Speech Recognition Module and setting up google API<h5>
    pip install SpeechRecognition
    sudo pip install google-api-python-client
    
    <b>Note</b>-Google API has some limit on number of inputs per day. To install other servers when google API is unavailable, refer to https://github.com/Uberi/speech_recognition
    
   <h5>Installing Twitter API for python<h5>
    sudo pip install twython
    
   <h5>Installing ALSA libraries<h5>
    sudo apt-get install libasound-dev
    
    
    
<h4>Twitter Setup</h4>
     You need a valid twitter account to tweet and need to implement the following steps from your account.
     
     1) Go to https://apps.twitter.com
     2) Create a new app and generate your Consumer Key, Consumer Secret, Access token and Access token secret and replace these values under TwitterBot/letsTweet.py
     3) Save the changes.

<b>Note</b>-Tweets cannot be duplicated.

For language changes and other settings in speech to text conversions, view https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
<br>
<h6>Finally, execute the letsTweet.py under MyTwitterBot/TwitterBot using command "python letsTweet.py".</h6>
<b><i>P.S.</b> Remember to say 'exit' if you want to quit without tweeting</i>
     
