import time
from functools import partial


class Retry:
    def __init__(self, max_tries=1, delay=0.0, jitter=0.0):
        """ Instantiate new instance or Retry
        :param max_tries: total retries
        :param delay: post-exception delay between attempts
        :param jitter: extra seconds added to delay post-exception between attempts
        """
        self.max_tries = max_tries
        self.tries = 0

        self.delay = delay
        self.jitter = jitter
        self.error = None

    def run(self, fn, *args, **kwargs):
        """ Invoke function until ran or exhausting retries

        :param fn: function to invoke
        :param args: positional arguments of function to invoke.
        :param kwargs: named arguments of function to invoke.
        :return: result of function {fn}
        """
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
                time.sleep(self.delay if not self.jitter else self.delay + (self.tries * self.jitter))

    def copy(self):
        """ instantiate new instance with shadowed arguments

        :return: new copied retry instance
        """
        return Retry(self.max_tries, self.delay, self.jitter)
