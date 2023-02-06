import speech_recognition as sr

  #This is my python speech to text program made with python for ece 331 asssignment

r = sr.Recognizer()
print("Recognising my speech...")

generate = sr.AudioFile('ronald.wav')
with generate as source:
    audio = r.record(source)
    
    type(audio)
    
    r.recognize_google(audio)
    
    print("Ending my speech Recognition..")
    
    
 
    
    