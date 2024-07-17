def create_youtube_video(title,description):
	youtube={}
	youtube["title"]=title
	youtube["description"]=description
	youtube["likes"]=0
	youtube["dislikes"]=0
	youtube["comments"]={}
	return youtube

def like(youtube):
	if "likes" in youtube:
		    youtube["likes"] += 1
	return youtube

def dislike(youtube):
	if "dislikes" in youtube:
		    youtube["dislikes"] += 1
	return youtube

def add_comment(youtube,username,comment_text):
	youtube["comments"][username]=comment_text
	return youtube

new_youtube_video = create_youtube_video("0OP 101 with Loai!", "This tutorial helps you successfully review most of the material learned so far in Y1 Summer and Yearlong, so we can start the Y2 Summer super strong and elevate you to a whole new level in CS by the end of the summer!!!")
new_youtube_video = add_comment(new_youtube_video, "Loai", "YO000 first video ya'11! Fame, here we come")
new_youtube_video = add_comment(new_youtube_video, "Lyel", "Thanks! Been looking for something like this for so long.")
for _ in range(495):
     new_youtube_video = like(new_youtube_video)
for _ in range(123):
     new_youtube_video = dislike(new_youtube_video)
new_youtube_video = dislike(new_youtube_video)
print(f"Title: {new_youtube_video['title']}")
print(f"Description: {new_youtube_video['description']}")
print(f"{new_youtube_video['likes']} people liked this :)")
print(f"{new_youtube_video['dislikes']} people disliked this :(")
print("\nComments:")
for username, comment in new_youtube_video['comments'].items():
    print(f"{username}: {comment}")