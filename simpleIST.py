import tkinter as tk
import speedtest


s = speedtest.Speedtest()


def download_p():
    dl = s.download()/1000000
    d_button.pack_forget()  # or .destroy()
    label = tk.Label(window, text=f"Download {round(dl, 2)} Mbps")
    label.pack()


def upload_p():
    up = s.upload()/1000000
    u_button.pack_forget()  # .destroy()
    label = tk.Label(window, text=f"Upload {round(up, 2)} Mbps")
    label.pack()


window = tk.Tk()
window.title("Speed Test")
d_button = tk.Button(window, text="Download", width=25, command=download_p)
d_button.pack()
u_button = tk.Button(window, text="Upload", width=25, command=upload_p)
u_button.pack()


window.mainloop()
