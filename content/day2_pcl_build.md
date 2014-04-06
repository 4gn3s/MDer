# Day 2

trying to solve problems with __flann__:

* cmake using x32 generator (why? in x64 I keep getting *left of '.serialize' must have class/struct/union*);
* disabled python and matlab bindings;
* in VS unbinded all projects with pyunit in name;
* to build INSTALL in release run VS as administrator, otherwise errors

update: managed to build x64 flann by adding:

    #ifdef _MSC_VER
    BASIC_TYPE_SERIALIZER(unsigned __int64);
    #endif


to *serialize.h*, as described in [here](https://github.com/mariusmuja/flann/issues/82)

## CMake-ing PCL (version: pull request with OpenNI2 support):

1. error: *Unable to find the requested Boost libraries.*
    WTF?? Installed using binaries provided and it can't find it?!
    -> fixed by setting env. variable `BOOST_LIBRARYDIR`
2. error: *Could NOT find Eigen (missing: EIGEN_INCLUDE_DIR)*
    -> set `EIGEN_INCLUDE_DIR`
3. build Qhull from sources & set `QHULL_INCLUDE_DIR`, `QHULL_LIBRARY`
4. error: *CMake Error at C:/Qt/qt-5.1.1-x86-msvc2012-opengl/qt-5.1.1-x86-msvc2012-opengl/lib/cmake/Qt5Gui/Qt5GuiConfigExtras.cmake:16 (message): Failed to find "glu32" in "".*
    -> added `CMAKE_PREFIX_PATH` = “C:\Program Files (x86)\Windows Kits\8.0\Lib\win8\um\x64”)'
5. still *VTK not found.*. But for the first time __no ERRORS!__
    no option other than to build VTK myself; it can'e be that easy: VTK doesn't work with QT5
    -> solved by changing `VTK_QT_VERSION` cmake option from 4 to 5. (“Advanced” to show this option)
    OH GREAT, but I have Qt x32, and VTK wants x64->downloading binary `qt-opensource-windows-x86-msvc2012_64_opengl-5.2.1`
    and changing `QT_DIR` after install


## Building PCL
176 errors, canceled build after ~45 mins.

OK, it seems that PCL doesn't support VTK v.6 :(
So again I will have to download the sources and build VTK...


