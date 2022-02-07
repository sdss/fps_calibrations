# Changelog

## APO.2022.01.25-alpha.1
* Update boss fiber positions in positionerTable, fibers with LTC metrology and apogee measurements are used to solve for boss fiber microscopy locaitons, boss fibers without LTC measurements are adjusted by a linear fit based on LTC metrology fiber location measurement.

## APO.2021.12.25
* Fixed calculation of fiber positions
* Used for initial dither observations

## APO.FIRST.LIGHT.2021.12.09
* Add gfaCoordinates table
* Add measured Apogee and Boss locations in fiberPositionerTable based on pluglab data
* Add hack xy offset to Boss fiber locations to guess at obvious descrepancy between apogee and boss measured locations.
* Roughly 10% of fibers got hits with this config and rough "janky guiding"

## APO.2021.12.01
* Updated APO positionerTable based on danger move calibration in plug lab

## APO.2021.11.28
* Updated APO positionerTable based on safe move calibration in plug lab
* Updated APO fiducialCoords based on measured positions of spots on camera, not including outliers in fits.  GFA fiducials added.

## APO.2021.11.24

* Updated APO positionerTable for robots swapped out after OSU lab testing.
* Robot 235 replaced by Robot 935, calibration zeroed
* Robot 1395 replaced by Robot 386, calibration zeroed
* Robot 278 replaced by Robot 1264, calibration zeroed


## APO.2021.11.14

* Initial files for both APO, LCO, and UW and OSU miniwoks.
* ``sloanFlatCMM`` files with metrology.
* Baseline calibrations for duPont and Sloan.
