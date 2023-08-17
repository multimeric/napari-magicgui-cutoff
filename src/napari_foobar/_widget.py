from magicgui import magic_factory

@magic_factory(x={'widget_type': 'RangeSlider', 'max': 50})
def example_magic_widget(x: tuple[int, int]):
    print(f"you have selected {x}")
