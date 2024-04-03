<div align="center">
  <!-- Illustration of a tranquil camping scene under a starry night. The main focus is a campfire with flames composed of binary digits and pixelated embers with a tent pitched nearby. The backdrop is a clear sky with floating clouds. -->
  <img src="./datacamp.jpg" width="270" alt="A data campfire" />
  <h1 align="center"><code>datacamp</code></h1>
  <a href="https://github.com/codespaces/new/adamelliotfields/datacamp?machine=basicLinux32gb&devcontainer_path=.devcontainer/devcontainer.json">
    <img src="https://img.shields.io/badge/launch-codespace-24292E?logo=github" alt="Launch Codespace" />
  </a>
</div>
<br />

[DataCamp](https://www.datacamp.com) notebooks.

## Installation

Each notebook can be run directly in [Colab](https://colab.research.google.com). Any required data files will be fetched remotely.

Alternatively, you can run them locally in VS Code or a Codespace:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# optional
pip install -r requirements_*.txt
```

## Contents

* [Python Programming](./notebooks/python/readme.md)
* [Data Engineering](./notebooks/data_engineering/readme.md)
* [Data Science](./notebooks/data_science/readme.md)
* [Machine Learning](./notebooks/machine_learning/readme.md)
* [Deep Learning (TensorFlow)](./notebooks/deep_learning_tensorflow/readme.md)
* [Natural Language Processing](./notebooks/nlp/readme.md)
* [Projects](./notebooks/projects/readme.md)
* [Time Series](./notebooks/time_series/readme.md)
