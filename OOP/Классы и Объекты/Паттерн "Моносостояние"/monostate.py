class ThreadData:
    __shared_attrs = {
        'name' : 'Tabigat',
        'data' : {},
        'id' : 1,
    }


    def __init__(self):
        self.__dict__ = self.__shared_attrs

    # Go Python Console
    # th1 = ThreadData()
    # th2 = ThreadData()
    # th2.id = 3
    # th1.attr_new = 'new_attr'



