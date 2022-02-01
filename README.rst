tempto
=====
Convenient retrying

Code
""""""""

.. code:: python

    from tempto import retry

    def raise_error(message):
        raise Exception(message)

    retry = Retry(retries=5, delay=1, jitter=1)
    retry.run(raise_error, "oops! an error occurred")