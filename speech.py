def speech():
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r1.listen(source)
        print(r1.recognize_google(audio))
        text = r1.recognize_google(audio)
    response = messagebox.showinfo("Verify","Did you mean "+text+" ?")
    Down(text)