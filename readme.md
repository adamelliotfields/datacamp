# datacamp

[![Launch Codespace](https://img.shields.io/badge/launch-codespace-24292E?logo=github)](https://github.com/codespaces/new/adamelliotfields/datacamp?machine=basicLinux32gb&devcontainer_path=.devcontainer/devcontainer.json)
[![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/adamelliotfields/datacamp/main)

## Usage

See [`Makefile`](./Makefile).

```bash
# this installs dependencies
make

# this runs the server (optional)
make jupyter
```

## Courses

### Python Programming

  * [Introduction to Python](./notebooks/courses/introduction_to_python/notebook.ipynb)
  * [Intermediate Python](./notebooks/courses/intermediate_python/notebook.ipynb)
  * [Dates and Times in Python](./notebooks/courses/dates_and_times_in_python/notebook.ipynb)
  * [Regular Expressions in Python](./notebooks/courses/regular_expressions_in_python/notebook.ipynb)
  * [Unit Testing in Python](./notebooks/courses/unit_testing_in_python/notebook.ipynb)
  * [Object-Oriented Programming in Python](./notebooks/courses/oop_in_python/notebook.ipynb)
  * [Data Structures and Algorithms in Python](./notebooks/courses/dsa_in_python/notebook.ipynb)

### Data Engineering

  * [Intermediate SQL](./notebooks/courses/intermediate_sql/notebook.ipynb)
  * [Joining Data in SQL](./notebooks/courses/joining_data_in_sql/notebook.ipynb)
  * [Database Design](./notebooks/courses/database_design/notebook.ipynb)
  * [Importing Data in Python](./notebooks/courses/importing_data_in_python/notebook.ipynb)
  * [Data Ingestion with `pandas`](./notebooks/courses/data_ingestion_with_pandas/notebook.ipynb)

### Data Science

  * [Data Manipulation with `pandas`](./notebooks/courses/data_manipulation_with_pandas/notebook.ipynb)
  * [Merging Data with `pandas`](./notebooks/courses/merging_data_with_pandas/notebook.ipynb)
  * [Python Data Science Toolbox](./notebooks/courses/python_data_science_toolbox/notebook.ipynb)
  * [Statistics in Python](./notebooks/courses/statistics_in_python/notebook.ipynb)

### Machine Learning

  * [Linear Classifiers in Python](https://app.datacamp.com/learn/courses/linear-classifiers-in-python)

### Miscellaneous

  * [Introduction to Statistics](./notebooks/courses/introduction_to_statistics/notebook.ipynb)
  * [Introduction to NumPy](./notebooks/courses/introduction_to_numpy/notebook.ipynb)

## Projects

  * [Investigating Netflix Movies](./notebooks/projects/investigating_netflix_movies/notebook.ipynb)
  * [World's Oldest Businesses](./notebooks/projects/worlds_oldest_businesses/notebook.ipynb)

## Notes

### Getting Files from DataCamp

The datasets linked in the course descriptions are often times not the same as the ones used in the course. This was extremely frustrating until I found [file.io](https://file.io). You could also do something similar with [localtunnel.me](https://localtunnel.me) or [tunnelto.dev](https://tunnelto.dev).

You just have to use `!` to run a shell command from within whatever exercise's IPython you're in:

```ipython
# the `@` means "the contents of this file"
In [1]: !curl -F 'file=@course_dataset.csv' https://file.io
```

Which should return something like this:

```json
{ "success":true, "link":"https://file.io/ATC77VxxTsAZ" }
```

So then you can just use `wget` to download the file wherever you want:

```bash
wget https://file.io/ATC77VxxTsAZ -O course_dataset.csv
```
