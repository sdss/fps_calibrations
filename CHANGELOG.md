# Changelog

## 2024.03.27
* new nudge model at APO (Dec 8 2023)
* updated GFA locations at APO and LCO

## 2023.12.08
* ~ (0.2,0.2) arcsecond shift of GFAs with respect to robots for LCO gfaCoords
* removed junk column in gfaCoords for APO

## 2023.09.29
* update LCO nudge model after baffle reinstall and FVC refocus
* update APO nudge model after FVC refocus

## 2023.07.27
* Update GFA locations at APO and LCO to minimize guide rms at both sites and zero the cherno offsets at APO.

## 2023.01.21
* Swap APOGEE fibres 151-160 with 181-190 at LCO
* Update LCO GFA coordinates in translation and rotation after FPS remount (from 2022-10-26 but never properly committed).

## 2023.01.05
* Updated fiberAssignments and positionerTable after robot swaps in October 2022 and rehoming.
* Updated LCO gfaCoords (mostly rotation).
* Update fibreAssignments at LCO with monolithic slit.
* Update BOSS fibre positions for 16 APO robots replaced in October.

## 2022.09.11
* Fix `sloanFlatCMM` fiberAssignments. After the swap of robots 463->758 and 1340->56, the `positionerID` column had not been updated.

## 2022.09.10
* Translate LCO GFAs to be centered on wok=0.

## APO.2022.08.02
* Modify positionerTable and fiberAssignments table to account for robot 463 replaced by 758 and robot 1340 replaced with 56. Fix error in FPI fiber accounting in wokCoords file R0C1 has an Apogee fiber, R-13C14 does not have an Apogee fiber.
* Updated fiberAssignments for sloanFlatCMM with comments on spliced fibres.

## APO.2022.06.01
* Pre-shutdown tag. BOSS fiber locations updated based on dithers.

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
* Updated APO fiducialCoords based on measured positions of spots on camera, not including outliers in fits. GFA fiducials added.

## APO.2021.11.24

* Updated APO positionerTable for robots swapped out after OSU lab testing.
* Robot 235 replaced by Robot 935, calibration zeroed
* Robot 1395 replaced by Robot 386, calibration zeroed
* Robot 278 replaced by Robot 1264, calibration zeroed


## APO.2021.11.14

* Initial files for both APO, LCO, and UW and OSU miniwoks.
* ``sloanFlatCMM`` files with metrology.
* Baseline calibrations for duPont and Sloan.
