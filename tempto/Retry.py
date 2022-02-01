import time
from functools import partial


class Retry:
    def __init__(self, max_tries=1, delay=0.0, jitter=0.0):
        self.max_tries = max_tries
        self.tries = 0

        self.delay = delay
        self.jitter = jitter
        self.error = None

    def run(self, fn, *args, **kwargs):
        args = args or list()
        kwargs = kwargs or dict()

        _delay = self.delay

        for _try in range(self.max_tries):
            try:
                self.tries += 1
                return partial(fn, *args, **kwargs)()
            except Exception as e:
                self.error = e
                if _try == self.max_tries - 1:
                    raise e
                time.sleep(self.delay if self.jitter else self.delay + (self.tries * self.jitter))
