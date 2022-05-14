"""
Test code for napari plugin
"""

from magicgui import magic_factory
from napari.layers import Image


@magic_factory
def function0(a: int = 5):
    my_shared_vars.c = a
    print(my_shared_vars.c)


@magic_factory
def function1(image: Image):
    image.scale = [my_shared_vars.c,1,1]
    

class shared_variables:
    def init(self, c = 0):
        self.c = c

my_shared_vars = shared_variables  
    
    

# this will not be executed by the plugin: widget0.a will not exists there
if __name__ == '__main__':
    import napari
    viewer = napari.Viewer()

    widget_0 = function0()
    widget1 = function1()
    
    viewer.window.add_dock_widget(widget_0, name = 'mywidget 0',
                                  area='right', add_vertical_stretch=True)
    viewer.window.add_dock_widget(widget1, name = 'mywidget 1',
                                  area='right', add_vertical_stretch=True)
    
    napari.run()







# class ExampleQWidget(QWidget):
#     # your QWidget.__init__ can optionally request the napari viewer instance
#     # in one of two ways:
#     # 1. use a parameter called `napari_viewer`, as done here
#     # 2. use a type annotation of 'napari.viewer.Viewer' for any parameter
#     def __init__(self, napari_viewer):
#         super().__init__()
#         self.viewer = napari_viewer

#         btn = QPushButton("Click me!")
#         btn.clicked.connect(self._on_click)

#         self.setLayout(QHBoxLayout())
#         self.layout().addWidget(btn)

#     def _on_click(self):
#         print("napari has", len(self.viewer.layers), "layers")


# @magic_factory
# def example_magic_widget(img_layer: "napari.layers.Image"):
#     print(f"you have selected {img_layer}")


# # Uses the `autogenerate: true` flag in the plugin manifest
# # to indicate it should be wrapped as a magicgui to autogenerate
# # a widget.
# def example_function_widget(img_layer: "napari.layers.Image"):
#     print(f"you have selected {img_layer}")
