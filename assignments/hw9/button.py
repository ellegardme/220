from graphics import GraphWin, Point
class Button:
    def __init__(self, rectangle_shape, string_label):
        self.shape = rectangle_shape
        self.text = string_label

    def get_label(self):
        return self.text

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        if self.shape.getP1().getX() < point.getX() < self.shape.getP2().getX():
            if self.shape.getP2().getY() > point.getY() > self.shape.getP1().getY():
                return True
        return False

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)
