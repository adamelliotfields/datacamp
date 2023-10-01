from ..preprocessing_helpers import convert_to_int, row_to_list


class TestConvertToInt(object):
    def test_on_string_with_one_comma(self):
        test_argument = "2,081"
        expected = 2081
        actual = convert_to_int(test_argument)
        message = f"convert_to_int('2,081') should return the int 2081, but it actually returned {actual}"
        assert actual == expected, message

    def test_with_no_comma(self):
        actual = convert_to_int("756")
        assert actual == 756, f"Expected: 756, Actual: {actual}"

    def test_with_one_comma(self):
        actual = convert_to_int("2,081")
        assert actual == 2081, f"Expected: 2081, Actual: {actual}"

    def test_with_two_commas(self):
        actual = convert_to_int("1,034,891")
        assert actual == 1034891, f"Expected: 1034891, Actual: {actual}"

    def test_on_string_with_missing_comma(self):
        actual = convert_to_int("178100,301")
        assert actual is None, f"Expected: None, Actual: {0}"

    def test_on_string_with_incorrectly_placed_comma(self):
        actual = convert_to_int("12,72,891")
        assert actual is None, f"Expected: None, Actual: {0}"

    def test_on_float_valued_string(self):
        actual = convert_to_int("23,816.92")
        assert actual is None, f"Expected: None, Actual: {0}"


class TestRowToList(object):
    def test_on_no_tab_no_missing_value(self):
        actual = row_to_list("123\n")  # (0, 0) boundary value
        assert actual is None, f"Expected: None, Actual: {actual}"

    def test_on_two_tabs_no_missing_value(self):
        actual = row_to_list("123\t4,567\t89\n")  # (2, 0) boundary value
        assert actual is None, f"Expected: None, Actual: {actual}"

    def test_on_one_tab_with_missing_value(self):
        actual = row_to_list("\t4,567\n")  # (1, 1) boundary value
        assert actual is None, f"Expected: None, Actual: {actual}"

    def test_on_no_tab_with_missing_value(self):
        actual = row_to_list("\n")  # (0, 1) case
        assert actual is None, f"Expected: None, Actual: {actual}"

    def test_on_two_tabs_with_missing_value(self):
        actual = row_to_list("123\t\t89\n")  # (2, 1) case
        assert actual is None, f"Expected: None, Actual: {actual}"

    def test_on_normal_argument_1(self):
        actual = row_to_list("123\t4,567\n")
        expected = ["123", "4,567"]
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"

    def test_on_normal_argument_2(self):
        actual = row_to_list("1,059\t186,606\n")
        expected = ["1,059", "186,606"]
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"
