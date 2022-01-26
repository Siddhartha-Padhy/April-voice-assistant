from tkinter import *
from threading import *
from driver import *
import speech_recognition as sr
import os

BACKGR_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
FONT = "Helvetica"

class Assistant:
    def __init__(self):
        self.window = Tk()
        self.setup_main_window()

    def run(self):
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop(0)

    def setup_main_window(self):
        self.window.title("Assistant")
        self.window.iconbitmap('Assistant/assets/icon.ico')
        self.window.resizable(width=False, height=False)
        self.window.configure(width=400, height=500, bg=BACKGR_COLOR)

        #output field for providing meta data
        self.output_field = Entry(self.window,borderwidth=3, relief="sunken", justify=CENTER, disabledbackground="#282828", font=(FONT, 16), disabledforeground=TEXT_COLOR, background="#282828", foreground=TEXT_COLOR)
        self.output_field.insert(0,"Let's Get Started")
        self.output_field.place(relx=0.5, rely=0.08, anchor=CENTER, width=328, height=43)
        self.output_field.configure(cursor="arrow", state=DISABLED)

        #border outline
        outline = Label(self.window, width=40, height=18)
        outline.place(relx=0.5, rely=0.5, anchor=CENTER)

        #main text field
        self.text_field = Text(self.window, wrap=WORD, bg="#000000", fg=TEXT_COLOR, state=DISABLED)
        self.text_field.place(relx=0.5,rely=0.5, anchor=CENTER, width=310, height=330)

        #user input field
        self.input_field = Entry(self.window,borderwidth=3, relief="sunken", justify=CENTER, font=(FONT, 14))
        self.input_field.place(relx=0.43, rely=0.92, anchor=CENTER, height=40, width=270)
        self.input_field.focus()
        
        #MIC button
        self.start_btn = Button(self.window,text="MIC", command=self.start_thread,bg="#228B22",fg="white",disabledforeground="white", padx=30)
        self.start_btn.place(relx=0.85,rely=0.92, anchor=CENTER, width=50, height=43)

    def start_thread(self):
        t1 = Thread(target=self.start_voice)
        t1.start()

    def local_driver(self,text):
        heading, output = main_driver(text)

        if heading != None:
            if heading=="Sleep":
                self.output_field.configure(state=NORMAL)
                self.output_field.delete(0,END)
                self.output_field.insert(END, "Waiting")
                config.speak("Waiting")
                self.output_field.configure(state=DISABLED)
                self._sleep_()
            
            else:
                self.output_field.configure(state=NORMAL)
                self.text_field.configure(state=NORMAL)
                self.text_field.delete("1.0",END)
                self.output_field.delete(0,END)
                self.output_field.insert(END,heading)
                self.output_field.configure(state=DISABLED)
                self.text_field.configure(state=DISABLED)
                config.speak(self.output_field.get())

                for slide in output:
                    self.text_field.configure(state=NORMAL)
                    self.text_field.insert(END, slide+"\n")
                    self.text_field.configure(state=DISABLED)
                    config.speak(slide)

        else:
            self.output_field.configure(state=NORMAL)
            self.text_field.configure(state=NORMAL)
            new_txt = "You said " + text
            self.output_field.delete(0,END)
            self.output_field.insert(0,new_txt)
            self.text_field.delete("1.0", END)
            self.text_field.insert(END, "Write or say a meaningful command to operate.")
            self.output_field.configure(state=DISABLED)
            self.text_field.configure(state=DISABLED)

    def start_voice(self):
        while True:
            self.output_field.configure(state=NORMAL)
            self.output_field.delete(0,END)
            self.output_field.insert(END,"Listening...")
            self.output_field.configure(state=DISABLED)
            config.speak("Listening")
            text = config.listen()
            if text == None:
                self.output_field.configure(state=NORMAL)
                self.output_field.delete(0,END)
                self.output_field.insert(END,"Try again!")
                self.output_field.configure(state=DISABLED)
            else:
                text = text.lower()
                self.input_field.delete(0,END)
                self.input_field.insert(END, text)
                self.local_driver(text)

    def _sleep_(self):
        sample_rate = 48000
        chunk_size = 2048
        while True:
            r= sr.Recognizer()
            with sr.Microphone(sample_rate=sample_rate, chunk_size=chunk_size ) as source:
                try:
                    audio = r.listen(source)
                    MyText = r.recognize_google(audio)
                    if NAME.lower() in MyText.lower():
                        break

                except Exception as e:
                    continue
        
        return

    def on_closing(self):
        os._exit(1)

if __name__=="__main__":
    app = Assistant()
    app.run()