# Bad Apple!! but on FLTK

Three steps: <br>
1. Take any black and white video, blur it to remove rough edges, and convert into plain black and white. Then black and white => 3d array of 1s and 0s. At this point I cached the data as binary data with pickle. <br>
2. Load in the cached data and run an algorithm through every frame that converts the pixels into the least rectangles such that the rectangles cover all the pixels. This definitely isn't the most optimal algorithm, but it works for my purposes. Then cache the data again. <br>
3. Loop through the frames, and all the rectangles for that frame. If a rectangle was created the last frame that already exists, don't delete it and save some time. Delete all unused windows. Screenshot after the windows are created. <br>
[<img src='https://www.youtube.com/s/desktop/7449ebf7/img/favicon_32x32.png' width='16px'/>](https://www.youtube.com/watch?v=coyzbo8uWcs) [Link to the video](https://www.youtube.com/watch?v=coyzbo8uWcs)
