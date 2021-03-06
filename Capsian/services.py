from   Capsian.input.keyboard                 import KeyboardInputHandler
from   Capsian.entities.independent_component import IndependentComponent
from   pyglet.window                          import key                  as Key
import Capsian.engine                                                     as engine
import pyglet


@IndependentComponent
class CapsianKeyboardHandler(KeyboardInputHandler):
    def on_key_pressed(self, symbol, modifiers):
        if not engine.main_window.alive > 0:
            if symbol == Key.ESCAPE or symbol == Key.ENTER:
                engine.main_window.close()

            return

        if symbol == engine.main_window.fullscreen_key:
            import os

            if os.name == "nt":
                screen = pyglet.canvas.Screen(
                    display=engine.main_window.display,
                    width=engine.main_window.screen.width,
                    height=engine.main_window.screen.height,
                    handle=None,
                    x=0,
                    y=0
                )

                engine.main_window.set_fullscreen(
                    not engine.main_window.fullscreen,
                    screen=screen
                )

            elif os.name is not "nt":
                engine.main_window.set_fullscreen(
                    not engine.main_window.fullscreen
                )
            
            lock = engine.main_window.mouse_lock
            engine.main_window.set_mouse_lock(False)
            engine.main_window.set_mouse_lock(lock)
