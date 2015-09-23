import scrdisplay

screen = scrdisplay.screendisplay()
text = "This is a line, a long line, a very long line, a line that has lineness to beat the line, now I'm just babbling, I hope this is more than 80 characters."
text = text * 50
screen.formatDisplayText(text)
screen.prntScreen()
