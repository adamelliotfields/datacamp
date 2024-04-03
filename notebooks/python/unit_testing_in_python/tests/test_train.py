import pytest
import numpy as np
from ..train import split_into_training_and_testing_sets


class TestSplitIntoTrainingAndTestingSets(object):
    def test_on_one_row(self):
        test_argument = np.array([[1382.0, 390167.0]])

        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_argument)

        exc_info.match("Argument data_array must have at least 2 rows, it actually has just 1")

    def test_on_six_rows(self):
        example_argument = np.array(
            [
                [2081.0, 314942.0],
                [1059.0, 186606.0],
                [1148.0, 206186.0],
                [1506.0, 248419.0],
                [1210.0, 214114.0],
                [1697.0, 277794.0],
            ]
        )

        expected_training_array_num_rows = 4
        expected_testing_array_num_rows = 2
        actual = split_into_training_and_testing_sets(example_argument)

        assert (
            actual[0].shape[0] == expected_training_array_num_rows
        ), f"The actual number of rows in the training array is not {expected_training_array_num_rows}"

        assert (
            actual[1].shape[0] == 2
        ), f"The actual number of rows in the testing array is not {expected_testing_array_num_rows}"


@pytest.mark.xfail(reason="Using TDD, model_test() has not yet been implemented")
class TestModelTest(object):
    def test_on_linear_data(self):
        test_input = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected = 1.0
        actual = model_test(test_input, 2.0, 1.0)  # type: ignore
        message = (
            f"model_test({test_input}) should return {expected}, but it actually returned {actual}"
        )
        assert actual == pytest.approx(expected), message

    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            model_test(test_input, 1.0, 1.0)  # type: ignore
