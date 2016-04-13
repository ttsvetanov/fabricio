from collections import OrderedDict

import six

import utils


class Options(OrderedDict):

    @staticmethod
    def make_option(option, value=None):
        option = '--' + option
        if value is not None:
            value = utils.shell_escape(value)
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
