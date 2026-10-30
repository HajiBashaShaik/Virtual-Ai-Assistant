
import tkinter as tk
from tkinter import *
import speech_to_text
import action

# ---------------- MAIN WINDOW ----------------

root = Tk()
root.title("VIRTUAL - AI Assistant")
root.geometry("760x820")
root.minsize(650, 700)
root.config(bg="#101827")

BG = "#101827"
HEADER = "#17243A"
PANEL = "#202D40"
BLUE = "#476FD1"
USER_COLOR = "#354D83"
TEXT_COLOR = "#FFFFFF"
MUTED = "#AAB8CE"

# ---------------- HEADER ----------------

header = Frame(root, bg=HEADER, height=85)
header.pack(fill=X)
header.pack_propagate(False)

logo = Label(
    header,
    text="🤖",
    font=("Arial", 27),
    bg=HEADER
)
logo.pack(side=LEFT, padx=20)

title_frame = Frame(header, bg=HEADER)
title_frame.pack(side=LEFT, pady=17)

Label(
    title_frame,
    text="VIRTUAL AI ASSISTANT",
    font=("Arial", 16, "bold"),
    fg=TEXT_COLOR,
    bg=HEADER
).pack(anchor="w")

Label(
    title_frame,
    text="● Online  |  Your Personal AI Assistant",
    font=("Arial", 9),
    fg="#35D49A",
    bg=HEADER
).pack(anchor="w")

# ---------------- CHAT AREA ----------------

chat_frame = Frame(root, bg=BG)
chat_frame.pack(fill=BOTH, expand=True, padx=20, pady=15)

scrollbar = Scrollbar(chat_frame)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(
    chat_frame,
    bg=BG,
    fg=TEXT_COLOR,
    font=("Arial", 12),
    wrap=WORD,
    bd=0,
    padx=15,
    pady=15,
    state=DISABLED,
    yscrollcommand=scrollbar.set
)

text.pack(fill=BOTH, expand=True)

scrollbar.config(command=text.yview)

# Message styles

text.tag_configure(
    "user",
    foreground="#8FB5FF",
    font=("Arial", 11, "bold"),
    spacing1=12
)

text.tag_configure(
    "bot",
    foreground="#35D49A",
    font=("Arial", 11, "bold"),
    spacing1=12
)

text.tag_configure(
    "message",
    foreground=TEXT_COLOR,
    font=("Arial", 11),
    lmargin1=15,
    lmargin2=15,
    spacing3=8
)

text.tag_configure(
    "center",
    foreground=MUTED,
    font=("Arial", 10),
    justify=CENTER,
    spacing3=15
)


# ---------------- DISPLAY MESSAGES ----------------

def add_message(sender, message):

    text.config(state=NORMAL)

    if sender == "USER":
        text.insert(END, "\nYOU\n", "user")

    else:
        text.insert(END, "\nNOVA AI\n", "bot")

    text.insert(END, str(message) + "\n", "message")

    text.config(state=DISABLED)
    text.see(END)


# Welcome message

text.config(state=NORMAL)

text.insert(
    END,
    "\n\n🤖\nWELCOME TO AI ASSISTANT\n",
    "center"
)

text.insert(
    END,
    "Your personal assistant is ready.\n"
    "Ask me anything or give me a command!\n",
    "center"
)

text.config(state=DISABLED)


# ---------------- ASK FUNCTION ----------------

def ask():

    status.config(text="Listening...", fg="#35D49A")

    root.update_idletasks()

    user_val = speech_to_text.speech_to_text()

    if user_val is None or not user_val.strip():

        add_message(
            "BOT",
            "Sorry, I couldn't understand your voice."
        )

        status.config(text="Online", fg="#35D49A")
        return

    add_message("USER", user_val)

    bot_val = action.Action(user_val)

    if bot_val is not None:
        add_message("BOT", bot_val)

    status.config(text="Online", fg="#35D49A")

    if bot_val == "Completed":
        root.destroy()


# ---------------- SEND FUNCTION ----------------

def send():

    user_val = entry.get().strip()

    if not user_val:
        return

    entry.delete(0, END)

    add_message("USER", user_val)

    bot_val = action.Action(user_val)

    if bot_val is not None:
        add_message("BOT", bot_val)

    if bot_val == "Completed":
        root.destroy()


# ---------------- CLEAR FUNCTION ----------------

def del_text():

    text.config(state=NORMAL)

    text.delete("1.0", END)

    text.insert(
        END,
        "\n\n🤖\nCHAT CLEARED\n"
        "Start a new conversation!\n",
        "center"
    )

    text.config(state=DISABLED)


# ---------------- STATUS ----------------

status_frame = Frame(root, bg=BG)
status_frame.pack(fill=X, padx=25)

status = Label(
    status_frame,
    text="Online",
    font=("Arial", 9),
    fg="#35D49A",
    bg=BG
)

status.pack(anchor="w")


# ---------------- INPUT AREA ----------------

input_frame = Frame(
    root,
    bg=HEADER,
    padx=12,
    pady=12
)

input_frame.pack(fill=X, padx=20, pady=15)

entry = Entry(
    input_frame,
    font=("Arial", 12),
    bg=PANEL,
    fg=TEXT_COLOR,
    insertbackground=TEXT_COLOR,
    relief=FLAT,
    bd=0
)

entry.pack(
    side=LEFT,
    fill=X,
    expand=True,
    ipady=12,
    padx=8
)

entry.insert(0, "Type your message...")

def clear_placeholder(event):

    if entry.get() == "Type your message...":
        entry.delete(0, END)

entry.bind("<FocusIn>", clear_placeholder)
entry.bind("<Return>", lambda event: send())


# ---------------- BUTTONS ----------------

ask_button = Button(
    input_frame,
    text="🎤",
    font=("Arial", 15),
    bg=BLUE,
    fg="white",
    relief=FLAT,
    cursor="hand2",
    command=ask
)

ask_button.pack(side=LEFT, padx=5, ipadx=8, ipady=5)


send_button = Button(
    input_frame,
    text="➤",
    font=("Arial", 16, "bold"),
    bg="#35A77D",
    fg="white",
    relief=FLAT,
    cursor="hand2",
    command=send
)

send_button.pack(side=LEFT, padx=5, ipadx=8, ipady=5)


# ---------------- CLEAR CHAT ----------------

clear_button = Button(
    root,
    text="Clear Conversation",
    font=("Arial", 9),
    bg=BG,
    fg=MUTED,
    activebackground=BG,
    activeforeground=TEXT_COLOR,
    relief=FLAT,
    cursor="hand2",
    command=del_text
)

clear_button.pack(pady=(0, 12))


# ---------------- RUN APPLICATION ----------------

root.mainloop()
