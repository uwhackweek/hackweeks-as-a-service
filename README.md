# hackweeks-as-a-service
[![Deploy](https://github.com/uwhackweek/hackweeks-as-a-service/actions/workflows/deploy.yaml/badge.svg)](https://github.com/uwhackweek/hackweeks-as-a-service/actions/workflows/deploy.yaml)
[![DOI](https://zenodo.org/badge/354072491.svg)](https://zenodo.org/badge/latestdoi/354072491)

This repository hosts a website with information describing the [UW eScience Institute's](https://escience.washington.edu) hackweeks as a service model. It uses [Jupyter-book](https://jupyterbook.org/) and the website is hosted on the gh-pages branch.

## GitHub Deployment
This repository is configured with [GitHub Actions](./.github/workflows/deploy.yaml) to automatically build and publish HTML to the gh-pages branch. Just commit to the main branch and the website will be automatically updated.

## Local Deployment
```
git clone https://github.com/uwhackweek/hackweeks-as-a-service.git
cd hackweeks-as-a-service
conda env create
conda activate hackweek-guidebook
jb build docs
```

## Contact

* [Anthony Arendt](mailto:arendta@uw.edu)
* [Scott Henderson](mailto:scottyh@uw.edu)

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>
