tempto
=====
Convenient retrying for python that supports asynchronous and synchronous systems

Code
""""""""

.. code:: python

    from tempto import retry

    def raise_error(message):
        raise Exception(message)

    retry = Retry(retries=5, delay=1, jitter=1)
    retry.run(raise_error, "oops! an error occurred")

Async
""""""""

.. code:: python

    from tempto import retry

    async def raise_error(message):
        raise Exception(message)

    retry = await AsyncRetry(retries=5, delay=1, jitter=1)
    await retry.run(raise_error, "oops! an error occurred")