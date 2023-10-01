import numpy as np


def get_data_as_numpy_array(clean_data_file_path, num_columns):
    result = np.empty((0, num_columns))

    with open(clean_data_file_path, "r") as f:
        rows = f.readlines()

        for row_num in range(len(rows)):
            try:
                row = np.array([rows[row_num].rstrip("\n").split("\t")], dtype=float)
            except ValueError:
                raise ValueError(
                    f"Line {row_num + 1} of {clean_data_file_path} is badly formatted"
                )
            else:
                if row.shape != (1, num_columns):
                    raise ValueError(
                        f"Line {row_num + 1} of {clean_data_file_path} does not have {num_columns} columns"
                    )
            result = np.append(result, row, axis=0)
    return result
