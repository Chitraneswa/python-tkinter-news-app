from tkinter import *
import requests
from PIL import Image,ImageTk

class News:
    def __init__(self):#constructor
        self.root=Tk()
        self.root.title("News Application:")
        self.root.minsize(500,600)
        self.root.maxsize(500,600)
        self.root.configure(bg="#fff")

        self.label=Label(self.root,text="Apna news 24*7")#object of label class
        self.label.configure(font=("Times",30,"bold"))
        self.label.pack(pady=(30,30))

        self.label1=Label(self.root,text="Enter the topic:",bg="#fff")
        self.label1.configure(font=("Times",15,"italic"))
        self.label1.pack(pady=(10,20))

        self.topic=Entry(self.root)#entry box
        self.topic.pack(pady=(5,10),ipadx=30,ipady=3)

        self.click=Button(self.root,text="Search",bg="#000",fg="#fff",command=lambda: self.fetch())#obj of button class
        self.click.pack(pady=(5,10))

        self.root.mainloop()

    def fetch(self):
        #fetch the searching term
        term=self.topic.get()
        url="https://newsapi.org/v2/everything?q={}&apiKey=129bd801b8004a0fb0c4efe153deeacc".format(term)#dynamic url
        #hit the api

        response=requests.get(url)
        self.response=response.json()#converting to json
        #print(self.response)
        self.data=self.response['articles']
        self.extract()


    def extract(self,index=0):
        news=[]
        news.append(self.data[index]['title'])
        news.append(self.data[index]['source']['name'])
        news.append(self.data[index]['description'])
        self.clear()
        self.display(news,index=index)

    def clear(self):

        for i in self.root.pack_slaves():
            i.destroy()

    def display(self,news,index):
        #imageUrl = "https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/itjfdggt8lzfe6oizwat.jpg"
        #load = Image.open(imageUrl)
        #load = load.resize((200, 200), Image.ANTIALIAS)
        #render = ImageTk.PhotoImage(load)
        #img = Label(image=render)
        #img.image = render
        #img.pack()
        title=Label(self.root,text=news[0],fg="#000",bg="#fff")
        title.pack()
        source = Label(self.root, text=news[1], fg="#000", bg="#fff")
        source.pack()
        desc = Label(self.root, text=news[2], fg="#000", bg="#fff")
        desc.pack()

        #frame for purpose of adding button
        frame=Frame(self.root)
        frame.pack()
        if index!=0:#for edge cases
            previous=Button(frame,text="Previous",command=lambda: self.extract(index=index-1))
            previous.pack(side="left")
        # extract needs data,data needs index no to show news
        if index!=19:
            next = Button(frame, text="Next",command=lambda:self.extract(index=index+1))
            next.pack(side ="right")
obj=News()

