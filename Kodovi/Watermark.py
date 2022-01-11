import moviepy.editor as mp

video = mp.VideoFileClip("video.mp4")

watermark = (mp.ImageClip("watermark.png")
          .set_duration(video.duration)
          .set_pos(("center")))

txt_clip = (mp.TextClip("GeeksforGeeks").set_pos('center'))

final = mp.CompositeVideoClip([video, txt_clip])
final.write_videofile("test.mp4")
