from tkinter import *
import speedtest

sp=Tk()
sp.title("Internet Speed Test") 
sp.geometry("360x600")
sp.config(bg="#1a212d")
sp.resizable(False,False)

def check():
    test=speedtest.Speedtest()
    Uploading=round(test.upload()/(1024*1024),2)
    upload.config(text=Uploading)

    downloading=round(test.download()/(1024*1024),2)
    download.config(text=downloading)
    Download.config(text=downloading)

    servernames=[]
    test.get_servers(servernames)
    ping.config(text=test.results.ping)

image_icon=PhotoImage(file="logo.png")
sp.iconphoto(False,image_icon)

top=PhotoImage(file="top.png")
Label(sp,image=top,bg="#1a212d").pack()

main=PhotoImage(file="main.png")
Label(sp,image=main,bg="#1a212d").pack(pady=(40,0))

button=PhotoImage(file="button.png")
Button=Button(sp,image=button,bg="#1a212d",bd=0,activebackground="#1a212d",cursor="hand2",command=check)
Button.pack(pady=10)

Label(sp,text="PING",font="arial 10 bold",bg="#384056").place(x=50,y=0)
Label(sp,text="DOWNLOAD",font="arial 10 bold",bg="#384056").place(x=140,y=0)
Label(sp,text="UPLOAD",font="arial 10 bold",bg="#384056").place(x=260,y=0)

Label(sp,text="MS",font="arial 7 bold",bg="#384056",fg="white").place(x=60,y=80)
Label(sp,text="MBPS",font="arial 7 bold",bg="#384056",fg="white").place(x=165,y=80)
Label(sp,text="MBPS",font="arial 7 bold",bg="#384056",fg="white").place(x=275,y=80)

Label(sp,text="Download",font="arial 15 bold",bg="#384056",fg="white").place(x=138,y=270)
Label(sp,text="MBPS",font="arial 13 bold",bg="#384056",fg="white").place(x=158,y=380)

ping=Label(sp,text="00",font="arial 13 bold",bg="#384056",fg="white")
ping.place(x=70,y=60,anchor="center")

download=Label(sp,text="00",font="arial 13 bold",bg="#384056",fg="white")
download.place(x=180,y=60,anchor="center")

upload=Label(sp,text="00",font="arial 13 bold",bg="#384056",fg="white")
upload.place(x=290,y=60,anchor="center")

Download=Label(sp,text="00",font="arial 40 bold",bg="#384056",fg="white")
Download.place(x=185,y=340,anchor="center")

sp.mainloop()


