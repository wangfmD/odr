# -*- coding: utf-8 -*-


class FrozenJSON:

    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    # @classmethod
    # def build(cls, obj):
    #     if isinstance(obj, abc.Mapping):
    #         return cls(obj)
    #     elif isinstance(obj, abc.MutableSequence):
    #         return [cls.build(item) for item in obj]
    #     else:
    #         return obj


class FoDict(dict):
    def __init__(self,*args, ** kwargs):
        dict.__init__(self, *args,** kwargs)
        self.__dict__ = self


def allowDotting(self,state = True):
    if state:
            self.__dict__ = self
    else:
        self.__dict__ = dict()


def aww():
    w = FoDict({"name": "wfm", "age": 20})
    print(w.name,w.age)


if __name__ == '__main__':
    aww()
