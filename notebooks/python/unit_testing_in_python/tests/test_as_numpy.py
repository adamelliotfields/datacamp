import pytest
import sys
import numpy as np
from ..as_numpy import get_data_as_numpy_array


class TestGetDataAsNumpyArray(object):
    # example_clean_data.txt
    # 2081	314942
    # 1059	186606
    # 1148	206186
    @pytest.mark.skipif(sys.version_info > (2, 7), reason="Works only on Python 2.7 or lower")
    def test_on_clean_file(self):
        expected = np.array([[2081.0, 314942.0], [1059.0, 186606.0], [1148.0, 206186.0]])
        actual = get_data_as_numpy_array("example_clean_data.txt", num_columns=2)
        message = f"Expected return value: {expected}, Actual return value: {actual}"
        assert actual == pytest.approx(expected), message
