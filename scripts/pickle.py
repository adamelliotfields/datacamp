#!venv/bin/python
import sys
import pandas as pd


def main() -> None:
    """Converts a .pkl file to a .csv file or vice versa."""
    filename = sys.argv[1]

    if filename.endswith(".pkl"):
        df = pd.read_pickle(filename)
        csv = filename[:-4] + ".csv"
        df.to_csv(csv, index=False)
    elif filename.endswith(".csv"):
        df = pd.read_csv(filename)
        pkl = filename[:-4] + ".pkl"
        df.to_pickle(pkl)
    else:
        print("convert.py: file must be .pkl or .csv")
        sys.exit(1)


# run the main function if the script is run directly
if __name__ == "__main__":
    main()
