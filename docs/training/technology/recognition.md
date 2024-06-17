# Recognizing Contributions

There are a variety of ways that we would like to recognize community contributions to hackweeks.

## Website Presence

We invite all people who join us in organizing and hosting a hackweek to be included in our "Meet the team" section of each hackweek website:

```{image} ../../images/meet-the-team.png
:alt: meet the team website section for bios
:width: 1100px
:align: center
```

We use a YAML template to render this portion of the website. The arrows below map the template text to how it appears on the webs:

```{image} ../../images/website-bio.jpg
:alt: example of how to fill out website bio
:width: 1100px
:align: center
```

```{warning}
So that the website correctly interprets the YAML format we recommend using our template and not changing indents or spacing.
```
- We encourage everyone to use their GitHub avatar as the source of their personal photograph (e.g. https://avatars.githubusercontent.com/USERNAME)
- Also provide your GitHub username, together with the full url, for the `link` key under `social` (https://github.com/USERNAME)
- Acceptable user_groups (Hackweek "roles") can be found [here](https://escience.washington.edu/using-data-science/hackweeks/planning/hackweek-roles).

### Uploading to the website

To include your content on the website, follow [these instructions](https://github.com/uwhackweek/jupyterbook-template/blob/main/team/README.md) or because YAML is a simple human-readable text format, you can add your content directly in the GitHub interface. We also show screenshots of doing this for a specific event below:

1. Go to https://github.com/uwhackweek/event-page-2024/blob/main/team/template.yaml and copy the contents of the template

![team template](../../images/copy-team-template.png)

1. Follow https://github.com/uwhackweek/event-page-2024/new/main/team to make a new file. Paste the template contents, rename to FIRST-LAST.yaml

![team template](../../images/create-team-entry.png)

1. Commit to a new branch and open a pull request

![team template](../../images/commit-changes.png)

1. Add the 'preview' label to your pull request to make sure your bio looks correct

![add preview](../../images/create-pull-request.png)


## Online Tutorials

All of our tutorials are recorded and shared on the [eScience Institute's youtube channel](https://www.youtube.com/c/UWeScienceInstitute/playlists). We encourage tutorial leads to link to these videos from their social media accounts and websites as a way to demonstrate their teaching competencies.

## Referrals and Feedback

The eScience Institute's hackweek as a service program will provide references for past organizers upon request. We will also offer feedback to help promote your professional development. [Contact us](mailto:escience-hackweeks@uw.edu) for more information.
