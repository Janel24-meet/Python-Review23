def create_youtube_video(title, description):
	hashtags = set()
	for i in range(5):
		hashtags.add(input("hashtag: "))
	youtube_vid = {'title': title, 'description': description, 'likes': 0, 'dislikes': 0, 'comments': {}, 'hashtags':hashtags}
	
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

def similarity_to_video(v1,v2):
	s_vid1 = v1['hashtags']
	s_vid2 = v2['hashtags']
	similiar_set = s_vid1.intersection(s_vid2)
	float_percentage = len(similiar_set) / max(len(s_vid1), len(s_vid2))
	return str(100*float_percentage) + '%'

vid=create_youtube_video(str(input('enter title: ')), str(input('enter description: ')))
for i in range(495):
	vid=like(vid)
vid=dislikes(vid)
vid=add_comment(vid, str(input('enter username: ')), str(input('enter comment: ')))
print("here is the first video")
print(vid)
vid2=create_youtube_video(str(input('enter title: ')), str(input('enter description: ')))
for i in range(495):
	vid2=like(vid2)
vid2=dislikes(vid2)
vid2=add_comment(vid2, str(input('enter username: ')), str(input('enter comment: ')))
print("here is the second video")
print(vid2)

pec=similarity_to_video(vid,vid2)
print("the simillarty percentage bettween the hashtags in the 2 videos is: " + pec)
