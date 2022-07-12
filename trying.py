import tkinter as tk
import json

app = tk.Tk()

text = tk.Text(app)

text.pack()
with open("employee.json","r")as file:
    data = json.load(file)
json_val = json.load(data)

for k in data:
    text.insert(tk.END, '{} = {}\n'.format(k, data[k]))
text.config(state = tk.DISABLED)
app.mainloop()
