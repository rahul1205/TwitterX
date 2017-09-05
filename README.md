Requirements

To use all of the functionality of the library, you should have:
    
    Python 2.6, 2.7, or 3.3+ (required)
    PyAudio 0.2.11+ (required only if you need to use microphone input, Microphone)
    PocketSphinx (required only if you need to use the Sphinx recognizer, recognizer_instance.recognize_sphinx)
    Google API Client Library for Python (required only if you need to use the Google Cloud Speech API, recognizer_instance.recognize_google_cloud)
    FLAC encoder (required only if the system is not x86-based Windows/Linux/OS X)


Commands to run

    sudo apt-get install python-pip
    sudo apt-get install portaudio-dev
    sudo pip install google-api-python-client
    sudo pip install google-cloud
    sudo pip install twython

Note-To correctly upgrade/install PyAudio, download and extract the 0.2.11 version from here https://pypi.python.org/pypi/PyAudio
and run the following set of commands from inside the portaudio directory

    ./configure && make
    sudo make install
    sudo pip install pyaudio --upgrade
    
    
Twitter Setup
     You need a valid twitter account to tweet and need to implement the following steps from your account.
     1) Go to https://apps.twitter.com
     2) Create a new app and generate your Consumer Key, Consumer Secret, Access token and Access token secret and replace 
     these values under TwitterBot/letsTweet.py
     3) Save the changes.

Note-Tweets cannot be duplicated.

For language changes and other settings in speech to text conversions, view https://github.com/Uberi/speech_recognition




Finally, execute the letsTweet.py under MyTwitterBot/TwitterBot using command "python letsTweet.py".
     
