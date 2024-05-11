# Tutorial Design

This section will focus on designing and editing the intellectual content of your tutorial, with an eye towards the different contexts in which it will be used (synchronous and asynchronous).

## Getting started


Starting from scratch on any project can feel like a daunting task. To overcome "blank page syndrome," we recommend the "backwards design" process in which we start by defining the core outcomes we hope for our audience to experience, and then refine to further detail from there. In the rest of this chapter, we'll go into detail about each stage:


```{image} ../images/tutorials-granularity.png
:alt: TODO
:width: 100%
:align: center
```

This process is heavily inspired by the [Software Carpentry Curriculum Development](https://carpentries.github.io/workbench/) model for building learning content.

```{important}
A hackweek tutorial is *learning-oriented* and should guide participants through a step-wise process with a meaningful outcome.
```

### Learning Goals


```{image} ../images/tutorials-lighthouse.gif
:alt: A toy lighthouse
:width: 25%
:align: right
```

A tutorial's learning goals are a set of succinctly stated objectives the audience is intended to achieve through their participation in the content. As tutorial authors, they serve as our guiding light to determine what content we need to produce and what content we can reasonably ignore.

Although there are many ways to articulate a lesson's goals, we recommend the following structure to hold ourselves accountable later in the design process:

- Write them as a bulleted list, with one goal per bullet.
- Use a consistent format for each goal's phrasing. For example, state each goal as a single sentence that begins with “Students will be able to…”
- Expect to achieve 2-3 goals per 50 minutes of synchronous tutorial time
- Make goals concrete enough to be measurable using some sort of interactive activity. It doesn't matter whether you actually have time for said activities or not -- just know that if you can't articulate an activity to measure a goal, it is likely too general.


```{note}
Learning goals primarily describe the outcome of the _synchronous time_ spent during tutorial delivery (as opposed to what participants will gain throughout the week when using your material as a reference).
```

```{warning}
TODO: learning goals example
```

### Content Outline

```{image} ../images/tutorials-outline.png
:alt: A cat sculpture getting successively more refined
:width: 25%
:align: left
```
TODO: cite figure: https://www.instagram.com/yamaneko5656/

Using our learning goals as a framing device, we can write an outline describing the intellectual content needed to achieve those desired outcomes. The outline takes the form of a longer bullet list that tersely expresses “everything you need to know” about the topic of the tutorial, roughly in the order it will be covered during synchronous lesson time. Sub-bullets in the list get to increasing levels of detail.

The outline is our key tool for being able to keep track of varying levels of detail throughout the rest of the design process, though it also serves several other uses:
- Discussing content amongst the teaching team
- Understanding the narrative arc of the intellectual information
- Adjusting “air time” given to any given topic
- Identifying logical gaps that need to be filled in
- Just getting started!

Although tutorial outlines don't necessarily use their learning goals as the top-level bullet points, it's often a good way to get started.


```{note}
**Example outline**

Feeding yourself: a workshop for new college students

- Students will be able to find ingredients
    - Selecting a grocery store
        - Trader Joes vs. Whole Foods vs. Safeway
        - Pricing differences
        - Specialty ingredients and “absolute needs”
    - Finding ingredients
        - Search by aisle
        - Bulk bins
        - Shelf stable vs refrigerated (eg, pickles)
    - Checkout
        - Cashier
        - Self checkout
                • PLU codes
                • Barcode scanning
                • By weight
- Students will be able to make a sandwich
    - Getting out ingredients
        - Identify minimum ingredient set by recipe, put on counter
        - Remove portion of refrigerated ingredients you need, put rest back in fridge
    - Assembly
    - Plating
- Students will be able to store left-over food
    - Tupperware
    - Fridge vs. shelf
    - Lifetimes

```

### Interactivity and Assessment

Once the tutorial has been outlined, instructive bullets can be punctuated with bullets describing participant activities. Activities can serve a variety of different purposes:
    - During synchronous time, they engage the audience and help maintain attention
    - They provide a way for participants to self-assess their mastery of the material
    - They provide opportunities for participants to help each other, which builds community and strengthens understanding through peer teaching.
    - They provide opportunities for structured practice of the material, which through repetition improves retention.

Some activity suggestions are outlined below, depending on the ultimate intent of the activity at a given point in our outline.

#### Attentional activities

To maintain participant engagement during long days, it can be very helpful to provide forms of interactivity that _don't_ assess a skill, but rather just have folks switch from a 'student' mode to 'participant' mode.

A common attentional activity is to ask participants to respond to a creative prompt, observing the following guidelines:
- Ask for _written_ responses through slack or zoom chat, or platforms like [particify](https://particify.de/)
- Give adequate time for shy folks to write their responses. One way to solicit them is to ask people to type their responses and hold back from posting them until you do a countdown and say "go!".
- Read back some responses out loud

It's important to not ask comprehension or mastery questions, like "describe back to me what I just said" or "we're about to talk about XYZ. can someone tell me what XYZ is". Rather, try questions like these:
- Ask for reflections on past experience
- Ask participants to brainstorm as many unique responses as possible
- Ask for participants' opinions on or “favorites of” a given subject


#### Conceptual activties

For non-technical material, several techniques are described in this [active learning strategies guide](https://drive.google.com/file/d/1lJ2Eb773tOx0Oik_G51bcWcwub20Co-4/view) and summarized in this chart:

```{image} ../images/tutorials-active-learning-strategies.png
:alt: A chart of active learning strategies [TODO enumerate them]
:width: 100%
:align: center
```

#### Technical activities

For technical material, here are some suggestions:

- Material involving data access
    - Repeat a procedure you just modeled
    - Find and share an interesting datapoint/dataset/layer
- Material involving codeing techniques
    - Fill-in-the-blanks
    - Reading pre-written code for comprehension
    - Tweak pre-written code behavior
    - Parsons problems (arranging scrambled lines of code)


### Timing and refinement

Once we've built out content for our tutorial, it's important to run through it once or twice to get a sense of how much time each section takes. Although it's helpful to do this in front of colleagues and solicit feedback, even just doing a dry run alone at your desk with a stopwatch can give critical understanding as to how well your material flows and how much content you may need to edit. 

## Editing

You're likely leading a tutorial because it is a topic that you are excited about! It is tempting to want to share all the things, but keep the *learning-oriented* framing of your tutorial in mind as you begin to plan your tutorial.

```{image} ../images/tutorials-priority.png
:alt: A chart expressing content priority [TODO describe in detail]
:width: 100%
:align: center
```

TODO: cite Veldof, Jerilyn R. Creating the One-Shot Library Workshop: A Step-by-Step Guide. Chicago: American Library Association, 2006.

TODO:

Questions to ask yourself:
- Is this piece of content critical for learning success?
- Can the learners (or will the learners) learn this content elsewhere?



## Lessons learned from previous hackweeks

* *Keep it simple and brief!* Hackweeks have a lot going on, and between tutorials, networking events, and projects there is a lot for participants to digest.

* Make your tutorials *interactive* through live coding challenges, working through a Juypter Notebook together, or interactive discussions. Leave some space when you are not talking for people to work through examples and ask questions.

* Try for content that is *broad in scope* and gives an initial picture of what might be possible when applying a particular data science tool. Save detailed explanations on a narrow topic for optional breakout sessions.

* *Start with simple explanations* that attend to people who are seeing this content for the first time, AND *keep advanced participants engaged by inviting them to assist others*, or to explore more advanced concepts through individual study.


## Formatting

An effective format for tutorial content is in the form of a Jupyter Notebook that provides participants with narrative text and interactive code examples. Notebooks can contain a wide variety of embedded media (images, videos, equations, etc.) and can be easily rendered on hackweek event websites.

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


### Examples of formatting

Spend a bit of time looking at these examples from past events:

| Description | Links |
| - | - |
| SnowEx 2021 Thermal IR | [rendered](https://snowex-hackweek.github.io/website/tutorials/thermal-ir/thermal-ir-tutorial.html), [download](https://github.com/snowex-hackweek/website/raw/main/book/tutorials/thermal-ir/thermal-ir-tutorial.ipynb) |



## References

To dig a bit deeper on some general guidance on creating technical content for a hackweek, we recommend reviewing [The Diátaxis Framework](https://diataxis.fr) for documentation.

```{note}
While we've advocated for *learning-oriented* tutorials based on the Diátaxis Framework during a hackweek, keep in mind alternative approaches that might be a good fit depending on your goals: [*understanding-oriented*](https://diataxis.fr/explanation), [*reference-oriented*](https://diataxis.fr/reference), and [*goal-oriented*](https://diataxis.fr/how-to-guides).
```
