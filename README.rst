=============================
Pytest VirtualTime Event Loop
=============================

Features
--------

* Use virtual time inside the asyncio loop and stop waiting in real time
* Code to be tested has not to be changed

Installation
------------

You can install "pytest-virtualtime" via `pip`_ from `PyPI`_::

    $ pip install pytest-virtualtime

Example
-------

How long will the following test take?

```python
@pytest.mark.asyncio
async def test_waiting(event_loop):
    l = list()

    asyncio.call_later(5, l.append, 5)

    await asyncio.sleep(4)
    assert len(l) == 0

    await asyncio.sleep(2)
    assert l == [5]
```

Yes, you will wait 6 seconds. And yes, after running this test you will be 6
seconds older.

**But has time to be wall-clock time in tests?**

In most cases - **No!**

So instead do this:

```python
@pytest.mark.asyncio
async def test_waiting(virtual_time_loop):
    ...
```

When replacing `event_loop` with `virtual_time_loop` the default asyncio loop
get exchanged by a loop where time is just virtually passing by. No wall-clock
time is passing - and you will not be 6 seconds older.

**Use virtual time event loop and stay young!**

Credits
-------

This plugin is using the VirtualTimeEventLoop from `aioreactive`_ . Without
that work this plugin would not be possible!


.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
.. _`aioreactive`: https://github.com/dbrattli/aioreactive