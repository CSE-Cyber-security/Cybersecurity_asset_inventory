# Cybersecurity Asset Inventory System

**Weekly Mini Project — 01**

A menu-driven Python application that lets a security administrator maintain an
inventory of an organization's IT assets, classify them by type and risk, and
see at a glance which assets need attention.

---

## Problem Statement

An organization maintains several IT assets such as computers, servers, routers,
switches and software applications. Managing these manually makes it difficult to
identify the assets, track their security status, and determine which ones require
immediate attention.

This system allows an administrator to **add, search, update, delete and display**
information about the organization's IT assets, classifying each asset by its
type and security risk level.

---

## Features

- Add a new asset with all required details
- Search for an asset by its Asset ID
- Update an existing asset's details
- Delete an asset from the inventory
- Display all assets in a formatted report
- Display a security summary with risk-wise counts
- Input validation on every menu-based field
- Automatic saving and loading of data from `data/assets.json`

---

## Asset Fields

Each asset record stores the following eight fields:

| Field | Description |
|---|---|
| Asset ID | Unique identifier for the asset (primary key) |
| Asset Name | Friendly name, e.g. `HR-PC-01` |
| Asset Type | Category of the asset |
| IP Address | Network address of the asset |
| Operating System | OS running on the asset |
| Owner/Department | Department responsible for the asset |
| Risk Level | Impact if the asset is compromised |
| Security Status | Current security condition of the asset |

### Allowed Values

**Asset Type**

| Option | Value |
|---|---|
| 1 | Workstation |
| 2 | Server |
| 3 | Router |
| 4 | Switch |
| 5 | Application |

**Risk Level**

| Option | Value |
|---|---|
| 1 | Low |
| 2 | Medium |
| 3 | High |
| 4 | Critical |

**Security Status**

| Option | Value |
|---|---|
| 1 | Secure |
| 2 | Warning |
| 3 | Vulnerable |

Any input outside these options is rejected and the user is asked again.

---

## Repository Structure

```
Week-01-Cybersecurity-Asset-Inventory/
│
├── src/
│   └── asset_inventory.py
│
├── data/
│   └── assets.json
│
├── tests/
│   └── test_cases.md
│
├── screenshots/
│   ├── 01-add-asset.png
│   ├── 02-display-assets.png
│   ├── 03-search-asset.png
│   ├── 04-update-asset.png
│   ├── 05-delete-asset.png
│   ├── 06-security-summary.png
│   └── 07-input-validation.png
│
└── README.md
```

---

## How to Run

**Requirements:** Python 3.x (no external libraries needed — uses only the
built-in `json` and `os` modules).

Run the program **from the project root folder**, so that `data/assets.json`
is created in the correct location:

```bash
python src/asset_inventory.py
```

The main menu appears:

```
========== CYBERSECURITY ASSET INVENTORY ==========
1. Add Asset
2. Search Asset
3. Update Asset
4. Delete Asset
5. Display All Assets
6. Display Summary
7. Exit
```

Enter the number of the operation you want to perform.

---

## Sample Output

```
=========================================
       CYBERSECURITY ASSET INVENTORY
=========================================
Asset ID : A101
Asset Name : HR-PC-01
Asset Type : Workstation
IP Address : 192.168.1.10
OS : Windows 11
Department : HR
Risk Level : Medium
Status : Secure
-----------------------------------------
Asset ID : A102
Asset Name : Web-Server
Asset Type : Server
IP Address : 192.168.1.20
OS : Ubuntu
Department : IT
Risk Level : Critical
Status : Vulnerable
-----------------------------------------
Asset ID : A103
Asset Name : Core-Router
Asset Type : Router
IP Address : 192.168.1.1
OS : Cisco IOS
Department : Network
Risk Level : High
Status : Warning
-----------------------------------------

=========================================
              ASSET SUMMARY
=========================================
Total Assets : 3
Critical Assets : 1
High Risk Assets : 1
Medium Risk Assets : 1
Vulnerable Assets : 1
=========================================
```

---

## Implementation Notes

- **Data structure:** a *list of dictionaries*. Each asset is a dictionary so
  fields can be accessed by name (`asset["Risk Level"]`) instead of by index,
  and the list preserves insertion order.
- **Validation:** the `choose()` helper displays the valid options and loops
  until the user enters one of them, so an invalid value can never be stored.
- **Uniqueness:** Asset ID acts as the primary key. `add_asset()` rejects an ID
  that already exists, since duplicates would make records unreachable through
  search, update and delete.
- **Search:** performed with a linear scan — O(n) time. Asset IDs are compared
  case-insensitively so `a101` matches `A101`.
- **Persistence:** assets are written to `data/assets.json` with `json.dump()`
  after every change and reloaded with `json.load()` at startup. File reads are
  wrapped in `try/except` so a missing or corrupted file does not crash the
  program.
- **Update behaviour:** pressing Enter at a text field keeps the existing value,
  preventing accidental data loss.

---

## Testing

Twenty test cases covering normal operation, invalid input and edge cases are
documented in [`tests/test_cases.md`](tests/test_cases.md). All 20 pass.

---

## Possible Future Enhancements

*Not part of the problem statement — listed as scope for further work.*

- Validate the IP address format
- Filter or sort assets by risk level or department
- Export the inventory report to CSV or PDF
- Store assets in a database instead of a JSON file
- Add user authentication and an audit log of changes
