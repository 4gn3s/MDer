#Days 7-8

Created the project in VS2012. Linked Qt 5.3 x64 with OpenGL and OpenCV.

###Work completed:
* Some GUI
* Loading a series of images from a directory
* Matching class structure:
    * _ImageInfo_ class, that contains a single image with its keypoints,
    desriptors etc.
    * _Matcher_ class, that performs feature detection and matching and
      creates debug images.

      __Maybe change FlannBasedMatcher for BruteForce later. Also Add SIFT.
      Work on tests that filter out some of the connections.__

###TODO NEXT:
* Output matching results to file
* View debug matching results in one of the tabs
* CREATE POINT CLOUD

![screen][days78]

[days78]: assets/images/day78.png
