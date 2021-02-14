import unittest
import pathlib

from main import tree_maker


class TestTree(unittest.TestCase):
    def test_base(self):
        """
        Test tree structure without providing arguments other than required.
        """

        # define test directory
        path_test = "testdir/test1"
        path_test = pathlib.Path(path_test).resolve()

        # create result tree
        result = tree_maker(input_path=str(path_test), write_md=True)

        # expected tree
        path_expected = "testdir/test1_exp.md"
        path_expected = pathlib.Path(path_expected).resolve()

        with open(path_expected, "r", encoding="utf-8") as reader:
            expected = reader.read()

        # print test result
        test_res_path = "testdir/test1_res.md"
        test_res_path = pathlib.Path(test_res_path).resolve()

        # with open(test_res_path, "w+", encoding='utf-8') as writer:
        #     writer.write(result)

        self.assertEqual(result, expected)

    def test_csv_exclusion(self):
        return True

    def test_init_exclusion(self):
        return True


if __name__ == '__main__':
    unittest.main()
