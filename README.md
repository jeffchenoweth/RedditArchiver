# RedditArchiver
Take links from Reddit submissions and generate reply with webpage archive.

### Required packages:

praw: https://pypi.org/project/praw/

archiveis: https://github.com/pastpages/archiveis

### Configuration (archiver.cfg):

One section header per subreddit and hostname to monitor.  Bot requires registration at https://www.reddit.com/prefs/apps

```
[subreddit_1]
user_agent: <user_agent string>
client_id: <reddit client_id>
client_secret: <reddit client secret>
username: <reddit username>
password: <reddit password>
url: <hostname to monitor submissions for>
subreddit: <subreddit to monitor>
```
  
### Usage:

```bash
python reddit_archiver.py <section_header from archiver.cfg>
```
