from napari_mytest import function0, function1
import numpy as np
    
def test_widgets(make_napari_viewer, capsys):
    viewer = make_napari_viewer()
    data = np.random.random ([3,100,100])
    im_layer = viewer.add_image(data)
    test_widget0 = function0()
    test_widget1 = function1()

    test_widget0(3)
    test_widget1(im_layer)
    
    
    
    # captured = capsys.readouterr()
    
    assert im_layer.scale[0] == 3 