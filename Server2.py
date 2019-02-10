from flask import Flask, jsonify, request, abort, render_template, flash, url_for, redirect, render_template
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.playback import play
import base64 
import os
import speech_recognition as sr

app = Flask(__name__)
app.config.from_object(__name__)

# -------------------------------------------------------------- API --------------------------------------------------------------
@app.route('/soundboard', methods=['POST'])
def get_soundclip():
        clip = request.get_json()

        file_name = clip['name']
        file_body = clip['raw']

        new_file = open(file_name + '.mp4', 'wb')
        new_file.write(base64.b64decode(file_body))
        new_file.close()
        os.system('ffmpeg -i {}.mp4 -acodec pcm_s16le -ar 16000 {}.wav'.format(file_name, file_name))
        os.remove(file_name + '.mp4')
        return jsonify(split_sound(file_name + '.wav'))

# ------------------------------------------------------------ SPLIT ---------------------------------------------------------------
def split_sound(soundfilename):
        returnclips = []
        r = sr.Recognizer()
        soundclip = AudioSegment.from_file(soundfilename)
        words = split_on_silence(soundclip, min_silence_len=200, silence_thresh=soundclip.dBFS - 10, keep_silence=50)
        print(len(words))

        for i, chunk in enumerate(words):
                chunkfilename = 'chunk' + str(i) + '.wav'
                words[i].export(chunkfilename, format = 'wav')
                
                with sr.AudioFile(chunkfilename) as source: 
                    audio = r.record(source)   
            
                try: 
                    print("The audio file contains: " + r.recognize_google(audio)) 
                    raw = ""
                    with open(chunkfilename, "rb") as chunkfile:
                        raw = base64.b64encode(chunkfile.read())
                        #print(raw)

                    #raw = str(base64.b64encode(rawfile))
                    chunkfile.close()
                    returnclips.append({'name' : r.recognize_google(audio), 'raw' : str(raw) })
                
                except sr.UnknownValueError: 
                    print("Google Speech Recognition could not understand audio") 

                except sr.RequestError as e: 
                    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

                os.remove(chunkfilename)
        
        os.remove(soundfilename)
        return returnclips

if __name__ == '__main__':
        app.run(host='0.0.0.0')
