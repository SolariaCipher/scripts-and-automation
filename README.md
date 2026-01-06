# Allowlist updater (Python)

A small utility that updates an allowlist of IP addresses stored in a text file by removing IPs that should no longer have access.

This comes from a common security-operations task: maintaining allowlists/denylists for restricted services or content.

## What it does
- Reads IPs from a file (whitespace-separated: spaces/newlines/tabs)
- Removes any IP present in a provided remove list
- Writes the updated allowlist back to disk (in-place by default)

## Usage

### 1) Quick demo (creates/updates an example file)
```bash
python allowlist_updater.py --demo
```

### 2) Update a real file in-place
```bash
python allowlist_updater.py --input allow_list.txt --remove 192.168.25.60 --remove 192.168.140.81 --remove 192.168.203.198
```

### 3) Write to a new output file (no overwrite)
```bash
python allowlist_updater.py --input allow_list.txt --output allow_list_updated.txt --remove 192.168.25.60
```

## Notes
- This is an educational mini-project for legal lab environments.
- No secrets, no real-world targeting.
