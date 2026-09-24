# Test Cases — Cybersecurity Asset Inventory System

**Project:** Weekly Mini Project 01
**File under test:** `src/asset_inventory.py`
**Python version:** 3.12
**Test method:** Manual black-box testing through the menu interface

---

## Test Data Used

The three assets from the problem statement are used throughout:

| Asset ID | Asset Name | Asset Type | IP Address | OS | Department | Risk Level | Security Status |
|---|---|---|---|---|---|---|---|
| A101 | HR-PC-01 | Workstation | 192.168.1.10 | Windows 11 | HR | Medium | Secure |
| A102 | Web-Server | Server | 192.168.1.20 | Ubuntu | IT | Critical | Vulnerable |
| A103 | Core-Router | Router | 192.168.1.1 | Cisco IOS | Network | High | Warning |

---

## A. Positive Test Cases

### TC-01 — Add a valid asset
| | |
|---|---|
| **Objective** | Verify a new asset is added with all 8 fields |
| **Input** | Menu `1`, then A101 / HR-PC-01 / type `1` / 192.168.1.10 / Windows 11 / HR / risk `2` / status `1` |
| **Expected** | `Asset added successfully!` and the asset appears in the inventory |
| **Actual** | `Asset added successfully!` — asset stored correctly |
| **Result** | **PASS** |

### TC-02 — Display all assets
| | |
|---|---|
| **Objective** | Verify the display format matches the expected output |
| **Input** | Menu `5` after adding A101, A102, A103 |
| **Expected** | Header banner, all 3 assets with fields labelled `Asset ID :`, `OS :`, `Status :` etc., separated by `-----` lines |
| **Actual** | Output matched the problem statement exactly, character for character |
| **Result** | **PASS** |

### TC-03 — Search an existing asset
| | |
|---|---|
| **Objective** | Verify search retrieves the correct record |
| **Input** | Menu `2`, then `A102` |
| **Expected** | `Asset Found!` followed by the Web-Server details |
| **Actual** | `Asset Found!` — Web-Server / Server / 192.168.1.20 / Ubuntu / IT / Critical / Vulnerable |
| **Result** | **PASS** |

### TC-04 — Update an existing asset
| | |
|---|---|
| **Objective** | Verify selected fields can be changed |
| **Input** | Menu `3`, `A101`, new IP `192.168.1.99`, type `1`, risk `3`, status `2` |
| **Expected** | `Asset updated successfully!`; IP becomes 192.168.1.99 and Risk becomes High |
| **Actual** | IP Address = 192.168.1.99, Risk Level = High, Status = Warning |
| **Result** | **PASS** |

### TC-05 — Delete an existing asset
| | |
|---|---|
| **Objective** | Verify an asset is removed from the inventory |
| **Input** | Menu `4`, then `A103` |
| **Expected** | `Asset deleted successfully!`; total drops from 3 to 2 |
| **Actual** | Deleted; summary showed Total Assets : 2, High Risk Assets : 0 |
| **Result** | **PASS** |

### TC-06 — Security summary counts
| | |
|---|---|
| **Objective** | Verify the summary counts match the expected output |
| **Input** | Menu `6` with all 3 assets present |
| **Expected** | Total 3, Critical 1, High 1, Medium 1, Vulnerable 1 |
| **Actual** | Total Assets : 3, Critical Assets : 1, High Risk Assets : 1, Medium Risk Assets : 1, Vulnerable Assets : 1 |
| **Result** | **PASS** |

### TC-07 — Summary recalculates after update
| | |
|---|---|
| **Objective** | Verify counts are not stale after a record changes |
| **Input** | Change A101 from Medium to High, then menu `6` |
| **Expected** | Medium count decreases by 1, High count increases by 1 |
| **Actual** | Medium Risk Assets : 0, High Risk Assets : 1 |
| **Result** | **PASS** |

### TC-08 — Data persists after restart
| | |
|---|---|
| **Objective** | Verify assets are saved to `data/assets.json` and reloaded |
| **Input** | Add 3 assets, choose `7` to exit, restart the program, choose `6` |
| **Expected** | Summary still shows Total Assets : 3 |
| **Actual** | `data/assets.json` created with 3 records; summary showed Total Assets : 3 after restart |
| **Result** | **PASS** |

---

## B. Negative / Validation Test Cases

### TC-09 — Invalid Asset Type rejected
| | |
|---|---|
| **Objective** | Verify only the 5 allowed asset types can be stored |
| **Input** | At the Asset Type prompt, enter `9` |
| **Expected** | Error message and re-prompt; `9` is not accepted |
| **Actual** | `Invalid choice. Please enter a number from the list above.` then re-prompted |
| **Result** | **PASS** |

### TC-10 — Invalid Risk Level rejected
| | |
|---|---|
| **Objective** | Verify only Low / Medium / High / Critical can be stored |
| **Input** | At the Risk Level prompt, enter `0` |
| **Expected** | Error message and re-prompt |
| **Actual** | Rejected and re-prompted until a valid option was entered |
| **Result** | **PASS** |

### TC-11 — Invalid Security Status rejected
| | |
|---|---|
| **Objective** | Verify only Secure / Warning / Vulnerable can be stored |
| **Input** | At the Security Status prompt, enter `abc` |
| **Expected** | Error message and re-prompt |
| **Actual** | Rejected and re-prompted |
| **Result** | **PASS** |

### TC-12 — Duplicate Asset ID rejected
| | |
|---|---|
| **Objective** | Verify Asset ID stays unique |
| **Input** | Add A101, then try to add A101 again |
| **Expected** | The second asset is not added |
| **Actual** | `An asset with this ID already exists. Asset not added.` |
| **Result** | **PASS** |

### TC-13 — Blank required field rejected
| | |
|---|---|
| **Objective** | Verify empty input is not stored |
| **Input** | Press Enter at the Asset ID prompt |
| **Expected** | Error message and re-prompt |
| **Actual** | `This field cannot be empty.` then re-prompted |
| **Result** | **PASS** |

### TC-14 — Search for a non-existent asset
| | |
|---|---|
| **Objective** | Verify a clean message instead of a crash |
| **Input** | Menu `2`, then `A999` |
| **Expected** | `Asset not found.` |
| **Actual** | `Asset not found.` — no exception raised |
| **Result** | **PASS** |

### TC-15 — Delete a non-existent asset
| | |
|---|---|
| **Objective** | Verify a clean message instead of a crash |
| **Input** | Menu `4`, then `A999` |
| **Expected** | `Asset not found.` |
| **Actual** | `Asset not found.` |
| **Result** | **PASS** |

### TC-16 — Invalid menu choice
| | |
|---|---|
| **Objective** | Verify the main menu handles bad input |
| **Input** | Enter `99` at the main menu |
| **Expected** | `Invalid choice. Try again.` and the menu is shown again |
| **Actual** | `Invalid choice. Try again.` — loop continued normally |
| **Result** | **PASS** |

---

## C. Edge Cases

### TC-17 — Display with an empty inventory
| | |
|---|---|
| **Objective** | Verify no crash when no assets exist |
| **Input** | Menu `5` before adding anything |
| **Expected** | `No assets available.` |
| **Actual** | `No assets available.` |
| **Result** | **PASS** |

### TC-18 — Summary with an empty inventory
| | |
|---|---|
| **Objective** | Verify all counts show 0, not an error |
| **Input** | Menu `6` before adding anything |
| **Expected** | Total 0, Critical 0, High 0, Medium 0, Vulnerable 0 |
| **Actual** | All counts displayed as 0 |
| **Result** | **PASS** |

### TC-19 — Case-insensitive Asset ID lookup
| | |
|---|---|
| **Objective** | Verify `a101` finds the asset stored as `A101` |
| **Input** | Menu `3`, then `a101` |
| **Expected** | The asset is found and can be updated |
| **Actual** | Asset located and updated successfully |
| **Result** | **PASS** |

### TC-20 — Blank input during update keeps the old value
| | |
|---|---|
| **Objective** | Verify pressing Enter does not wipe a field |
| **Input** | Update A101, press Enter at Asset Name, OS and Department |
| **Expected** | Those three fields keep their original values |
| **Actual** | Asset Name remained HR-PC-01, OS remained Windows 11, Department remained HR |
| **Result** | **PASS** |

---

## Summary

| Category | Cases | Passed | Failed |
|---|---|---|---|
| Positive | 8 | 8 | 0 |
| Negative / Validation | 8 | 8 | 0 |
| Edge Cases | 4 | 4 | 0 |
| **Total** | **20** | **20** | **0** |

No syntax errors, runtime exceptions or crashes were observed during testing.
