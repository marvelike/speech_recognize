import speech_recognition as sr

r = sr.Recognizer()  # initialize recognizer
with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
    r.adjust_for_ambient_noise(source)
    print("Speak Anything :")
    audio = r.listen(source)  # listen to the source
    try:
        text = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
        print("You said : {}".format(text))
    except Exception as e:
        print("Sorry could not recognize your voice", e)  # In case of voice not recognized  clearly