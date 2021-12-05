from tkinter import *

from agent.hill_climbing.models import *
import time

class Drawer:

    def __init__(self, title):
        # Constants
        self.cell_size = 50
        self.colors = ['#0000FF', '#FF7F50', '#DC143C', '#8B008B', '#228B22', '#808000', '#D3D3D3', '#B8860B', '#FF00FF', '#FFD700']

        # Windows initialization
        self.window = Tk()
        self.window.title(title)
        self.title = title

        # Canvas initialization
        self.canvas = Canvas(self.window, width=(12 * self.cell_size), height=(14 * self.cell_size), background='white')
        self.canvas.grid(column=0, row=0)

        # Variables
        self.iteration = 0
        self.state = State()

        # Objects initializacion
        self.objs = []

    def draw(self, state, iteration):
        self.state = state
        self.iteration = iteration
        for obj in self.objs:
            self.canvas.delete(obj)

        # Draw Title
        self.objs.append(self.canvas.create_text(
            6 * self.cell_size, 
            1 * self.cell_size,
            fill='#000000',
            text=self.title,
            font='Times 32 italic bold'
        ))

        # Draw Indicator
        self.objs.append(self.canvas.create_text(
            6 * self.cell_size, 
            2 * self.cell_size,
            fill='#000000',
            text='Iteración # {0}'.format(self.iteration),
            font='Times 20 bold'
        ))

        # Draw Sheet
        self.objs.append(self.canvas.create_rectangle(
            self.cell_size,
            3 * self.cell_size,
            self.cell_size + 10 * self.cell_size ,
            3 * self.cell_size + 10 * self.cell_size,
            outline='#000000',
            width=3
        ))

        # Draw laminates
        for index, laminate in enumerate(self.state.laminates):
            if laminate.placed:
                self.objs.append(self.canvas.create_rectangle(
                    self.cell_size * laminate.x + self.cell_size,
                    self.cell_size * laminate.y + 3 * self.cell_size,
                    self.cell_size * laminate.x + self.cell_size + self.cell_size * laminate.width,
                    self.cell_size * laminate.y + 3 * self.cell_size + self.cell_size * laminate.heigth,
                    outline=self.colors[index],
                    width=2,
                    fill=self.colors[index],
                    stipple="gray50"
                ))
        self.canvas.update()        
