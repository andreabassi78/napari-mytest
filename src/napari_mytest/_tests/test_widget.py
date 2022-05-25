from napari_mytest import function0, function1
    
def test_widgets(make_napari_viewer, capsys):
    test_widget0 = function0()
    test_widget1 = function1()

    test_widget0(3)
    test_widget1(4)
     
    out, err = capsys.readouterr()
    assert out == 12
