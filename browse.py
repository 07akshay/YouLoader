def browse():
    root.filename = filedialog.askopenfilename(initialdir="/home/akshay",title = "select a file",filetypes=[("mp4","*.mp4")])
    res = messagebox.askquestion("Confirmation","Do you want to play it??")
    if res =="yes":
        video(root.filename)