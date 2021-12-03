from tkinter import *

from drawer.models import *

class Drawer:

    def __init__(self):
        self.cell_size = 50
        self.canvas = Canvas(width=31 * self.cell_size, height=14 * self.cell_size, background='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        self.colors = ['#0000FF', '#FF7F50', '#DC143C', '#8B008B', '#228B22', '#808000', '#D3D3D3', '#B8860B', '#FF00FF', '#FFD700']

    def draw(self, state):
        # Draw Title

        # Draw board
        self.canvas.create_rectangle(
            self.cell_size,
            3 * self.cell_size,
            self.cell_size + 10 * self.cell_size ,
            3 * self.cell_size + 10 * self.cell_size,
            outline='#000000',
            width=3
        )

        # Draw laminates
        for index, laminate in enumerate(state.laminates):
            if laminate.used: # if the laminate is gonna be used into the board
                # width and height depends if the laminate position is horizontal(1) or vertical(0)
                width = laminate.width if laminate.rotation else laminate.height
                height = laminate.height if laminate.rotation else laminate.width
                
                self.canvas.create_rectangle(
                    self.cell_size * laminate.x + self.cell_size + 19,
                    self.cell_size * laminate.y + 3 * self.cell_size,
                    self.cell_size * laminate.x + self.cell_size + 19 + self.cell_size * width,
                    self.cell_size * laminate.y + 3 * self.cell_size + self.cell_size * height,
                    outline=self.colors[index],
                    width=2,
                    fill=self.colors[index],
                    stipple="gray50"
                )
        mainloop()
    
    def close(self):
        self.root.destroy()
