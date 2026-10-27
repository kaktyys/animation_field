import tkinter as tk
from src.app import StarfieldApp


def main():
    root = tk.Tk()
    StarfieldApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
