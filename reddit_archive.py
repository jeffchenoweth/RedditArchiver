import praw
import archiveis
import sys
import ConfigParser

def main(config_section):
    config_dict = {}
    options = ["client_id", "client_secret", "user_agent", "username", "password", "subreddit", "url"]
    Config = ConfigParser.ConfigParser()
    Config.read("archiver.cfg")
    sections = Config.sections()
 
    if(config_section not in sections):
        print(config_section + " not found in archiver.cfg")
        return

    for option in options:
        try:
	    config_dict[option] = Config.get(config_section, option)
            # optional debugging:
            # print(option + ": " + config_dict[option])
	except:
            print("exception on %s" % option)
	    return
    try:
	# starts praw instance
        reddit = praw.Reddit(client_id=config_dict["client_id"], 
                             client_secret=config_dict["client_secret"],
                             user_agent=config_dict["user_agent"], 
			     username=config_dict["username"], 
                             password=config_dict["password"])
        subreddit = reddit.subreddit(config_dict['subreddit'])

    except Exception as x:
	print x
	return

    for submission in subreddit.stream.submissions():
        process_submission(submission, config_dict["url"])

def process_submission(submission, url):
    if submission.url.find(url) > -1:
        print submission.url
        try:
            #load all top-level comments (since monitoring stream there should not be many)
            submission.comments.replace_more(limit=None)
	    for comment in submission.comments:
		# check if archive already exists in top level comments
                if comment.body.find('archive.is') > 1: 
                    print comment.body
                    return
            short_url = archiveis.capture(submission.url)
	    submission.reply(short_url)
        except Exception as x:
           print x
           return

if __name__ == '__main__':
    usage = "usage: python reddit_archive.py <archiver.cfg section header> \nexample: python reddit_archive.py subreddit_1"
    try:
        section_header = sys.argv[1]
        	
	if(section_header == "-h" or section_header == "--help"):
            print(usage)
	else: main(section_header)
    except Exception as x:
        print(usage)

    

