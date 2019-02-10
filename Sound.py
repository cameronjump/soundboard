from flask import Flask, jsonify, request, abort, render_template, flash, url_for, redirect, render_template
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.playback import play
import base64 
import os
import speech_recognition as sr

def main():
    split_sound('file.wav')
    

def split_sound(soundfilename):
        returnclips = []
        r = sr.Recognizer()

        soundclip = AudioSegment.from_file(soundfilename)
        #play(soundclip)
        words = split_on_silence(soundclip, min_silence_len=200, silence_thresh=soundclip.dBFS - 10, keep_silence=50)
        print(len(words))
        for i, chunk in enumerate(words):
                chunkfilename = 'chunk' + str(i) + '.wav'
                words[i].export(chunkfilename, format = 'wav')
                
                with sr.AudioFile(chunkfilename) as source: 
                    audio = r.record(source)   
            
                try: 
                    print("The audio file contains: " + r.recognize_google(audio)) 
                    returnclips.append({'name' : r.recognize_google(audio), 'file' : chunkfilename })
                
                except sr.UnknownValueError: 
                    print("Google Speech Recognition could not understand audio") 

                except sr.RequestError as e: 
                    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

        return returnclips
main()
