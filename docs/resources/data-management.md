# Data management

A challenging aspect of tutorial development is how to manage datasets. Ideally, the data you use will be publicly accessible and permanent for reproducibility of your computational examples.

```{important}
Remember, a hackweek tutorial is *learning-oriented* and should guide participants through a step-wise process with a meaningful outcome.
```

## Make your tutorial data publicly accessible
*We recommend using small (<100 MB) example datasets for your tutorial*. If you typically work with large datasets, consider working with a small subset to get your ideas across.

```{note}
If using a subset be sure to capture data provenance, for example by including a script that you used to access the original full-sized dataset from the data provider.
```

You can create a repository on GitHub to publicly host the tutorial dataset, and even create a DOI for it if you want! Here is an [example for images](https://github.com/snowex-hackweek/tutorial-data), and here is an [example for n-dimensional arrays](https://github.com/scottyhq/zarrdata).


## Stream data from a public server
Increasingly there are ways to access data remotely in a streaming fashion so that you don't have to download files at all! At a basic level, software can read URLs to data files instead of local file paths. This is a great option to facilitate portability of your tutorial to run on different machines (hackweek JupyterHub, your personal computer, the computers of collaborators, etc.).

```{warning}
If your tutorial streams data directly from a data provider, check that scheduled server downtime for maintenance isn't planned during your presentation!
```

## Computational resource considerations
In order for tutorial notebooks to be executable on different machines, we recommend targeting limited computational requirements such as 2-core CPU, 8 GB of RAM memory, 10 GB of disk space (at the time of writing)
