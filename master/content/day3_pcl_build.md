#Day 3

VTK 5 doesn't support Qt 5, so I have to build Qt 4.8 from sources (no x64 binaries are provided), following [that answer on SO]

####This is starting to get silly

next building VTK 5 in debug (time: *00:44:56.22*) & release (time: *00:37:25.25*) and I'm like
![waiting][gentelman]

OK, and so we go to PCL.
While opening the project in VS it loads for about 10 minutes or so, that's why: 
![long loading][pcl solution load]

Problems:

1. CMake Eigen path incorrect
2. CMake flann path pointing to x86 flann
3. *serialization.h* x64 bug in PCL again (probably will be solved by linking the correct version of flann)

Can't build some apps because of QVTK missing,
seems that to have QVTK you not only need to build VTK with Qt, but also set following variables to true:

    VTK_USE_QT 
    VTK_USE_GUISUPPORT
    BUILD_SHARED_LIBS

### Great, so we're building VTK yet *again*

* debug: *03:57:27.99* ok just kidding, went to lunch in the meantime
* release: *00:39:18.70*

## Building PCL:

* debug *01:12:06.28*

![errors debug][pcl debug]

* release *much longer*

![errors release][pcl release]

All the errors are of PCL\_CC\_*SOMETHING*, hopefully I'm not gonna need that. (__CloudCompare?__ - of so, not suprising, I haven't installed that)

[that answer on SO]: http://stackoverflow.com/questions/12113400/compiling-qt-4-8-x-for-visual-studio-2012
[gentelman]: http://i.imgur.com/Yf0tR4v.gif "Waiting..."
[pcl solution load]: http://i.imgur.com/BTW1lcA.png "Long loading PCL solution"
[pcl debug]: http://i.imgur.com/NuTqavy.png "Errors in debug build"
[pcl release]: http://i.imgur.com/WsPvSIl.png "Errors in release build"

