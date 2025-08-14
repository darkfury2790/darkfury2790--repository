from tkinter import*
from deep_translator import GoogleTranslator as gt

translated_txt = gt(source='en', target='fr').translate("Hello")

root=Tk()
root.title("language translator")
root.geometry("500x150")
lbl=Label(root, text='type what you what to translate')
lbl.grid()

original_txt = Entry(root, width=20)
original_txt.grid(column=0, row=1)


trgt_language = ['French']
slct_language = StringVar(root)
slct_language.set("select an option")
question_menu = OptionMenu(root, slct_language, *trgt_language)
question_menu.grid(column=1,row=1)
def translate():
    if slct_language.get() == 'French':
       translated_txt = gt(source='en', target='fr').translate(original_txt.get())
    else:
        translated_txt = gt(source='en', target='fr').translate(original_txt.get())
    txt = Label(root, text=translated_txt)
    txt.grid(column= 0, row=3)



btn=Button(root, text='Translate', fg='red', command=translate)
btn.grid(column=0, row=2)
root.mainloop()  