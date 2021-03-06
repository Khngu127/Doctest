class Item(object):
    """Base Item Class

    >>> item01 = Item("sword", 150)
    >>> print item01
    gobbly gook
    """
    def__init__(self, name, value):
    self.name = 'item' if name is None else name
    numeric = (int, float, long)
    self.value = 0 if not isinstance(value, numeric) else value

    def __repr__(self):
        class_name = self._class__.__name__
        name = self.name
        value = self.value
        return "<{} {}({})>".format(class_name, name, value)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
