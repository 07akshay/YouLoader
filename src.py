def Down(name):
    links =[]
    query = name+" "+"youtube"
    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
        links.append(j)
    yt = YouTube(links[0],on_progress_callback=progress_Check)
    e.delete(0,END)
    print("starting")
    stream = yt.streams.first()
    stream.download()

    response = messagebox.showinfo("Progress","Download Successful!!")
    today = date.today()
    conn = sqlite3.connect('down.db')
    c = conn.cursor() 
    c.execute("INSERT INTO past_downloads VALUES (:f_name, :date)",
             {
                 'f_name': name,
                 'date': today
             })
    conn.commit()
    conn.close()
    root.filename = filedialog.askopenfilename(initialdir="/home/akshay",title = "select a file",filetypes=[("mp4","*.mp4")])
    res = messagebox.askquestion("Confirmation","Do you want to play it??")
    if res =="yes":
        video(root.filename)