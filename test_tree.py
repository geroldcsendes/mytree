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
        result = tree_maker(
            input_path=str(path_test), write_md=True)

        # print test result
        res_path = "testdir/test_base_res.md"
        res_path = pathlib.Path(res_path).resolve()

        # uncomment when experimenting
        # with open(res_path, "w+", encoding='utf-8') as writer:
        #     writer.write(result)

        # expected tree
        path_expected = "testdir/test_base_exp.md"
        path_expected = pathlib.Path(path_expected).resolve()

        with open(path_expected, "r", encoding="utf-8") as reader:
            expected = reader.read()

        self.assertEqual(result, expected)

    def test_csv_exclusion(self):

        # define test directory
        path_test = "testdir/test1"
        path_test = pathlib.Path(path_test).resolve()

        # create result tree
        result = tree_maker(
            input_path=str(path_test), write_md=True, exclude_ext=".csv")

        # save
        res_path = "testdir/test_excl-csv_res.md"
        res_path = pathlib.Path(res_path).resolve()

        # uncomment when experimenting
        # with open(res_path, "w+", encoding='utf-8') as writer:
        #     writer.write(result)
        
        # expected tree
        path_expected = "testdir/test_excl-csv_exp.md"
        path_expected = pathlib.Path(path_expected).resolve()

        with open(path_expected, "r", encoding="utf-8") as reader:
            expected = reader.read()

        self.assertEqual(result, expected)

    def test_init_exclusion(self):
        return True


if __name__ == '__main__':
    unittest.main()
