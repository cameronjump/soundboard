# soundboard

![screenshot_20190210_132220](https://user-images.githubusercontent.com/23038185/52538350-3c527980-2d37-11e9-87fc-b0eff53c92fa.png)

Hacklahoma 2019

What it does

The app allows users to record sound clips and manually or automatically generate sound buttons on the soundboard. These buttons can then be searched to string together new sentences in the user's voice.
How we built it

We have a python server running on Heroku that receives sound clips recorded on the Android app. The server takes the clip and splits it into word sound clips, writes those audio clips to text, and sends the text and associated sound file back to the app, which then displays each as a button. The app then provides functionality to search for specific words or phrases and the user can click the buttons to string together recorded clips.

The app is built in Kotlin using some extra libraries such as EventBus, RxJava, and RetroFit. The app records audio and then posts it to the python server. Once the app receives the response from the server it writes the files to the local directories for display.
Challenges we ran into

The libraries for splitting sound clips and converting speech to text did not function as well as we had hoped and we ran into some difficulties sending and working with the sound files. We had a lot of trouble with the encoding and decoding of the audio files between the Android app and the Python server. We also had some trouble getting our server to run on Heroku, but ended up getting it working in the end. A lot of great learning opportunities for the team!
Accomplishments that we're proud of

The app user interface is super clean and user-friendly! And we are free of our computers and fully hosted in Heroku.

cameronjump - android
madhawk22- flask python server
gerardototh - python audio to text
stmead - c/c++ audio manipulation
