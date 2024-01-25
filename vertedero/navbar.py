import reflex as rx
navbar_height = "3em"
navbar_color = "#f2eedf"
navbar_style = {
    "position": "fixed",
    "width": "100%",  # Ensure the navbar spans the full width
    "height": navbar_height,
    "padding": "0 1em",
    "display": "flex",
    "justify-content": "space-between",  # This spreads out the items on the navbar
    "align-items": "center",
    "background-color": "#38383A",
    "box-shadow": "0 0.2em 0.4em rgba(0,0,0,.1)",
    "font-size": "1.2em",
    "color": "white"
}

class WebDomains:
    main = "https://vertedero-senor-caballero.reflex.run/"
    cnn = "https://vertedero-senor-caballero.reflex.run/cnn/"

class LocalDomains:
    main = "http://localhost:3000/"
    cnn = "http://localhost:3000/cnn/"


def navbar():
    return rx.box(
        rx.link(
            rx.text("El Rincón del Caballero"),
            href=LocalDomains.main,
            ),
        rx.link(
            "Sobre mí",
            href="https://danimoreno.reflex.run/",
        ),
        # If you have other navbar items, you can include them here
        style=navbar_style
    )
