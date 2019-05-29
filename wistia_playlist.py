#This script outputs the link of each video in the playlist url. 
#TODO- merge this code with youtube-dl wista extractor.
import urllib.request
import sys
import json

test_link='http://fast.wistia.net/embed/playlists/5dfzfu5zvz'
link= str(sys.argv[1])

f = urllib.request.urlopen(link)
json_playlist= f.read().decode('utf-8').split('Wistia.iframeInit(')
json_playlist_done= json_playlist[1].split(', {});\n</script>')
obj=json.loads(json_playlist_done[0])
print ('Playlist from', link)
for total in obj:
    for video in total['medias']:
        print ('{}'.format(video['name']))
        g = open("list.txt", "a")
        g.write('http://fast.wistia.net/embed/iframe/{}\n'.format(video['embed_config']['media']['hashedId']))
        g.close()
