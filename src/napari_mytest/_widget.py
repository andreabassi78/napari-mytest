"""
Test code for napari plugin
"""

from magicgui import magic_factory

@magic_factory
def function0(a: int = 5):
    my_shared_vars.c = a
    print('c=', my_shared_vars.c)


@magic_factory
def function1(b: int = 3):
    result = my_shared_vars.c * b
    print('c*b=', result)
    

from dataclasses import dataclass
@dataclass
class Shared_variables:
    c: int 

my_shared_vars = Shared_variables(2)  # create instance with just some initial value for c
    
    

# this will not be executed by the plugin: widget0.a will not exists there
if __name__ == '__main__':
    import napari
    viewer = napari.Viewer()

    widget0 = function0()
    widget1 = function1()
    
    viewer.window.add_dock_widget(widget0, name = 'mywidget 0',
                                  area='right')
    viewer.window.add_dock_widget(widget1, name = 'mywidget 1',
                                  area='right')
    
    napari.run()


