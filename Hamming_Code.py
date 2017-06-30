from tkinter import *
root =Tk()


def sender():
    d = sinp.get()
    data = [int(x) for x in str(d)]

    codeword = []
    pow2 = [int(pow(2, x)) for x in range(0, 5)]
    codeword.append(-5)
    j = 0
    for i in range(1, 17):
        if (j < len(data)):
            if (i not in pow2):
                codeword.append(int(data[j]))
                j = j + 1
            else:
                codeword.append(-1)
        else:
            codeword.append(5)

    j = codeword.count(5)
    for i in range(1, j + 1):
        codeword.remove(5)



    r = [0 for i in range(6)]

    t1 = []
    t2 = []
    t3 = []
    t4 = []

    t1.append(0)
    t2.append(0)
    t3.append(0)
    t4.append(0)

    for i in range(1, 17):
        t1.append(1 ^ t1[i - 1])

        if t1[i - 1] == 1:
            t2.append(1 ^ t2[i - 1])
        else:
            t2.append(t2[i - 1])

        if t1[i - 1] == 1 and t2[i - 1] == 1:
            t3.append(1 ^ t3[i - 1])
        else:
            t3.append(t3[i - 1])

        if t1[i - 1] == 1 and t2[i - 1] == 1 and t3[i - 1] == 1:
            t4.append(1 ^ t4[i - 1])
        else:
            t4.append(t4[i - 1])

    for i in range(0, len(codeword)):
        if codeword[i] != -1 and codeword[i] != -5:
            if t1[i] == 1:
                r[1] = r[1] ^ codeword[i]

            if t2[i] == 1:
                r[2] = r[2] ^ codeword[i]

            if t3[i] == 1:
                r[3] = r[3] ^ codeword[i]

            if t4[i] == 1:
                r[4] = r[4] ^ codeword[i]

    for i in range(1, 5):
        print(r[i])

    rbit=' '
    for i in range(1,len(r)):
        rbit+="   "+str(r[i])
    print(rbit)

    j = 1
    for i in pow2:
        if i < len(codeword):
            codeword[i] = r[j]
            j += 1

    print(codeword[1:])
    sendword=' '


    for i in range(1,len(codeword)):
        sendword+=str(codeword[i])
    print(sendword)
    sender1 = Label(root, text="The Hamming code is  ")
    sender2 = Label(root, text=sendword)
    sender3 = Label(root, text="The Redundant bit is ")
    sender4 = Label(root, text=rbit)

    sender1.grid(row=9)
    sender2.grid(row=9,column=1)
    sender3.grid(row=10)
    sender4.grid(row=10, column=1)


def reciver():
    codeword=[]
    d = rinp.get()
    data = [int(x) for x in str(d)]
    codeword.append(-5)
    j = 0
    for i in range(0, len(data)):
        codeword.append(int(data[i]))

    print(codeword)



    s = [0 for i in range(5)]

    t1 = []
    t2 = []
    t3 = []
    t4 = []

    t1.append(0)
    t2.append(0)
    t3.append(0)
    t4.append(0)

    for i in range(1, 17):
        t1.append(1 ^ t1[i - 1])

        if t1[i - 1] == 1:
            t2.append(1 ^ t2[i - 1])
        else:
            t2.append(t2[i - 1])

        if t1[i - 1] == 1 and t2[i - 1] == 1:
            t3.append(1 ^ t3[i - 1])
        else:
            t3.append(t3[i - 1])

        if t1[i - 1] == 1 and t2[i - 1] == 1 and t3[i - 1] == 1:
            t4.append(1 ^ t4[i - 1])
        else:
            t4.append(t4[i - 1])


    for i in range(0, len(codeword)):
        if codeword[i] != -1 and codeword[i] != -5:
            if t1[i] == 1:
                s[1] = s[1] ^ codeword[i]

            if t2[i] == 1:
                s[2] = s[2] ^ codeword[i]

            if t3[i] == 1:
                s[3] = s[3] ^ codeword[i]

            if t4[i] == 1:
                s[4] = s[4] ^ codeword[i]

    print(s[4],s[3],s[2],s[1])
    s.reverse()

    error=' '
    for i in range(0,4):
        error+=str(s[i])
    print(error)
    reciver1 = Label(root, text="The error pos is  ")
    reciver2 = Label(root, text=error)

    reciver1.grid(row=9,column=3)
    reciver2.grid(row=9, column=4)






rinp=StringVar()
sinp=StringVar()
button1=Button(root,text="submit data word ",command=sender)
button2=Button(root,text="submit recived word ",command=reciver)

thelabel=Label(root,text="Hamming code")
thelabe2=Label(root,text="Hamming codes are a family of linear error-correcting codes  that generalize the Hamming(7,4)-code")
thelabe3=Label(root,text="and were invented by Richard Hamming in 1950. Hamming codes can detect up to two-bit errors or ")
thelabe4=Label(root,text="correct one-bit errors without detection of uncorrected errors.")
sender_label=Label(root,text="Enter the data bits in (in binary) ")
reciver_label=Label(root,text="Enter the recived bits in (in binary) ")


sender_entry=Entry(root,textvariable=sinp)
reciver_entry=Entry(root,textvariable=rinp)


thelabel.grid(row=0,column=2)
thelabe2.grid(row=1,column=2)
thelabe3.grid(row=2,column=2)
thelabe4.grid(row=3,column=2)

sender_label.grid(row=6)
reciver_label.grid(row=6,column=3)

sender_entry.grid(row=7)
reciver_entry.grid(row=7,column=3)

button1.grid(row=8)
button2.grid(row=8,column=3)




root.mainloop()
