# Bad Apple!! but on FLTK

Four steps: <br>
1. Take any black and white video, blur it to remove rough edges, and convert into plain black and white. Then black and white => 3d array of 1s and 0s. At this point I cached the data as binary data with pickle. <br>
2. Load in the cached data and run an algorithm through every frame that converts the pixels into the least rectangles such that the rectangles cover all the pixels. This definitely isn't the most optimal algorithm, but it works for my purposes. Then cache the data again. Do this twice, targetting the black and white pixels separately.<br>
3. Loop through the frames, and all the rectangles for that frame. If there are more white rectangles than black rectangles, render the black windows as "background" and the white rectangles on top as "foreground".<br>
4. If a rectangle was created the last frame that already exists, don't delete it and save some time. Delete all unused windows. Screenshot after the windows are created. <br>
[<img src='https://img.youtube.com/vi/coyzbo8uWcs/0.jpg'/>](https://www.youtube.com/watch?v=coyzbo8uWcs) <br>[Link to the video](https://www.youtube.com/watch?v=coyzbo8uWcs) <br>
