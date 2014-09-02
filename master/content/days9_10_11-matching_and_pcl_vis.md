#Days 9, 10, 11

###Usage of __QVTKwidget__ for PCL visualization instead of writing a _GLWidget_ class with VBOs. Problems:

* Was using Qt5, but QVTK widget depends on Qt4 -> solution: _downgrade the entire project_
* problems with __"QWidget: Must construct a QApplication before a QPaintDevice"__ solved as mentioned [here](http://www.vtk.org/Wiki/VTK/FAQ#Shared_builds_of_VTK_and_debugging_QVTKWidget_using_Visual_Studio)
    * removed VTK, Qt from the PATH
    * added VTK in Environment section in VS
    * VTK INSTALL is missing /debug files, so copied them manually from build folder to newly created /debug under /bin and /lib in VTK_DIR, also chaged paths in VS (added /debug)
* QT visualizer added as described [here](http://pointclouds.org/documentation/tutorials/qt_visualizer.php#qt-visualizer)

##some TODOs
* add system variables for PCL, VTK, Eigen etc. and change paths in VS under _additional include dirs_ and _linker->input_
* check if point cloud visualization actually works
* __Matcher.cpp__ is a mess- reorganize the whole class, implement interfaces, etc.
* add Optical Flow based matcher for camera tests later
* Start SFM:
    * camera matrices
    * triangulation
    * add many views: _solvePnp_
    * Bundle Adjustment (later from OpenMVG or mine)
    * results to point cloud
    * filter out the cloud
    * create surface, normals etc.

