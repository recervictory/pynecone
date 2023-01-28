"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    colors = ["black", "red", "green", "blue", "purple"]
    index = 0
    
    def next_color(self):
        self.index = (self.index + 1) % len(self.colors)
    
    #Todo: Computed vars: Computed properties are properties that are computed from other properties. 
    @pc.var
    def color(self):
        return self.colors[self.index]

def index():
    return pc.center(
        pc.vstack(
            pc.heading("Welcome to Pynecone!", 
                       font_size="2em",
                       on_click= State.next_color,
                       color=State.color,
                       _hover={"cursor": "pointer"}
                       ),  
        ),
    )

def about():
    return pc.text('About Page')



# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.add_page(about)
app.compile()
