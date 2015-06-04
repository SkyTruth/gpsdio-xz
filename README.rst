=====================
gpsdio xz plugin
=====================


.. image:: https://travis-ci.org/SkyTruth/gpsdio-xz.svg?branch=master
    :target: https://travis-ci.org/SkyTruth/gpsdio-xz


.. image:: https://coveralls.io/repos/SkyTruth/gpsdio-xz/badge.svg?branch=master
    :target: https://coveralls.io/r/SkyTruth/gpsdio-xz


A compression driver plugin for `gpsdio <https://github.com/skytruth/gpdsio/>`_ that reads and writes messages compressed with xz / lzma.


Installing
----------

Via pip:

.. code-block:: console

    $ pip install gpsdio-xz

From master:

.. code-block:: console

    $ git clone https://github.com/SkyTruth/gpsdio-xz
    $ cd gpsdio-xz
    $ pip install .


Developing
----------

.. code-block::

    $ git clone https://github.com/SkyTruth/gpsdio-xz
    $ cd gpsdio-xz
    $ virtualenv venv && source venv/bin/activate
    $ pip install -e .[test]
    $ py.test tests --cov gpsdio_xz --cov-report term-missing
