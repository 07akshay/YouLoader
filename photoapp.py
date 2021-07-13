global nu
nu = 0
def forward():
    global my_label
    global nu
    global nex
    global prev
    if nu<4:
        nu = nu+1
    my_label.grid_forget()
    my_label = Label(root,image=img_lst[nu])
    my_label.grid(row=0,column=0,columnspan=4)
    if nu==4:
        nex=Button(frame,text="next",borderwidth=2,padx=30,command =forward,state=DISABLED,fg='black',bg='white',font = Desired_font)
        nex.grid(row=1,column=2)
    else:
        prev=Button(frame,text="prev",borderwidth=2,padx=30,command =backward,fg='black',bg='white',font = Desired_font)
        prev.grid(row=1,column=0)
    return


def backward():
    global my_label
    global nu
    global nex
    global prev
    if nu>0:
        nu=nu-1
    my_label.grid_forget()
    my_label = Label(root,image=img_lst[nu])
    my_label.grid(row=0,column=0,columnspan=4,sticky=W+E)
    if nu==0:
        prev=Button(frame,text="prev",borderwidth=2,padx=30,command =backward,state=DISABLED,fg='black',bg='white',font = Desired_font)
        prev.grid(row=1,column=0)
    else:
        nex=Button(frame,text="next",borderwidth=2,padx=30,command =forward,fg='black',bg='white',font = Desired_font)
        nex.grid(row=1,column=2)
    return