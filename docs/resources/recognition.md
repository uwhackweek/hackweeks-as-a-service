# Recognizing Contributions

There are a variety of ways that we would like to recognize community contributions to hackweeks. 

## Website Presence

We invite all people who join us in organizing and hosting a hackweek to be included in our "Meet the team" section of each hackweek website. 

We use this YAML markdown template for each team member. 

```
- title: 
  avatar: 
  role: 
  organizations:
  - name: 
    url: 
  - name: 
  bio: 
  expertise:
  - 
  - 
  social:
  - icon: github
    icon_pack: fab
    link: 
  user_groups:
  - 
  ```

The first step is to copy the text above into your favorite editor and add your information. Here is an example of how the text you include gets rendered on the website:

  ```{image} ../images/website-bio.jpg
:alt: example of how to fill out website bio
:width: 1100px
:align: center
```

Note that it is important to precisely follow the indentation and spacing layout shown here, so that the website correctly interprets the YAML format. Also, we encourage everyone to use their GitHub avatar as the source of their personal photograph.

## Uploading to the website

There are two ways you can upload your information so that we can include you on the website:

1. send the completed YAML file to one of the lead organizers, and they will push it to the website
2. If you're familiar with GitHub, make a pull request to the `team.yaml` file located in the website for the event you're involved with. For example, here is the [file for the ICESat-2 2022 hackweek](https://github.com/ICESAT-2HackWeek/website2022/blob/main/book/team.yaml). 