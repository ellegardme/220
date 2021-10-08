"""
Name: Madeleine Ellegard
traffic.py

Problem: To survey the amount of cars that travel on roads

Certification of Authenticity:
I certify that this assignment is entirely my own work, but I discussed it with Logan
"""
import graphics


def main():
    # The window set up
    width = 400
    height = 400
    win = graphics.GraphWin("Greeting", width, height)

    # Text Box
    message_pt = graphics.Point(width / 2, 10)
    message = graphics.Text(message_pt, "Happy Valentine's Day!")
    message.draw(win)

    # Heart
    heart_image = graphics.Image(graphics.Point(200, 200), "giphy.gif")
    heart_image.draw(win)

    # Arrow
    arrow = graphics.Line(graphics.Point(0, 400), graphics.Point(50, 350))
    arrow.setArrow("last")
    arrow.draw(win)

    # Loop
    for _ in range(15):
        graphics.time.sleep(0.1)
        arrow.move(30, -30)
    end_message = graphics.Point(width / 2, 375)
    end = graphics.Text(end_message, "Click to end program")
    end.draw(win)

    # Ends the program
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
