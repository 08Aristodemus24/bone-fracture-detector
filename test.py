from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.graphics import Color, Ellipse, Line


# There are many widgets built in, such as buttons, sliders and other common stuff
# akin to the elements we dynamically create in javascript and then add to the dom
# through dom operations
class MyPaintWidget(Widget):
    # this is basically how we add event listeners to our application
    # and trigger an action upon the happening of an event which in this
    # case is a touch down or tap of our phone event
    def on_touch_down(self, touch):
        # the touch variable/argumetn here actually prints
        # <MouseMotionEvent spos=(0.2390488110137672, 0.7579298831385642) pos=(191.0, 454.0)>
        # <MouseMotionEvent spos=(0.8410513141426783, 0.7412353923205341) pos=(672.0, 443.99999999999994)> 
        # where the values of pos are actually attributes of 
        # this mousemotionevent object that consists of an x
        # and y coordinate respectively e.g. 191.0 and 454.0
        # in this case to where in the black screen of the app 
        # we clicked down on our mouse with
        print(touch)

        # We use Python’s with statement with the widget’s Canvas object. 
        # This is like an area in which the widget can draw things to 
        # represent itself on the screen
        with self.canvas:
            # here the arguments of the COlor class represent
            # the RGB color values, so this means 1 for red, 1
            # for green and 0 for blue, which actually results in
            # a color of yellow

            # the RGB values of color are actually normalized such that
            # instead of 0 to 255 values for each three RGB values, we have our
            #     values ranging from 0 to 1 inclusively, this is why 1, 1, 0 is
            # yellow because when unnormalized it is actually 255, 255, 0 which is
            # yellow not almost a black color since 1, 1, 0 is technically black
            Color(1, 1, 0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))

            # here we use the touch object again and set the ud attributes
            # dictionary line key to a Line object that takes in the position
            # in the black screen we pressed our mouse left click down with

            # I believe line here is a setter function that populates further a points
            # attribute
            touch.ud['line'] = Line(points=(touch.x, touch.y))

            # now I know why we add a list [touch.x, touch.y] to touch.ud['line'].points
            # it is because its attribute points is actually also a list that we can add
            # a list to that contains our x and y coordinate values everytime we click
            # down on a certain position of the black screen

            # and also the touch.ud['line'] = Line() was not actually a setter
            # statement but actually just instantiating the LIne object that is why
            # we were able to now access .points using touch.ud['line'] since Line()
            # class contains this points attribute and keywrod argument when instantiated
            # which we can populate using our x and y coordinates that we touched in the
            # black screen

            # Line moreover accepts a points argument that has to be a list of 2D
            # point coordinates, like (x1, y1, x2, y2, ..., xN, yN).
            print(touch.ud['line'].points)

    def on_touch_move(self, touch):
        # as we hold and move from the position of the black screen we  
        # touched we add its x and y coordinates to the already populated 
        # points attribute that the line key the ud dictionary has
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):
    def build(self):
        # we return an instantiation of the Widget object
        # in the end of this method
        parent = Widget()

        # we instantiate our modified Widget object that
        # inherited from the Widget class as well making it
        # a child of the Widget class
        self.painter = MyPaintWidget()

        # we create an element with text clear akin to creating
        # an element in javascript. And as alluded earlier, widgets/elements
        # can be complex and have several "event listeners" attached to them
        clearbtn = Button(text='Clear')

        # we add an "event listener" on_release when we click and
        # specifically release the tap on our phone or mouse
        clearbtn.bind(on_release=self.clear_canvas)

        # create a camera "element"
        cam = Camera(play=True)
        
        # we add our both our painter and clear button 
        # functionalities and return the instantiated widget class
        # parent.add_widget(self.painter)
        # parent.add_widget(clearbtn)
        parent.add_widget(cam)

        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


if __name__ == '__main__':
    # runs our application infinitely to keep window open
    # this is bascially how most apps run, they run infinitely
    # until an event is triggered through a button perhaps that
    # closes them
    MyPaintApp().run()