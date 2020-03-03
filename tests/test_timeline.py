import unittest

from drum_machine.timeline import Timeline


class TimelineTestCase(unittest.TestCase):
    def setUp(self):
        self.timeline = Timeline()
        for beat in range(5, 10):
            self.timeline.add_sample(beat, 'a')

    def test_slicing(self):
        timeline_slice = list(self.timeline[5:10])
        expected_result = [['a']] * 5
        self.assertListEqual(timeline_slice, expected_result)

        timeline_slice = list(self.timeline[:10])
        expected_result = [[]] * 5 + [['a']] * 5
        self.assertListEqual(timeline_slice, expected_result)

        timeline_slice = self.timeline[8:]
        self.assertListEqual(next(timeline_slice), ['a'])
        self.assertListEqual(next(timeline_slice), ['a'])
        self.assertListEqual(next(timeline_slice), [])
        self.assertListEqual(next(timeline_slice), [])

        with self.assertRaises(NotImplementedError):
            _ = self.timeline[1:1:1]

    def test_stacked_samples(self):
        self.timeline.add_sample(5, 'b')
        self.assertListEqual(self.timeline[5], ['a', 'b'])

    def test_iterator(self):
        timeline_slice = []
        for beat, samples in enumerate(self.timeline):
            if beat >= 12:
                break

            timeline_slice.append(samples)

        expected_result = [[]] * 5 + [['a']] * 5 + [[]] * 2
        self.assertListEqual(timeline_slice, expected_result)
