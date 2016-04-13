import unittest

from pip_dependencies2json import parse


class TestPipDependencies2json(unittest.TestCase):

    def test_empty(self):
        content = [
            "irrelevant line"
        ]

        self.assertEqual(parse(content), [])

    def test_some_lines(self):
        content = [
            "irrelevant line",
            "lib1==1.2.3",
            "lib2==3.2.1.dev1",
            "irrelevant line"
        ]

        result = parse(content)

        self.assertEqual(result, [
            {
                "type": "pip",
                "name": "lib1",
                "version": "1.2.3",
            },
            {
                "type": "pip",
                "name": "lib2",
                "version": "3.2.1.dev1",
            }
        ])
