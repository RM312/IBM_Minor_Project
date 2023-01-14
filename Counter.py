import tkinter as tk
import tkinter.messagebox
import time


class Application(tk.Frame): 
    def __init__(nift, master, *args, **kwargs):
        tk.Frame.__init__(nift, master, *args, **kwargs)
        nift.master = master
        nift.running = False
        nift.time = 0
        nift.hours = 0
        nift.mins = 0
        nift.secs = 0
        nift.build_interface()

    def build_interface(nift):
        nift.time_entry = tk.Entry(nift)
        nift.time_entry.grid(row=0, column=1)

        nift.clock = tk.Label(nift, text="00:00:00", font=("Courier", 20), width=10)
        nift.clock.grid(row=1, column=1, stick="S")

        nift.time_label = tk.Label(nift, text="hour   min   sec", font=("Courier", 10), width=15)
        nift.time_label.grid(row=2, column=1, sticky="N")

        nift.power_button = tk.Button(nift, text="Start", command=lambda: nift.start())
        nift.power_button.grid(row=3, column=0, sticky="NE")

        nift.reset_button = tk.Button(nift, text="Reset", command=lambda: nift.reset())
        nift.reset_button.grid(row=3, column=1, sticky="NW")

        nift.quit_button = tk.Button(nift, text="Quit", command=lambda: nift.quit())
        nift.quit_button.grid(row=3, column=3, sticky="NE")

        nift.pause_button = tk.Button(nift, text="Pause", command=lambda: nift.pause())
        nift.pause_button.grid(row = 3,column=2, sticky = "NW")

        nift.master.bind("<Return>", lambda x: nift.start())
        nift.time_entry.bind("<Key>", lambda v: nift.update())

    def calculate(nift):
        """time calculation"""
        nift.hours = nift.time // 3600
        nift.mins = (nift.time // 60) % 60
        nift.secs = nift.time % 60
        return "{:02d}:{:02d}:{:02d}".format(nift.hours, nift.mins, nift.secs)

    def update(nift):
        """validation"""
        nift.time = int(nift.time_entry.get())
        try:
            nift.clock.configure(text=nift.calculate())
        except:
            nift.clock.configure(text="00:00:00")

    def timer(nift):
        """display time"""
        if nift.running:
            if nift.time <= 0:
                nift.clock.configure(text="Time's up!")
            else:
                nift.clock.configure(text=nift.calculate())
                nift.time -= 1
                nift.after(1000, nift.timer)

    def start(nift):
        """start timer"""
        try:
            nift.time = int(nift.time_entry.get())
            nift.time_entry.delete(0, 'end')
        except:
            nift.time = nift.time
        nift.power_button.configure(text="Stop", command=lambda: nift.stop())
        nift.master.bind("<Return>", lambda x: nift.stop())
        nift.running = True
        nift.timer()

    def stop(nift):
        """Stop timer"""
        nift.power_button.configure(text="Start", command=lambda: nift.start())
        nift.master.bind("<Return>", lambda x: nift.start())
        nift.running = False

    def reset(nift):
        """Resets the timer to 0."""
        nift.power_button.configure(text="Start", command=lambda: nift.start())
        nift.master.bind("<Return>", lambda x: nift.start())
        nift.running = False
        nift.time = 0
        nift.clock["text"] = "00:00:00"

    def quit(nift):
        """quit the window"""
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            rm.destroy()

    def pause(nift):
        """Pause timer"""
        nift.pause_button.configure(text="Resume", command=lambda: nift.resume())
        nift.master.bind("<Return>", lambda x: nift.resume())
        if nift.running == True:
            nift.running = False
        nift.timer()
      

    def resume(nift):
        """Resume timer"""
        nift.pause_button.configure(text="Pause", command=lambda: nift.pause())
        nift.master.bind("<Return>", lambda x: nift.pause())
        if nift.running == False:
            nift.running = True
        nift.timer()
       

            


if __name__ == "__main__":
    """Main loop of timer"""
    rm = tk.Tk()
    rm.title("TIMER")
    Application(rm).pack(side="top", fill="both", expand=True)
    rm.mainloop()
