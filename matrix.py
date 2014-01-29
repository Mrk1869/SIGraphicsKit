# coding:utf-8

import numpy as np
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

class Matrix:

    def __init__(self, classes, data):
        self.margin_header = 8.0*mm
        self.margin_footer = 2.0*mm
        self.cell_size = 10.0*mm
        self.font_size = 14
        self.label_font_size = 7
        self.title_font_size = 9
        self.cvs = canvas.Canvas("out.pdf")
        self.page_width = self.margin_header + len(classes)*self.cell_size + self.margin_footer
        self.cvs.setPageSize((self.page_width, self.page_width))
        self.inverse_color = False
        self.data = data
        self.classes = classes

    def draw(self):
        color_matrix = self.calculate_color()
        for i in xrange(len(self.classes)):
            for j in xrange(len(self.classes)):
                x = self.margin_header + self.cell_size * i
                y = self.margin_footer + self.cell_size * (len(self.classes) - 1 - j )
                self.draw_data(x, y, str(self.data[j][i]), color_matrix[j][i])
        if self.inverse_color:
            self.cvs.setFillColorRGB(1, 1, 1)
        else:
            self.cvs.setFillColorRGB(0, 0, 0)
        self.draw_title()
        self.cvs.showPage()
        self.cvs.save()
        print ">> Exported a matrix to ./out.pdf"

    def calculate_color(self):
        size = len(self.data[0])
        color_matrix = [[0 for x in range(size)] for x in range(size)]

        for j in range(size):
            sum = np.sum(self.data[j])
            print sum
            for i in range(size):
                color_matrix[j][i] = 1.0 - float(self.data[j][i])/float(sum)
        return color_matrix

    def draw_data(self, x, y, text, color):
        self.cvs.setLineWidth(0.5)
        self.cvs.setFillColorRGB(color, color, color)
        self.cvs.rect(x, y, self.cell_size, self.cell_size, stroke=1, fill=1)
        if color > 0.60:
            self.cvs.setFillColorRGB(0, 0, 0)
        else:
            self.cvs.setFillColorRGB(1, 1, 1)
        font_size = self.font_size_adjust(text, self.font_size, self.cell_size)
        self.cvs.setFont("Helvetica", font_size)
        text_width = self.cvs.stringWidth(text)
        self.cvs.drawString(x + self.cell_size/2 - text_width/2,
                y + self.cell_size/2 - self.font_size/2.8, text)

    def draw_title(self):
        # Acctual class
        self.cvs.setFont("Helvetica", self.title_font_size)
        title = "Actual class"
        text_width = self.cvs.stringWidth(title)
        self.cvs.drawString(self.page_width/2 - text_width/2,
                self.page_width - self.title_font_size*1.1, title)

        font_size = self.label_font_size
        for label in self.classes:
            font_size = self.font_size_adjust(label, font_size, self.cell_size)
        for i in range(len(self.classes)):
            text = self.classes[i]
            self.cvs.setFont("Helvetica", font_size)
            text_width = self.cvs.stringWidth(text)
            x_position = self.margin_header + self.cell_size/2 - text_width/2 + self.cell_size*i
            y_position = self.margin_footer + self.cell_size * len(self.classes) + self.label_font_size/2
            self.cvs.drawString(x_position, y_position, text)

        # Predicted class
        self.cvs.rotate(90)
        self.cvs.setFont("Helvetica", self.title_font_size)
        title = "Predicted class"
        text_width = self.cvs.stringWidth(title)
        self.cvs.drawString(self.page_width/2 - text_width/2,
                - self.title_font_size*1.1, title)

        font_size = self.label_font_size
        for label in self.classes:
            font_size = self.font_size_adjust(label, font_size, self.cell_size)
        for i in range(len(self.classes)):
            text = self.classes[len(self.classes)-1 - i]
            self.cvs.setFont("Helvetica", font_size)
            text_width = self.cvs.stringWidth(text)
            x_position = self.margin_footer + self.cell_size/2 - text_width/2 + self.cell_size*i
            y_position = self.margin_header - self.label_font_size/2
            self.cvs.drawString(x_position, - y_position, text)
        self.cvs.rotate(90)

    def font_size_adjust(self, text, font_size, space_size):
        self.cvs.setFont("Helvetica", font_size)
        text_width = self.cvs.stringWidth(text)
        while text_width > space_size:
            font_size -= 1
            self.cvs.setFont("Helvetica", font_size)
            text_width = self.cvs.stringWidth(text)
        return font_size

