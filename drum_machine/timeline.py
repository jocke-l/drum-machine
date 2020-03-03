import itertools
from collections import defaultdict


class Timeline:
    def __init__(self):
        self._timeline = defaultdict(list)

    def __getitem__(self, item):
        if isinstance(item, slice):
            if item.step is not None:
                raise NotImplementedError(
                    f'slice.step for {__name__}.{self.__class__.__name__} '
                    'is not not implemented.'
                )

            start, stop = item.start or 0, item.stop
            iterator = (
                itertools.count()
                if stop is None
                else range(stop - start)
           )
            return (self._timeline[start + delta] for delta in iterator)
        else:
            return self._timeline[item]

    def __iter__(self):
        return self[:]

    def add_sample(self, beat, sample):
        self._timeline[beat] += [sample]
