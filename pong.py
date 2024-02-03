from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.properties import (
    ReferenceListProperty, 
    NumericProperty,
    ObjectProperty
)
from kivy.clock import Clock

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
    ball = ObjectProperty(None)

    def update(self, dt):
        """
        dt just means date time
        """

        # we've already defined our PongBall widget to have a
        # method self.move to move from one point to another
        self.ball.move()

        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # bounce off left and right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1

class PongApp(App):
    def build(self):
        pong_game = PongGame()

        # here since we've instantiated the pongGame class we can
        # access its method self.update and pass it as a callback
        # that Clock.schedule_interval can call over and over
        Clock.schedule_interval(pong_game.update, 1.0 / 60.0)
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