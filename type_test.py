import tkinter as tk
from time import time


class TypeTest:

    def __init__(self, root):
        self.start_time = time()
        self.end_time = None
        # timer start and end time variable initialised

        self.root = root
        self.root.title("Typing speed test")

        self.time_taken = tk.StringVar()
        self.accuracy = tk.StringVar()

        self.typed_words = tk.StringVar()

        self.title_label = tk.Label(self.root, bg="light slate grey", font="helvetica", height="3", width="50",
                                    text="Typing speed test").pack()

        self.text_to_type = tk.Label(self.root, text="Type: If I could, I would watch the welsh rugby match in Cardiff."
                                     ).pack()

        self.type_box = tk.Entry(self.root, textvariable=self.typed_words).pack()

        self.time_taken_label = tk.Label(self.root, text="Time Taken").pack()

        self.time_taken_data = tk.Label(self.root, textvariable=self.time_taken).pack()

        self.typed_words_label = tk.Label(self.root, text="Typed Words").pack()

        self.typed_words_data = tk.Label(self.root, textvariable=self.typed_words).pack()

        self.start_button = tk.Button(self.root, command=lambda: self.check_result(), text="check", bg="light cyan"
                                      ).pack()

    def check_result(self):
        if self.typed_words.get() == "If I could, I would watch the welsh rugby match in Cardiff.":
            self.end_time = time()
            # measure time at finish
            self.time_taken.set(f"{round(self.end_time - self.start_time, 2)} seconds")
            # set the time as the the time at both points subtracted


if __name__ == "__main__":
    r = tk.Tk()
    t = TypeTest(r)
    t.root.mainloop()
