# Data management

A challenging aspect of tutorial development is how to manage dataset dependencies. Ideally, the data you use will be *publicly accessible* and *permanent* for reproducibility. In this section we present practical guidelines for effective data sharing for Hackweek Tutorials and Projects.

```{important}
Remember, a hackweek tutorial is *learning-oriented* and should guide participants through a step-wise process with a meaningful outcome. If you typically work with large datasets, consider designing your tutorial to work with a small subset (~10 MB) that still enables your learning objectives to be met.
```

## Computational resource considerations
In order for tutorial notebooks to be executable on widely available public computing infrastructure *we recommend targeting limited computational requirements such as 2-core CPU, 8 GB of RAM memory, 10 GB of disk space (at the time of writing)*

## Guidelines for Tutorials

### <10MB
If your tutorial just needs a small image, or tabular data like a `.csv` file, go ahead and add it to the repository along with your tutorial code.

### 10 - 100 MB
You can create a separate repository on GitHub to publicly host your tutorial dataset. [Per GitHub repository limits](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github), *individual files are required to be < 100 MB*.
* Here is an [example for images](https://github.com/snowex-hackweek/tutorial-data)
* Here is an [example for n-dimensional arrays](https://github.com/scottyhq/zarrdata).

```{note}
If using a subset be sure to capture data provenance, for example by including a script that you used to access the original full-sized dataset from the data provider.
```

#### GitHub Release artifacts

Generally it is not advisable to store binary files in GitHub repositories. Event if you make small changes to a file, an entire new copy is saved in the revision history and the size of the repository will quickly get unwieldy.

[GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) are a feature of GitHub repositories that archive a snapshot of files in your repository *in addition to other auxiliary files*. According to official GitHub documentation:

> You can create a release to package software, along with release notes and links to binary files, for other people to use.

At the time of writing, *each file included in a release must be under 2 GiB*. So storing tutorial data as files attached to a GitHub release of tutorial code can work well to keep code and associated data together.

* Here is an [example of attaching a large 100 MB Geotiff to a release artifact](https://github.com/scottyhq/share-a-raster/releases/tag/v0.0.1)

```{note}
The GitHub Command Line Interface (CLI) provides a convenient method for downloading release data https://cli.github.com/manual/gh_release_download
```

### >100 MB

#### Stream from URLs
Increasingly there are ways to load remote data in a streaming fashion, which allows you to avoid download and storage altogether! Essential this means using software that can read URLs instead of local file paths, such as at the beginning of [this tutorial](https://snowex-hackweek.github.io/website/tutorials/sar/sentinel1.html#dive-right-in).

```{note}
Software that can read URLs still ultimately must download data! It will either be stored only in RAM, or as a temporary file on your hard drive, so be aware that you are still constrained by your local computing resources.
```

```{warning}
Check that scheduled server downtime for maintenance isn't planned during your presentation! Also, be aware that URLs can be changed at any time by the data provider.
```
* Here is an [example using the Python earthaccess library](https://earthaccess.readthedocs.io/en/latest/tutorials/file-access/)

* Libraries like Xarray can [read data directly from cloud storage](https://docs.xarray.dev/en/stable/user-guide/io.html#cloud-storage-buckets)

#### Use Zenodo.org
Another approach is to upload your data on Zenodo, which at the time of writing has a standard 50 GB limit (https://library.cfa.harvard.edu/data-archiving-and-sharing).

```{note}
https://github.com/fatiando/pooch is a nice Python utility to fetch data from Zenodo
```

## Data permanence considerations
Be aware that GitHub repositories can be deleted at any time by repository owners. For guaranteed long-term (10+years) hosting of a tutorial dataset that receives a citable Digital Object Identifier (DOI) you can use [Zenodo.org](https://about.zenodo.org). You can easily [link a GitHub repository with Zenodo](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content)

* [Here](https://snowex-hackweek.github.io/website/tutorials/thermal-ir/thermal-ir-tutorial.html#) is an example tutorial that retrieves a dataset from a [Zenodo 'record'](https://zenodo.org/record/5504396)

## Guidelines for Projects

### JupterHub Data Sharing

During a hackweek, teams often want to share data with each other for collaborative analysis. In contrast to tutorial datasets which are usually hand-picked, project data is dynamic and changing over time. By using a JupyterHub during a hackweek, participants can take advantage of networked storage drives and pre-configured Cloud Object Storage.

```{note}
JupyterHubs do not always have the same configuration, but we encourage you to review this guide from 2i2c which explains options for JupyterHub storage (https://docs.2i2c.org/user/topics/data/)
```
