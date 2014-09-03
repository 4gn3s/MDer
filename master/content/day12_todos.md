#Day 12 TODOs progress
* [x] add system variables for PCL, VTK, Eigen etc. and change paths in VS under _additional include dirs_ and _linker->input_
* [x] check if point cloud visualization actually works
* [ ] __Matcher.cpp__ is a mess- reorganize the whole class, implement interfaces, etc.
* [ ] add Optical Flow based matcher for camera tests later
* Start SFM:
    * [ ] camera matrices
    * [x] triangulation
    * [ ] add many views: _solvePnp_
    * [ ] Bundle Adjustment (later from OpenMVG or mine)
    * [ ] results to point cloud
    * [ ] filter out the cloud
    * [ ] create surface, normals etc.
