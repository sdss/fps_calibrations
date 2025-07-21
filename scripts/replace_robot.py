#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2025-07-21
# @Filename: replace_robot.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations

import pathlib
from typing import Literal

import polars

FIBER_ASSIGNMENTS_SCHEMA = {
    "index": polars.Int16(),
    "site": polars.String(),
    "holeID": polars.String(),
    "Sextant": polars.Int16(),
    "CAN": polars.Int16(),
    "Device": polars.String(),
    "deviceID": polars.String(),
    "ofaID": polars.Int32(),
    "Row": polars.String(),
    "Column": polars.String(),
    "apogeeST": polars.String(),
    "bossST": polars.String(),
    "metST": polars.String(),
    "BOSSFiber": polars.Int16(),
    "APOGEETrib": polars.String(),
    "MTPFiber": polars.String(),
    "LongLinkMTP": polars.String(),
    "APOGEEFiber": polars.Int16(),
    "Comments": polars.String(),
    "positionerID": polars.Int16(),
}


POSITIONER_TABLE_SCHEMA = {
    "id": polars.Int16(),
    "site": polars.String(),
    "holeID": polars.String(),
    "positionerID": polars.Int16(),
    "robotailID": polars.String(),
    "wokID": polars.String(),
    "apSpecID": polars.Int16(),
    "bossSpecID": polars.Int16(),
    "alphaArmLen": polars.Float64(),
    "metX": polars.Float64(),
    "metY": polars.Float64(),
    "apX": polars.Float64(),
    "apY": polars.Float64(),
    "bossX": polars.Float64(),
    "bossY": polars.Float64(),
    "alphaOffset": polars.Float64(),
    "betaOffset": polars.Float64(),
    "dx": polars.Float64(),
    "dy": polars.Float64(),
}


def read_fiber_assignments(path: pathlib.Path | str) -> polars.DataFrame:
    """Reads the fiber assignments file."""

    path = pathlib.Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File {path} does not exist.")

    df = polars.read_csv(
        path,
        has_header=True,
        schema=FIBER_ASSIGNMENTS_SCHEMA,
    )

    return df.sort("index")


def update_fiber_assignments(
    path: pathlib.Path | str,
    old_positioner_id: int,
    new_positioner_id: int,
    new_ofa_id: int | None = None,
) -> None:
    """Updates the fiber assignments file."""

    f_ass = read_fiber_assignments(path)

    row_index = f_ass.row(
        by_predicate=polars.col.positionerID == old_positioner_id,
        named=True,
    )["index"]

    deviceID_col = f_ass["deviceID"]
    ofaID_col = f_ass["ofaID"]
    positionerID_col = f_ass["positionerID"]

    new_deviceID = f"P{new_positioner_id:04d}"
    deviceID_col[row_index] = new_deviceID

    ofaID_col[row_index] = new_ofa_id
    positionerID_col[row_index] = new_positioner_id

    f_ass = f_ass.with_columns(deviceID_col, ofaID_col, positionerID_col)
    f_ass.write_csv(path)


def update_positioner_table(
    path: pathlib.Path | str,
    old_positioner_id: int,
    new_positioner_id: int,
    sort_ids: bool = False,
) -> None:
    """Updates the positioner table file."""

    path = pathlib.Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File {path} does not exist.")

    df = polars.read_csv(
        path,
        has_header=True,
        schema=POSITIONER_TABLE_SCHEMA,
    )

    row_index = df.row(
        by_predicate=polars.col.positionerID == old_positioner_id,
        named=True,
    )["id"]

    positionerID_col = df["positionerID"]
    positionerID_col[row_index] = new_positioner_id
    df = df.with_columns(positionerID_col)

    zero_columns = ["alphaOffset", "betaOffset"]
    for col in zero_columns:
        df[row_index, col] = 0.0

    if sort_ids:
        df = df.drop("id").sort("positionerID").with_row_index("id")
    else:
        df.write_csv(path)


def sort_positioner_table(path: pathlib.Path | str) -> None:
    """Sorts the positioner table by positionerID and updates the file."""

    df = polars.read_csv(
        path,
        has_header=True,
        schema=POSITIONER_TABLE_SCHEMA,
    )

    df = df.drop("id").sort("positionerID").with_row_index("id")
    df.write_csv(path)


def replace_robot(
    observatory: Literal["APO", "LCO"],
    old_positioner_id: int,
    new_positioner_id: int,
    new_ofa_id: int | None = None,
):
    """Replaces a robot positioner ID in the fiber assignments file."""

    observatory = observatory.upper()  # type: ignore[assignment]
    if observatory not in ["APO", "LCO"]:
        raise ValueError("Observatory must be either 'APO' or 'LCO'.")

    cwd = pathlib.Path(__file__).parent
    if observatory == "APO":
        wok_model = "sloanFlatCMM"
    else:
        wok_model = "duPontFlatCMM"

    fiber_assignments_path = (
        cwd
        / f"../{observatory.lower()}/wok_calibs"
        / wok_model
        / "fiberAssignments.csv"
    )

    update_fiber_assignments(
        fiber_assignments_path,
        old_positioner_id,
        new_positioner_id,
        new_ofa_id=new_ofa_id,
    )

    positioner_table_path = (
        cwd / f"../{observatory.lower()}/wok_calibs" / wok_model / "positionerTable.csv"
    )

    update_positioner_table(positioner_table_path, old_positioner_id, new_positioner_id)
