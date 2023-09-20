#!/usr/bin/env poetry run python

import csv
import os
import sys
import tempfile


def main() -> None:
    """Adds a column of auto-incrementing IDs to a CSV file."""

    tmp_file = tempfile.NamedTemporaryFile(mode="w", delete=False)
    input_file = sys.argv[1]
    skip_header = False

    if input_file == "--header":
        skip_header = True
        input_file = sys.argv[2]

    if not input_file.endswith(".csv"):
        print("auto_id.py: not a CSV")
        sys.exit(1)

    with open(input_file, "r") as input, tmp_file as tmp:
        reader = csv.reader(input)
        writer = csv.writer(tmp)

        if skip_header:
            header = ["id"] + next(reader)
            writer.writerow(header)

        for i, row in enumerate(reader, start=1):
            row.insert(0, i)
            writer.writerow(row)

    os.rename(tmp_file.name, input_file)


if __name__ == "__main__":
    main()
