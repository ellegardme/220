"""
Name: Madeleine Ellegard
vigenere.py

Problem: To survey the amount of cars that travel on roads

Certification of Authenticity:
I certify that this assignment is entirely my own work, but I discussed it with laura
"""
import graphics


def code(message, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    acc = ""
    for i in range(len(message)):
        val_mes_chr = alphabet.index(message[i].upper().strip())
        val_key_chr = alphabet.index(keyword[i % len(keyword)].upper())
        acc += alphabet[(val_key_chr + val_mes_chr) % len(alphabet)]
    return acc


def main():
    # The window set up
    width = 400
    height = 400
    win = graphics.GraphWin("Vigenere", width, height)

    # Message
    message_pt = graphics.Point(60, 100)
    message_txt = graphics.Text(message_pt, "Message to code")
    message_txt.draw(win)
    ui_pt = graphics.Entry(graphics.Point(200, 100), 20)
    ui_pt.draw(win)

    # Entry
    keyword_pt = graphics.Point(60, 150)
    keyword_txt = graphics.Text(keyword_pt, "Enter Keyword")
    keyword_txt.draw(win)
    txt = graphics.Entry(graphics.Point(200, 150), 20)
    txt.draw(win)

    # Button
    encode_text = graphics.Text(graphics.Point(200, 250), "Encode")
    encode_outline = graphics.Rectangle(graphics.Point(150, 225), graphics.Point(250, 275))
    encode_text.draw(win)
    encode_outline.draw(win)

    # functions
    win.getMouse()
    message = ui_pt.getText()
    keyword = txt.getText()
    result = code(message, keyword)
    encode_text.undraw()
    encode_outline.undraw()

    output_text = graphics.Text(graphics.Point(300, 300), "Resulting Message \n" + result)
    output_text.draw(win)

    # Ends the program
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
