"""
requires the "PyGitHub" package (`pip install pygithub`).
You can leave out things like an assignee, a label etc., by simply leaving them out of the code.
"""


from github import Github
import os
from pprint import pprint
import configparser
from utils import read_google_sheets

df = read_google_sheets(credentials_file='../credentials.json', sheet_id='1Us-stsbBJ3XgsIPi0iIm1u5FyJPFGVgc993ppzQUBik', sheet_range='A1:g1000')

config = configparser.ConfigParser()
config.read('../token.config')
token = config['GitHub-api']['token']

client = Github(token)
repo = client.get_repo("snowex-hackweek/administrative")
for i in range(len(df)):
    issue = repo.create_issue(
        title=df['title'][i],
        body=df['body'][i],
        assignee=df['assignee'][i],
        labels=[
            repo.get_label(df["label-1"][i]), repo.get_label(df["label-2"][i]), repo.get_label(df["label-3"][i])
        ]
    )

pprint(issue)
