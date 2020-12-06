# Instagram-Comment-Bot

A simple but yet useful app, which the user can like, comment multiple posts and choose randomly comments to post.

## Files:

* **bot2.py** : The newest version of the program we are going to compile.

* **comments.txt** : In this file, the user can put the comments that he wants to post. The comments will be choosen randomly among the set.

* **requirements.txt** : The necessary packages we need to download.

* **posts.txt** : The posts that the user wants to comment.

* **backup_old**: Backup directory with older version of the program.

* **geckodriver*** : Necessary WebDriver files for Firefox.  

## Compile and run:

First, to download the program, simply type: `$ git clone https://github.com/dfwteinos/Instagram-Comment-Bot.git`

Then, you need to download the necessary requirements:

`$ pip3 install requires`

`$ pip3 install -r requirements.txt`

And finally, just type: `$ python3 bot2.py -u username -p password -c comments_per_post`

**Done:**

1.  Accept the cookies. :heavy_check_mark:
2.  Succesfully log-in with given username and password. :heavy_check_mark:
3.  Like the post if it's Unliked. Don't unlike it if it's liked. :heavy_check_mark:
4.  Automated the number of comments we can do at each post. :heavy_check_mark:

**TODO:** 

1.  Automate follow for specific users. :x:	
2.  Automate the numbers of different users that can log-in and do some comments. :x:	

## Main idea:

From time to time, there are many instagram celebrities,influencers e.t.c, that are doing some big Giveaways. The "conditions" are often simple, for example the only things you have to do in order to participate is to follow some pages, mention 3 different persons in the comments, and like the post. These things are very easy to be done with python and some cool tools. So, 1 comment = 1 participation. Thus, the more comments someone does, the more likely is to win.

So the main idea is to feed our program with some accounts, and let the technology do the rest. Yet, there are many parameters that we must consider, like the max number of comments we can do per hour,day, or even a week. After a specific number of comments, instagram is deactivating your ability to comment for some time.

Finally, the main equation here is: `accs*cpd`. Accs is for the number of accounts and cpd is a **constant** number and its equal to number of comments you can do per day. Unfortunately, after some research, we found that cpd is equal to ~250.

An average Giveaway from an greece's influencer, can start at 100.000 comments and reach up to 30.000.000(!). So let's say that in the worst case (this with 100.000 comments), in order to have a seriously good odds to win (let's say 50% for example), we must create 100.000/250 = 200 accounts! That's an insane number to do by hand. So the "secret" here is to automate the account creation. (Maybe will do it in future). 
