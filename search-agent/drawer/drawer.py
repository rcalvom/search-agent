from tkinter import *

from drawer.models import *

class Drawer:



    def __init__(self):
        self.cell_size = 50
        self.canvas = Canvas(width=31 * self.cell_size, height=14 * self.cell_size, background='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        self.colors = [
            '#0000FF',
            '#FF7F50',
            '#DC143C',
            '#8B008B',
            '#228B22',
            '#808000',
            '#D3D3D3',
            '#B8860B',
            '#FF00FF',
            '#FFD700'
        ]
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

        self.canvas.create_rectangle(
            20 * self.cell_size,
            3 * self.cell_size,
            20 * self.cell_size + 10 * self.cell_size ,
            3 * self.cell_size + 10 * self.cell_size,
            outline='black',
            width=3
        )
        # Draw laminates
        for index, laminate in enumerate(status.laminates):
            if laminate.rotation == Rotation.VERTICAL:
                self.canvas.create_rectangle(
                    self.cell_size * laminate.x + self.cell_size + laminate.sheet * self.cell_size * 19,
                    self.cell_size * laminate.y + 3 * self.cell_size,
                    self.cell_size * laminate.x +self.cell_size + laminate.sheet * self.cell_size * 19 + self.cell_size * Status.laminate_dimensions[index][0],
                    self.cell_size * laminate.y + 3 * self.cell_size + self.cell_size * Status.laminate_dimensions[index][1],
                    outline=self.colors[index],
                    width=2,
                    fill=self.colors[index],
                    stipple="gray50"
                    
                )
            else:
                self.canvas.create_rectangle(
                    self.cell_size * laminate.x + self.cell_size + laminate.sheet * self.cell_size * 19,
                    self.cell_size * laminate.y + 3 * self.cell_size,
                    self.cell_size * laminate.x + self.cell_size + laminate.sheet * self.cell_size * 19 + self.cell_size * Status.laminate_dimensions[index][1],
                    self.cell_size * laminate.y + 3 * self.cell_size + self.cell_size * Status.laminate_dimensions[index][0],
                    outline=self.colors[index],
                    width=2,
                    fill=self.colors[index],
                    stipple="gray50"
                )
        mainloop()
