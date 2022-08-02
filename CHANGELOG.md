# Changelog

* Updated fiberAssignments for sloanFlatCMM with comments on spliced fibres.

## APO.2022.08.02
* Modify positionerTable and fiberAssignments table to account for robot 463 replaced by 758 and robot 1340 replaced with 56.  Fix error in FPI fiber accounting in wokCoords file R0C1 has an Apogee fiber, R-13C14 does not have an Apogee fiber.

## APO.2022.06.01
* Pre-shutdown tag.  BOSS fiber locations updated based on dithers.

## APO.2022.04.21
* Meged sciFiberMeas branch: update boss fiber positions in positionerTable, fibers with LTC metrology and apogee measurements are used to solve for boss fiber microscopy locations, boss fibers without LTC measurements are adjusted by a linear fit based on LTC metrology fiber location measurement.

## APO.2022.02.07
* Swapped BOSS fibres 78 and 80.

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
