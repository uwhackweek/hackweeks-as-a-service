# Data management

A challenging aspect of tutorial development is how to manage dataset dependencies. Ideally, the data you use will be *publicly accessible* and *permanent* for reproducibility.

```{important}
Remember, a hackweek tutorial is *learning-oriented* and should guide participants through a step-wise process with a meaningful outcome.
```

If you typically work with large datasets, consider designing your tutorial to work with a small subset (~10 MB) to achieve your learning objectives. Below are some general guidelines based on past hackweeks:


## Make your tutorial data publicly accessible!

### My data is small (<10MB)
If your tutorial just needs a small image, or tabular data like a `.csv` file, go ahead and add it to the repository along with your tutorial code.

### My data is moderate (10 - 100 MB)
You can create a separatel repository on GitHub to publicly host your tutorial dataset. [Per GitHub repository limits](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github), *individual files are required to be < 100 MB*.
Here is an [example for images](https://github.com/snowex-hackweek/tutorial-data), and here is an [example for n-dimensional arrays](https://github.com/scottyhq/zarrdata).

```{note}
If using a subset be sure to capture data provenance, for example by including a script that you used to access the original full-sized dataset from the data provider.
```

### My data is cumbersome (>100 MB)
Increasingly there are ways to load remote data in a streaming fashion, which allows you to avoid download and storage! At a basic level, software can read URLs instead of local file paths, such as at the beginning of [this tutorial](https://snowex-hackweek.github.io/website/tutorials/sar/sentinel1.html#dive-right-in).

```{warning}
If your tutorial streams data directly from a data provider, check that scheduled server downtime for maintenance isn't planned during your presentation! Also, be aware that URLs can be changed at any time by the data provider.
```

## Data permanence
If you want long-term hosting of a tutorial dataset that receives a citable Digital Object Identifier (DOI), you can use [Zenodo.org](https://about.zenodo.org).

1. [Link your GitHub repository with data Zenodo](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content) *subject to GitHub repository size limits

2. [Use Zenodo directly](https://library.cfa.harvard.edu/data-archiving-and-sharing) *50 GB standard limit

[Here](https://snowex-hackweek.github.io/website/tutorials/thermal-ir/thermal-ir-tutorial.html#) is an example tutorial that retrieves a dataset from a [Zenodo 'record'](https://zenodo.org/record/5504396)


## Computational resource considerations
In order for tutorial notebooks to be executable on different machines, *we recommend targeting limited computational requirements such as 2-core CPU, 8 GB of RAM memory, 10 GB of disk space (at the time of writing)*
