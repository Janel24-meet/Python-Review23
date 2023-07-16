def create_youtube_video(title, description):
	youtube_vid = {'title': title, 'description': description, 'likes': 0, 'dislikes': 0, 'comments': {}}
	
	return youtube_vid

def like(youtube_video):
	if 'likes' in youtube_video:
		youtube_video['likes'] += 1

	return youtube_video

def dislikes(youtube_video):
	if 'dislikes' in youtube_video:
		youtube_video['dislikes'] += 1

	return youtube_video

def add_comment(video, username, comment_text):
	video['comments'][username] = comment_text

	return video

vid=create_youtube_video(str(input('enter title: ')), str(input('enter description: ')))
for i in range(495):
	vid=like(vid)
vid=dislikes(vid)
vid=add_comment(vid, str(input('enter username: ')), str(input('enter comment: ')))
print(vid)