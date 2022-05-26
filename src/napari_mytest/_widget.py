"""
Test code for napari plugin
"""

from magicgui import magic_factory
import napari

@magic_factory
def function0(a: int = 5):
    widget1.b.value = a
    
@magic_factory
def function1(b: int = 3):
    print('b = ', b)  

widget0 = function0()
widget1 = function1()

viewer = napari.Viewer()
viewer.window.add_dock_widget(widget0, name = 'mywidget 0',
                                  area='right')
viewer.window.add_dock_widget(widget1, name = 'mywidget 1',
                                  area='right') 
napari.run()


