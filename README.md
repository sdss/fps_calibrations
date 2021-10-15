# FPS calibration files

This repository contains calibration files for the FPS, including positioner metrology, wok measurements, and optic fibre assemblies.

To use this product git clone it and then add its path to `$FPS_CALIBRATIONS_DIR`. To be able to get the version of the calibrations, add the same path to `$PYTHONPATH` then do

```python
>>> import fps_calibrations
>>> fps_calibrations.get_version()
'0.1.1+04b4763'
```

The version will include the Git hash unless the product is not a Git repository (e.g., if the `.git` directory has been removed) or if the HEAD matches a tag.
