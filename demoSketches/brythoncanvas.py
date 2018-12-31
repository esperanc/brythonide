from browser import document, html
import math

body = document.select("body")[0]
canvas = html.CANVAS(width=400, height=400)
body <= canvas
context = canvas.getContext("2d")
context.fillStyle = "white";

def draw (event):
    if not event.buttons: return
    context.beginPath();
    context.arc(event.offsetX, event.offsetY, 40, 0, 2 * math.pi)
    context.fill()
    context.stroke()

canvas.bind("mousedown", draw)
canvas.bind("mousemove", draw)