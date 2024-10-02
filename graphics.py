import tkinter

tk = tkinter.Tk()
tk.geometry("500x500")

canvas = tkinter.Canvas(tk, width=500, height=500)
canvas.pack()

RADIUS = 10

def createNode(x, y, distance):
    colour = int(255*(1-distance))
    hex_color = f"#{colour:02x}0000"  # Convert to hexadecimal
    return create_circle(x, y, RADIUS, hex_color)
    #return canvas.create_oval(x-(RADIUS*(1.2-distance)), y-(RADIUS*(1.2-distance)), x+(RADIUS*(1.2-distance)), y+(RADIUS*(1.2-distance)), outline="", fill=hex_color)


def createControl(x, y, distance):
    colour = int(255*(1-distance))
    hex_color = f"#{colour:02x}{colour:02x}{colour:02x}"  # Convert to hexadecimal
    return create_circle(x, y, RADIUS, hex_color)
    #return canvas.create_oval(x-(RADIUS*(1.2-distance)), y-(RADIUS*(1.2-distance)), x+(RADIUS*(1.2-distance)), y+(RADIUS*(1.2-distance)), outline="", fill=hex_color)

def create_circle(x, y, r,fill):
    return canvas.create_oval(x-r, y-r, x+r, y+r, outline="",fill=fill)

controls = [(100,100,0),(300,200,0.6),(300,300,0.6),(100,400,0)]
for con in controls:
    createControl(con[0], con[1], con[2])

for ran1 in range(100):
    u= ran1/100
    for ran2 in range(100):
        v=ran2/100
        point = [0,0,0]
        for i in range(3):
            b1 = controls[0][i]*((1-u)**3)*((1-v)**3)
            b2 = controls[1][i]*(3*u*(1-u)**2)*(3*v*(1-v)**2)
            b3 = controls[2][i]*(3*(u**2)*(1-u))*(3*(v**2)*(1-v))
            b4 = controls[3][i]*(u**3)*(v**3)
            point[i] = b1 + b2 + b3 + b4
        createNode(point[0], point[1], point[2])
tk.mainloop()