# ytplaylisttofile
This Python 3 script allows you to bulk grab a YouTube playlist page, strip out the urls and save them to a text file. It's a little non straight forward but it does work and give you a working list to use for whatever reason you need a scraped channel list of video [yt-dlp](https://github.com/yt-dlp/yt-dlp) batch downloads for example.

I wrote this as the yt-dlp method for getting a playlist to bulk download was not working for me (kept download a standard consent page), I know I could play around and tie my session ID to everything but I want to keep everything seperate.

The script accepts the following arguments and abbreviations:
```usage: ytplgrab.py [-h] --infile INFILE --outfile OUTFILE

Strip YT video links from html to new file
Visit https://github.com/NebularNerd/ytplaylisttofile for more information

optional arguments:
  -h, --help            show this help message and exit
  --infile INFILE, -i INFILE
                        Path to input raw html from YT Playlist page
  --outfile OUTFILE, -o OUTFILE
                        Path to output processed file
```

## Usage
Using this is slightly awkward, but equally once you know very easy, this is based on Chrome, Edge and FireFox should be able to do similar:

### Step One
1) Head to a playlist page, hover over the first video, right click and use select ```Inspect```.
2) Once you can see the code look above your inspected element for a div with ```id="contents"``` and left click that, the playlist should highlight similar to below.
![Example playlist page](https://raw.githubusercontent.com/NebularNerd/ytplaylisttofile/main/ytplaylisttofile-example%20grab.jpg)
3) Right click that div and select ```Copy > Copy Element``` to grab the whole div with all the vids.
4) Paste this into a blank text file and save it.

### Step Two
Open a console/command prompt and run something similar to the below, adjust dirs and drives as required:
```python C:\python\ytplgrab.py -i R:\ytin.txt -o R:\ytdone.txt```
It will chew through the input file, find any vids, remove duplicates, create the output file with one video url to a line. This can then be used for what ever purpose you needed that list of url's for. For example, this might be handy for some:
```yt-dlp.exe --ffmpeg-location "C:\FFMpeg\bin" --user-agent "Chrome/89" -o "R:\Video\%%(title)s.%%(ext)s" -f "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b" --verbose --batch-file R:\ytdone.txt```

## Future plans:
- Tidy code and add file exists check/override (either as y/n or commandline arg or both)
- PyGUI based GUI to make it more point and click, could allow for multiple systems to be output into one file
- Suggestions?

## License:
None, honestly use this code as you want, if you fork it or whatever please be kind enough to tag me as the original creator.
