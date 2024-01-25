import reflex as rx
from ...navbar import navbar
with open("vertedero/pages/cnn/cnn.html", "r") as f:
    html = f.read()

def index():
    return rx.box(
        navbar(),
        rx.html(html, style={"background-color": "white"}),
         rx.image(src="/download.png"),
         rx.image(src="/nn.svg"),
        style={"background-color": "white"}
    )