def show():
    conn = sqlite3.connect('down.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM past_downloads")
    rec = c.fetchall()
    #     print(rec)
    print_rec=''
    mydict=[{}]
    fields= ['data']
    filename = "song_records.csv"
    for re in rec:
        print_rec += str(re) + "\n"
        mydict = mydict + [{'data':str(re)}]
    with open(filename,'w') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=fields)
        writer.writeheader()
        writer.writerows(mydict)
    qlabel = Label(root,text=print_rec)
    qlabel.grid(row=5,column=1,columnspan=4)
    qlabel.after(15000, qlabel.destroy)
    conn.commit()
    conn.close()
