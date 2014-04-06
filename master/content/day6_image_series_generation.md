#Day 6
###Image sequence generator

Generating images of a cube given its:

* size
* rotation angle
* rotation axis

toggling menu - *left mouse button*

###Class structure for *matching*
__input:__ series of images

__output:__ 

* matched points saved to a text file
* image pairs viewed/ saved with matches drawn

__*out data format:*__

```python
    # pair 1
point.x point.y
point.x point.y
...
point.x point.y
    # empty line
    # pair 2
point.x point.y
point.x point.y
..
point.x point.y
    # and so on
```
Decide on which detector to use:

* SIFT
    * slow
    * nice results
* SURF
   * fast
   * crappy
