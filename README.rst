tempto
=====
Convenient asynchronous ands synchronous retrying

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

    retry = AsyncRetry(retries=5, delay=1, jitter=1)
    await retry.run(raise_error, "oops! an error occurred")
