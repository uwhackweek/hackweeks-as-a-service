# Tutorial Notebooks

This section will focus on the practicalities of presenting tutorial content through a Jupyter notebook.

## Structure 

We recommend that all notebooks make use of sections with the following minimal structure:
```
# Title
* Learning objectives *
## Software
## Data
## My Section
### My Subsection
## Summary
## References
```

For convenience you can start with a copy of our [template notebook](https://uwhackweek.github.io/jupyterbook-template/tutorials/example/tutorial-notebook.html), which you can download [here](https://github.com/uwhackweek/jupyterbook-template/raw/main/book/tutorials/example/tutorial-notebook.ipynb).

## Signposting

```{image} ../images/tutorials-boxes.png
:alt: A screenshot of a jupyter notebook with several cells decorated with attention-grabbing formatting
:width: 20em
:align: right
```

Signposting is a general writing technique that involves using language specifically intended to prime a reader's expectations and prepare them to navigate the upcoming content. We naturally signpost when talking with others, to the extent that it can seem to obvious to be worth mentioning: prefacing the conclusion of a presentation with the phrase "Let's Recap."

In the context of reference texts like tutorial notebooks, however, signposting and related strategies can help a lot with making relevant content stand out in the deluge of learning material. Here are some strategies:

- Put new terminology in **bold** when introducing it
- Use section headers liberally, as you would functions when turning an unruly script into readable and reusable code.
- Identify one or two important notes or take-aways per section, and set them aside in [colored note boxes](https://gist.github.com/DanielKotik/4b81480c479a57e0dd13ac4d153e4451). This is great for things like common debugging pitfalls or data access instructions

## Images and figures

Notebooks can contain a wide variety of embedded media (images, videos, equations, etc.) and can be easily rendered on hackweek event websites. Try including figures and images even when they don't seem absolutely necessary to get the point across. Visual diversity can greatly help readers work through a long document.


## Examples

Spend a bit of time looking at these examples from past events:

| Description | Links |
| - | - |
| SnowEx 2021 Thermal IR | [rendered](https://snowex-2021.hackweek.io/tutorials/thermal-ir), [download](https://github.com/snowex-hackweek/website/raw/main/book/tutorials/thermal-ir/thermal-ir-tutorial.ipynb) |