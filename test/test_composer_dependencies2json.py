import unittest

from composer_dependencies2json import parse


class TestComposerDependencies2json(unittest.TestCase):

    def test_empty(self):
        content = [
            "irrelevant line"
        ]

        self.assertEqual(parse(content), [])

    def test_some_lines(self):
        content = [
            "domain1/lib1           1.2.3   A Description",
            "domain2/lib2           v3.1.29 A Description"
        ]

        result = parse(content)

        self.assertEqual(result, [
            {
                "type": "composer",
                "name": "domain1/lib1",
                "version": "1.2.3",
            },
            {
                "type": "composer",
                "name": "domain2/lib2",
                "version": "v3.1.29",
            }
        ])

    def test_ignore_irrelevant_lines(self):
        content = [
            "this is so irrelevant",
            "domain1/lib1           1.2.3   A Description",
            "so is this"
        ]

        result = parse(content)

        self.assertEqual(result, [
            {
                "type": "composer",
                "name": "domain1/lib1",
                "version": "1.2.3",
            }
        ])
