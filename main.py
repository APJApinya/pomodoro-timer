from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset(timer_text, timer_label,checkmark_label):
    window.after_cancel(timer) # cancel refreshing windows activity
    #timer 00:00
    canvas.itemconfig(timer_text, text="00:00")
    #titel_label "Timer"
    timer_label.config(text="Timer", fg = GREEN)
    #reset checkmark
    global marks
    marks = ""
    checkmark_label.config(text=marks)
    #reset reps
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global label
    reps+=1
    working_seconds = WORK_MIN * 60
    short_rest_seconds = SHORT_BREAK_MIN * 60
    long_rest_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_rest_seconds)

    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_rest_seconds)

    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(working_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# import time
#
# count = 5
# while True:
#     time.sleep(1)
#     count -= 1
# we should not loop inside the window loop

def count_down(count):

    count_min = math.floor(count/60) # return the whole number
    count_second = str(count % 60).zfill(2) # python unique functionality

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1) # it will run after 1 sec
        # 1000 is 1sec, function you want to call, arguments for function, other argument
    else:
        start_timer()
        global marks
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        checkmark_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)

timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"),fg= GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2,column=0)
reset_button = Button(text="Reset", highlightthickness=0, command=lambda: reset(timer_text, timer_label, checkmark_label))
reset_button.grid(row=2,column=2)

checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(row=3,column=1)



window.mainloop()