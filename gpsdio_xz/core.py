#!/usr/bin/env python


"""
Core components for gpsdio_xz
"""


import gpsdio.drivers
import six
import lzma


class Xz(gpsdio.drivers.BaseCompressionDriver):
    """
    A compression driver plugin that reads and writes messages
    compressed with xz / lzma.

    LIMITATION: This driver does not support using open file objects
    as input, only file paths.

    This driver does not accept any additional options.
    """

    driver_name = 'Xz'
    extensions = ('xz',)

    def __init__(self, f, mode='r', **kwargs):
        assert isinstance(f, six.string_types)

        driver = lzma.LZMAFile(f, mode)
        gpsdio.drivers.BaseCompressionDriver.__init__(
            self,
            driver
            )
