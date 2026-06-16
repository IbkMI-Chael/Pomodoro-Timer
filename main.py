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
timer = None
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
	global reps
	window.after_cancel(timer)
	canvas.itemconfig(timer_text, text = "00:00")
	timer_label.config(text = "Timer", fg = GREEN)
	checkmark_labels.config(text = "")
	reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
	global reps
	reps += 1
	work_sec = int(WORK_MIN * 60)
	short_break_sec = int(SHORT_BREAK_MIN * 60)
	long_break_sec = int(LONG_BREAK_MIN * 60)

	if reps % 2 == 1:
		timer_label.config(text = "Work", fg = GREEN)
		count_down(work_sec)
	elif reps % 2 == 0:
		timer_label.config(text = "Break", fg = PINK)
		count_down(short_break_sec)
	elif reps % 8 == 0:
		timer_label.config(text = "Break", fg = RED)
		count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
	global timer
	count_min = math.floor(count / 60)
	if count_min < 10:
		count_min = f"0{count_min}"
	count_sec = count % 60
	if count_sec < 10:
		count_sec = f"0{count_sec}"

	canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
	if count > 0:
		timer = window.after(1000, count_down, count - 1)
	else:
		start_timer()
		marks = ""
		work_sessions = math.floor(reps / 2)
		for _ in range(work_sessions):
			marks += "✔"
		checkmark_labels.config(text = marks)


# ---------------------------- UI SETUP ------------------------------- #
# Creating the window
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

# Creating the canvas
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_pic = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_pic)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)

# Labels
timer_label = Label(text = "Timer", font = (FONT_NAME, 50, "bold"), fg = GREEN, bg = YELLOW)
timer_label.grid(column = 1, row = 0)
checkmark_labels = Label(font = (FONT_NAME, 10, "normal"), bg = YELLOW, fg = GREEN)
checkmark_labels.grid(column = 1, row = 3)

# Buttons
start_btn = Button(text = "Start", highlightthickness = 0, command = start_timer)
start_btn.grid(column = 0, row = 2)
reset_btn = Button(text = "Reset", highlightthickness = 0, command = reset_timer)
reset_btn.grid(column = 2, row = 2)

##
##
##
window.mainloop()
