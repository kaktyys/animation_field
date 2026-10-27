import tkinter as tk
from src.models.animation_model import StarModel

WIDTH = 800
HEIGHT = 600
FOV = 400
MAX_DEPTH = 1000
NUM_STARS = 250


class StarfieldApp:

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Звездное поле 3D")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.center_x = WIDTH // 2
        self.center_y = HEIGHT // 2
        self.speed = 15

        self.stars = [StarModel(WIDTH, HEIGHT, MAX_DEPTH) for _ in range(NUM_STARS)]

        self.root.bind("<KeyPress>", self.handle_keypress)
        self.root.bind("<Motion>", self.handle_mouse_motion)

        self.animate()

    def handle_keypress(self, event: tk.Event):
        if event.keysym == "Up":
            self.speed = min(self.speed + 2, 50)
        elif event.keysym == "Down":
            self.speed = max(self.speed - 2, 1)

    def handle_mouse_motion(self, event: tk.Event):
        self.center_x = event.x
        self.center_y = event.y

    def animate(self):
        self.canvas.delete("all")

        self.stars.sort(key=lambda s: s.z, reverse=True)

        for star in self.stars:
            star.update(self.speed)
            sx = int(self.center_x + (star.x / star.z) * FOV)
            sy = int(self.center_y + (star.y / star.z) * FOV)
            radius = max(1, int((MAX_DEPTH - star.z) / 150) + 1)

            if 0 <= sx <= WIDTH and 0 <= sy <= HEIGHT:
                self.canvas.create_oval(
                    sx - radius, sy - radius,
                    sx + radius, sy + radius,
                    fill=star.color, outline=""
                )

        self.canvas.create_text(
            90, 20,
            text=f"Скорость (Вверх/Вниз): {self.speed}",
            fill="#A0A0A0", font=("Arial", 10, "bold")
        )
        self.root.after(16, self.animate)
