"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

from .navbar import navbar, navbar_height

from .merge import merge
import reflex as rx
from .pages.cnn.cnn import index as cnn

######################################### Styles #########################################
background_color = "#cccccc"
shadow_color = "#B1D4E0"

class WebDomains:
    main = "https://vertedero-senor-caballero.reflex.run/"
    cnn = "https://vertedero-senor-caballero.reflex.run/cnn/"

class LocalDomains:
    main = "http://localhost:3000/"
    cnn = "http://localhost:3000/cnn/"

class Styles:
    General = {
        "background": background_color,
        "font": "Arial, sans-serif",
        "color": "white",
        "height": "100vh",
        "width": "100vw",
        "top": "4em",
        "left": "0",
        # "margin-top": "2em"

    }
    Header = {
        "font": "bold",
        "text-align": "center",
        "font-size": "2.5rem",
        "color": "#EFEFEF",
        "margin-bottom": "0px",
        "padding-top": navbar_height,
    }
    Post = {
    "display": "block",
    "color_title": "#EFEFEF",
    "size_title": "2em",
    "margin_title": "0.5em 0",
    "color_text": "#BBBBBB",
    "margin_bottom_text": "1.5em",
    "size_text": "1em",
    "color": "black",
    "background": "#f2eedf",
    "border-radius": "0.5em",
    "padding": "1em",
    "margin": "1em auto",  # Center the card
    "max-width": "800px",  # Maximum width of the card
    "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.2)",  # Adds shadow for depth
    "transition": "0.3s",  # Smooth transition for mouse hover effects
    
    # Center the letters
    "text-align": "center",
    }

    Title_Post = {
        "font-size": "2em",
        "marging": "0.5em 0",
    }
    Explanation_Post = {
        "font-size": "1.1em",
    }
    # sidebar_link = {
    #     "color": "white",
    #     "hover": {
    #         "background-color": "#2E3A58",  # Soft blue for hover state
    #     },
    #     "display": "block",  # Ensure each link is on a new line
    #     "padding": "0.5em 1em",  # Add padding inside each link for better spacing
    #     "text-decoration": "none",
    #     "margin-bottom": "1em"  # Add margin to the bottom of each link
    # }
    content = {
        "margin-left": "15em",  # Match the width of the sidebar
        "margin-top": "3em",  # Match the height of the navbar
        "padding": "1em",
        "background-color": background_color,
        "height": "100vh",
        "width": "100vw",
        "color": "black"
    }



class State(rx.State):
    """The app state."""

    pass

######################################### Home #########################################

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            rx.box(
                rx.text("Bienvenido, espero que disfrute de la lectura", style=Styles.Header),
            ),
            rx.box(
                rx.box(
                    rx.link('Convolutional Neural Networks', href=LocalDomains.cnn, style=Styles.Title_Post),
                    rx.text("A brief introduction to CNNs", style=Styles.Explanation_Post),
                    style=Styles.Post
                )
            ),
            rx.box(
                rx.box(
                    rx.link('How to choose a bachelor', href=LocalDomains.cnn, style=Styles.Title_Post),
                    rx.text("Brief comment about a viral table", style=Styles.Explanation_Post),
                    style=Styles.Post
                )
            ),
            rx.box(
                rx.box(
                    rx.link('Do we live worse than our parents', href=LocalDomains.cnn, style=Styles.Title_Post),
                    rx.text("Brief discussion about it", style=Styles.Explanation_Post),
                    style=Styles.Post
                )
            ),
            style=Styles.General
        )
    )


######################################### About me #########################################
# def sidebar():
#     return rx.box(
#         rx.link("HOME", style=Styles.sidebar_link),
#         rx.link("BIO", style=Styles.sidebar_link),
#         rx.link("PRESS", style=Styles.sidebar_link),
#         # Add more links as needed
#         style=Styles.sidebar
#     )




# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.add_page(cnn, route="/cnn")
