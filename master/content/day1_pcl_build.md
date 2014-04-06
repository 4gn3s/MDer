# Day 1
## an attempt to build PLC on Windows 7 with Vs2012

starting [here](http\://cs.unc.edu/~kwaegel/pcl/pcl_build_notes.html) and [here](http\://pointclouds.org/documentation/tutorials/compiling_pcl_windows.php#compiling-pcl-windows)

##### list of dependencies:

* __cmake__ 2.8.11.2 already installed
* __boost__ 1.55.0 downloading binary from [here](http\://sourceforge.net/projects/boost/files/boost-binaries/1.55.0-build2/boost_1_55_0-msvc-11.0-64.exe/download); installed in *C:\local\boost_1_55_0*
    * to link in vs use [this](C\:/local/boost_1_55_0/more/getting_started/windows.html)
* __qhull__ extracted to *C:\local\qhull-2012.1*, binaries already provided
* __eigen__ extracted to *C:\local\eigen*, no need to build
* __flann__
* __Qt__ 5.1.1. with opnegl alfready here
* __VTK__ 6.1.0 x64 binary downloaded from [here](http://www.vtk.org/VTK/resources/software.html)
installing in *C:\Program Files\VTK 6.1.0*
* __OpenNI2__ already installed


Overall result: unsuccessful; flann build causes errors (in syntax?!)