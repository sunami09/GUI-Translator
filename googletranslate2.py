from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob
root = Tk()
root.geometry('500x400')
root.title('Translator')
root.resizable(False,False)
root.configure(bg='green')
lan_dict={'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
def translate():
    word=TextBlob(varname.get())
    lan= word.detect_language()
    lan_todict=languages.get()
    lan_to=lan_dict[lan_todict]
    word=word.translate(from_lang=lan,to=lan_to)
    varname1.set(word)
    
def main_exit():
    rr=messagebox.askyesnocancel('Notification','Do you want to exit?',parent=root)
    if rr==True:
        root.destroy()
        
def on_enterentry1(e):
    entry1['bg'] = 'aqua'
def on_leaveentry1(e):
    entry1['bg']='white'
def on_enterentry2(e):
    entry2['bg'] = 'aqua'
def on_leaveentry2(e):
    entry2['bg']='white'


languages=StringVar()
font_box=Combobox(root,width=30,textvariable=languages,state='readonly')
font_box['values']=[e for e in lan_dict.keys()]
font_box.current(21)
font_box.place(x=300,y=0)
varname= StringVar()
entry1=Entry(root,width=30,textvariable=varname,font=('times',15,'italic bold'))
entry1.place(x=150,y=50)

varname1= StringVar()
entry2=Entry(root,width=30,textvariable=varname1,font=('times',15,'italic bold'))
entry2.place(x=150,y=120)

label1=Label(root,text='Enter Words:',font=('times',15,'italic bold'),bg='green')
label1.place(x=5,y=50)

label2=Label(root,text='Translated:',font=('times',15,'italic bold'),bg='green')
label2.place(x=5,y=120)

btn1=Button(root,text='Click',command=translate,bd=5,bg='yellow',activebackground='red',width=10,font=('times',15,'italic bold'))
btn1.place(x=70,y=190)

btn2=Button(root,text='Exit',command=main_exit,bd=5,bg='yellow',activebackground='red',width=10,font=('times',15,'italic bold'))
btn2.place(x=280,y=190)

entry1.bind('<Enter>',on_enterentry1)
entry1.bind('<Leave>',on_leaveentry1)

entry2.bind('<Enter>',on_enterentry2)
entry2.bind('<Leave>',on_leaveentry2)



root.mainloop()
