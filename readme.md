<div align="center">
  <!-- Illustration of a tranquil camping scene under a starry night. The main focus is a campfire with flames composed of binary digits and pixelated embers with a tent pitched nearby. The backdrop is a clear sky with floating clouds. -->
  <img src="./datacamp.jpg" width="270" alt="A data campfire" />
  <h1 align="center"><code>datacamp</code></h1>
  <a href="https://github.com/codespaces/new/adamelliotfields/datacamp?machine=basicLinux32gb&devcontainer_path=.devcontainer/devcontainer.json">
    <img src="https://img.shields.io/badge/launch-codespace-24292E?logo=github" alt="Launch Codespace" />
  </a>
  <a href="https://mybinder.org/v2/gh/adamelliotfields/datacamp/main">
    <img src="https://mybinder.org/badge_logo.svg" alt="Launch Binder" />
  </a>
</div>
<br />

My notes and projects from [DataCamp](https://www.datacamp.com).

## Usage

See [`Makefile`](./Makefile).

**Local**

```bash
# create virtual env
make venv

# activate
source venv/bin/activate

# install dependencies
make pip

# run the lab server (venv must be activated)
make

# exit virtual env
deactivate
```

**Codespace**

```bash
# install dependencies (no need for venv in container)
make pip

# run the server
make
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
  * [Statistics in Python](./notebooks/courses/statistics_in_python/notebook.ipynb)
  * [Introduction to `matplotlib`](./notebooks/courses/introduction_to_matplotlib/notebook.ipynb)
  * [Introduction to `seaborn`](./notebooks/courses/introduction_to_seaborn/notebook.ipynb)
  * [Intermediate `seaborn`](./notebooks/courses/intermediate_seaborn/notebook.ipynb)
  * [Python Data Science Toolbox](./notebooks/courses/python_data_science_toolbox/notebook.ipynb)

### Machine Learning

  * [Linear Classifiers in Python](https://app.datacamp.com/learn/courses/linear-classifiers-in-python)

### Miscellaneous

  * [Introduction to Statistics](./notebooks/courses/introduction_to_statistics/notebook.ipynb)
  * [Introduction to NumPy](./notebooks/courses/introduction_to_numpy/notebook.ipynb)

## Projects

  * [Investigating Netflix Movies](./notebooks/projects/investigating_netflix_movies/notebook.ipynb)
  * [World's Oldest Businesses (SQL)](./notebooks/projects/worlds_oldest_businesses_sql/notebook.ipynb)
  * [World's Oldest Businesses (Python)](./notebooks/projects/worlds_oldest_businesses_python/notebook.ipynb)

## Notes

### Getting Files from DataCamp

The datasets linked in the course descriptions are often times not the same as the ones used in the course. This was extremely frustrating until I found [file.io](https://file.io). You could also do something similar with [localtunnel.me](https://localtunnel.me) or [tunnelto.dev](https://tunnelto.dev).

You just have to use `!` to run a shell command from within whatever exercise's IPython you're in:

```py
# the `@` means "the contents of this file"
!curl -F 'file=@course_dataset.csv' https://file.io
```

Which should return something like this:

```json
{ "success":true, "link":"https://file.io/ATC77VxxTsAZ" }
```

So then you can just use `wget` to download the file wherever you want:

```bash
wget https://file.io/ATC77VxxTsAZ -O course_dataset.csv
```

### Converting Markdown to Notebooks

I find it easier to take notes in Markdown and then convert to a notebook for cell execution. I use [jupytext](https://github.com/mwouts/jupytext) to do this.

```bash
pipx install jupytext
jupytext --opt=split_at_heading=true --from=md:markdown --to=ipynb notebook.md
```
