from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.properties import (
    ReferenceListProperty, 
    NumericProperty
)

from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line

from kivy.core.text import LabelBase


class PongBall(Widget):
    # velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # ``move`` function will move the ball one step. This
    #  will be called in equal intervals to animate the ball
    # this is btw a user defined function and not some kind of
    # event that triggers an action when it happens
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
    pass

class PongApp(App):
    def build(self):
        pong_game = PongGame()
        return pong_game


if __name__ == '__main__':
    LabelBase.register(
        name='Poppins',
        fn_regular='D:/Projects/To Github/project-seraphim/shop-visual-aids/data science gig/Poppins-Regular.ttf'
    )
    # runs our application infinitely to keep window open
    # this is bascially how most apps run, they run infinitely
    # until an event is triggered through a button perhaps that
    # closes them
    PongApp().run()