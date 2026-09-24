# ================================================
#   CYBERSECURITY ASSET INVENTORY SYSTEM
#   Weekly Mini Project - 01
# ================================================

import json
import os

DATA_FILE = "data/assets.json"

# Allowed values (as given in the problem statement)
ASSET_TYPES = {
    "1": "Workstation",
    "2": "Server",
    "3": "Router",
    "4": "Switch",
    "5": "Application"
}

RISK_LEVELS = {
    "1": "Low",
    "2": "Medium",
    "3": "High",
    "4": "Critical"
}

SECURITY_STATUS = {
    "1": "Secure",
    "2": "Warning",
    "3": "Vulnerable"
}

assets = []


# ---------- Helper functions ----------

def choose(title, options):
    """Show a numbered menu and keep asking until a valid option is picked."""
    print("\n" + title)
    for key in options:
        print(key + ". " + options[key])

    while True:
        choice = input("Enter choice: ").strip()
        if choice in options:
            return options[choice]
        print("Invalid choice. Please enter a number from the list above.")


def ask_text(prompt):
    """Keep asking until the user types something that is not blank."""
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("This field cannot be empty.")


def find_asset(asset_id):
    """Return the asset with this ID, or None if it does not exist."""
    for asset in assets:
        if asset["Asset ID"].lower() == asset_id.lower():
            return asset
    return None


def print_asset(asset):
    """Print one asset in the format shown in the problem statement."""
    print("Asset ID :", asset["Asset ID"])
    print("Asset Name :", asset["Asset Name"])
    print("Asset Type :", asset["Asset Type"])
    print("IP Address :", asset["IP Address"])
    print("OS :", asset["Operating System"])
    print("Department :", asset["Department"])
    print("Risk Level :", asset["Risk Level"])
    print("Status :", asset["Security Status"])


# ---------- File handling ----------

def load_assets():
    """Load saved assets from data/assets.json if the file exists."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except (ValueError, OSError):
            print("Could not read the data file. Starting with an empty inventory.")
    return []


def save_assets():
    """Save the current assets to data/assets.json."""
    try:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w") as f:
            json.dump(assets, f, indent=4)
    except OSError:
        print("Warning: could not save data to file.")


# ---------- Main operations ----------

def add_asset():
    asset_id = ask_text("\nAsset ID: ")

    if find_asset(asset_id) is not None:
        print("\nAn asset with this ID already exists. Asset not added.")
        return

    asset = {}
    asset["Asset ID"] = asset_id
    asset["Asset Name"] = ask_text("Asset Name: ")
    asset["Asset Type"] = choose("Asset Types:", ASSET_TYPES)
    asset["IP Address"] = ask_text("IP Address: ")
    asset["Operating System"] = ask_text("Operating System: ")
    asset["Department"] = ask_text("Owner/Department: ")
    asset["Risk Level"] = choose("Risk Levels:", RISK_LEVELS)
    asset["Security Status"] = choose("Security Status:", SECURITY_STATUS)

    assets.append(asset)
    save_assets()

    print("\nAsset added successfully!")


def search_asset():
    asset_id = ask_text("\nEnter Asset ID to search: ")
    asset = find_asset(asset_id)

    if asset is None:
        print("\nAsset not found.")
        return

    print("\nAsset Found!")
    print_asset(asset)


def update_asset():
    asset_id = ask_text("\nEnter Asset ID to update: ")
    asset = find_asset(asset_id)

    if asset is None:
        print("\nAsset not found.")
        return

    print("\nEnter new details (press Enter to keep the old value):")

    name = input("Asset Name [" + asset["Asset Name"] + "]: ").strip()
    if name != "":
        asset["Asset Name"] = name

    ip = input("IP Address [" + asset["IP Address"] + "]: ").strip()
    if ip != "":
        asset["IP Address"] = ip

    os_name = input("Operating System [" + asset["Operating System"] + "]: ").strip()
    if os_name != "":
        asset["Operating System"] = os_name

    dept = input("Department [" + asset["Department"] + "]: ").strip()
    if dept != "":
        asset["Department"] = dept

    asset["Asset Type"] = choose("Asset Types:", ASSET_TYPES)
    asset["Risk Level"] = choose("Risk Levels:", RISK_LEVELS)
    asset["Security Status"] = choose("Security Status:", SECURITY_STATUS)

    save_assets()
    print("\nAsset updated successfully!")


def delete_asset():
    asset_id = ask_text("\nEnter Asset ID to delete: ")
    asset = find_asset(asset_id)

    if asset is None:
        print("\nAsset not found.")
        return

    assets.remove(asset)
    save_assets()
    print("\nAsset deleted successfully!")


def display_assets():
    if len(assets) == 0:
        print("\nNo assets available.")
        return

    print("\n=========================================")
    print("       CYBERSECURITY ASSET INVENTORY")
    print("=========================================")

    for asset in assets:
        print_asset(asset)
        print("-----------------------------------------")


def display_summary():
    total = len(assets)
    critical = 0
    high = 0
    medium = 0
    vulnerable = 0

    for asset in assets:
        if asset["Risk Level"] == "Critical":
            critical += 1
        elif asset["Risk Level"] == "High":
            high += 1
        elif asset["Risk Level"] == "Medium":
            medium += 1

        if asset["Security Status"] == "Vulnerable":
            vulnerable += 1

    print("\n=========================================")
    print("              ASSET SUMMARY")
    print("=========================================")
    print("Total Assets :", total)
    print("Critical Assets :", critical)
    print("High Risk Assets :", high)
    print("Medium Risk Assets :", medium)
    print("Vulnerable Assets :", vulnerable)
    print("=========================================")


# ---------- Main program ----------

assets = load_assets()

while True:

    print("\n========== CYBERSECURITY ASSET INVENTORY ==========")
    print("1. Add Asset")
    print("2. Search Asset")
    print("3. Update Asset")
    print("4. Delete Asset")
    print("5. Display All Assets")
    print("6. Display Summary")
    print("7. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        add_asset()

    elif choice == "2":
        search_asset()

    elif choice == "3":
        update_asset()

    elif choice == "4":
        delete_asset()

    elif choice == "5":
        display_assets()

    elif choice == "6":
        display_summary()

    elif choice == "7":
        print("\nThank you!")
        break

    else:
        print("\nInvalid choice. Try again.")
