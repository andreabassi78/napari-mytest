from napari_mytest import function0, function1

    
def test_widgets(make_napari_viewer, capsys):
    # viewer = make_napari_viewer()
    
    
    test_widget0 = function0()
    test_widget1 = function1()


    test_widget1(3)
    # captured = capsys.readouterr()
    
    assert test_widget0.c.value == 6