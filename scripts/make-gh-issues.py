# uses PyGitHub (https://pygithub.readthedocs.io/)

from github import Github
import os
from pprint import pprint
import configparser
from utils import read_google_sheets

df = read_google_sheets(credentials_file='../credentials.json', sheet_id='1Us-stsbBJ3XgsIPi0iIm1u5FyJPFGVgc993ppzQUBik', sheet_range='new!A1:g1000')

config = configparser.ConfigParser()
config.read('../token.config')
token = config['GitHub-api']['token']

client = Github(token)
repo = client.get_repo("snowex-hackweek/administrative")

open_milestones = repo.get_milestones(state='open')
ms_dict = {}
for milestone in open_milestones:
    ms_dict[milestone.title] = milestone.number
    
for i in range(len(df)):
    issue = repo.create_issue(
        title=df['title'][i],
        body=df['body'][i],
        assignee=df['assignee'][i],
        milestone=repo.get_milestone(number = ms_dict[df['milestone'][i]]),
        labels=[
            repo.get_label(df["label"][i])
        ]
    )

pprint(issue)
