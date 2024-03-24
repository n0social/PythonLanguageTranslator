#Imports - Step 1

from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

#Setting up the Tkinter Window - # Step 2
root = Tk() #Initialize a root window
root.geometry('1100x320') #Set the size of the window
root.resizable(0,0) #Set it to a resizable
root['bg'] = 'blue' #Change the background color to blue
root.title('Google Translator') #Give the window a title

#Creating the GUI - Step 3

Label(root, text="Language Translator", font="Poppins 20 bold").pack()

Label(root, text="Enter Text", font="Poppins 13 bold", bg='white smoke').place(x=165,y=90)

Input_text = Entry(root, width=60)
Input_text.place(x=30,y=130)

Label(root, text="Output", font="Poppins 13 bold", bg="white smoke").place(x=780, y=90)
Output_text = Text(root, font="Poppins 10", height=5, wrap=WORD, padx=5, pady=5, width=50)
Output_text.place(x=600, y=130)

language = list(LANGUAGES.values())
dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=130,y=180)
dest_lang.set('Choose a Language')

#Translation function - Step 4
#The function uses the googletrans library to translate text from an entry
#widget ("input_text") to a specified destination language. It clears the
#output text widget ("Output_text") before inserting the translated text.
#Any errors will print out an error 

def Translate():
    try:
        translator = Translator()
        translation = translator.translate(Input_text.get(), dest=dest_lang.get())
        Output_text.delete(1.0, END)
        Output_text.insert(END,translation.text)
    except Exception as e:
        print(f"Translation error: {e}")
        
#Button for triggering Translation - Step 5
trans_btn = Button(root, text="Translate", font="Poppins 12 bold", pady=5, command=Translate, bg="lightblue", activebackground="grey")
trans_btn.place(x=445,y=180)

#Run the main loop - Step 6
root.mainloop()