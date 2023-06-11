from tkinter import Tk, Canvas


def creat_root():
    root = Tk()

    root.title("GUI Shop")
    root.geometry("700x600")
    root.resizable(False, False)

    return root


def create_frame():
    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)

    return frame


root = creat_root()
frame = create_frame()
