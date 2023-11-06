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

## Installation

```bash
python -m venv venv
venv/bin/pip install -r requirements.txt
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
  * [Data Importing in Python](./notebooks/courses/data_importing_in_python/notebook.ipynb)
  * [Data Ingestion with `pandas`](./notebooks/courses/data_ingestion_with_pandas/notebook.ipynb)
  * [Data Manipulation with `pandas`](./notebooks/courses/data_manipulation_with_pandas/notebook.ipynb)
  * [Data Merging with `pandas`](./notebooks/courses/data_merging_with_pandas/notebook.ipynb)

### Data Science
  * [Introduction to Statistics](./notebooks/courses/introduction_to_statistics/notebook.ipynb)
  * [Statistics in Python](./notebooks/courses/statistics_in_python/notebook.ipynb)
  * [Introduction to `numpy`](./notebooks/courses/introduction_to_numpy/notebook.ipynb)
  * [Introduction to `matplotlib`](./notebooks/courses/introduction_to_matplotlib/notebook.ipynb)
  * [Introduction to `seaborn`](./notebooks/courses/introduction_to_seaborn/notebook.ipynb)
  * [Intermediate `seaborn`](./notebooks/courses/intermediate_seaborn/notebook.ipynb)
  * [Python Data Science Toolbox](./notebooks/courses/python_data_science_toolbox/notebook.ipynb)
  * [Categorical Data in Python](./notebooks/courses/categorical_data_in_python/notebook.ipynb)
  * [Data Preprocessing in Python](./notebooks/courses/data_preprocessing_in_python/notebook.ipynb)
  * [Introduction to `statsmodels`](./notebooks/courses/introduction_to_statsmodels/notebook.ipynb)
  * [Sampling in Python](./notebooks/courses/sampling_in_python/notebook.ipynb)
  * [Hypothesis Testing in Python](./notebooks/courses/hypothesis_testing_in_python/notebook.ipynb)

### Machine Learning
  * [Supervised Learning with `scikit-learn`](./notebooks/courses/supervised_learning_with_sklearn/notebook.ipynb)
  * [Unsupervised Learning with `scikit-learn`](./notebooks/courses/unsupervised_learning_with_sklearn/notebook.ipynb)

## Projects

  * [Investigating Netflix Movies](./notebooks/projects/investigating_netflix_movies/notebook.ipynb)
  * [World's Oldest Businesses (SQL)](./notebooks/projects/worlds_oldest_businesses_sql/notebook.ipynb)
  * [World's Oldest Businesses (Python)](./notebooks/projects/worlds_oldest_businesses_python/notebook.ipynb)
  * [The Android App Market on Google Play](./notebooks/projects/android_app_market/notebook.ipynb)
  * [A Visual History of Nobel Prize Winners](./notebooks/projects/nobel_prize_history/notebook.ipynb)
  * [Dr. Semmelweis and the Discovery of Handwashing](./notebooks/projects/discovery_of_handwashing/notebook.ipynb)

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
