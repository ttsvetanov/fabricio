import collections

import six


class DefaultProperty(object):

    def __init__(self, func):
        self.__doc__ = getattr(func, '__doc__')
        self.func = func

    def __get__(self, obj, cls=None):
        if obj is None:
            return self
        return self.func(obj)

default_property = DefaultProperty


class Options(collections.OrderedDict):

    @staticmethod
    def make_option(option, value=None):
        option = '--' + option
        if value is not None:
            # TODO escape value
            option += ' ' + value
        return option

    def make_options(self):
        for option, value in self.items():
            if value is None:
                continue
            if isinstance(value, bool):
                if value is True:
                    yield self.make_option(option)
            elif isinstance(value, six.string_types):
                yield self.make_option(option, value)
            else:
                for single_value in value:
                    yield self.make_option(option, single_value)

    def __str__(self):
        return ' '.join(self.make_options())
