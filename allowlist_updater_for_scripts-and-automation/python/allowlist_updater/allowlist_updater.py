#!/usr/bin/env python3
import argparse
from pathlib import Path
from typing import List, Optional


def update_allowlist(import_file: str, remove_list: List[str], output_file: Optional[str] = None) -> str:
    '''
    Read IPs from import_file, remove any that appear in remove_list, and write the result
    back to output_file (or overwrite import_file if output_file is None).

    Returns the updated content as a newline-separated string.
    '''
    path = Path(import_file)

    # Read the file content and split on ANY whitespace (spaces/newlines/tabs)
    ip_addresses = path.read_text(encoding="utf-8", errors="ignore").split()

    # IMPORTANT: avoid removing items while iterating (can skip entries).
    remove_set = set(remove_list)
    updated = [ip for ip in ip_addresses if ip not in remove_set]

    # Write back (newline-separated is more readable than space-separated)
    new_content = "\n".join(updated) + ("\n" if updated else "")
    target = Path(output_file) if output_file else path
    target.write_text(new_content, encoding="utf-8")

    return new_content


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Update an allowlist file by removing specified IP addresses.")
    p.add_argument("--input", default="allow_list.txt", help="Path to the allowlist file (default: allow_list.txt).")
    p.add_argument(
        "--remove",
        action="append",
        default=[],
        help="IP address to remove (repeat this flag to remove multiple IPs).",
    )
    p.add_argument("--output", default=None, help="Optional output file. If omitted, updates in-place.")
    p.add_argument("--demo", action="store_true", help="Create a small demo allow_list.txt and run an example update.")
    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.demo:
        demo_path = Path(args.input)
        if not demo_path.exists():
            demo_path.write_text(
                "192.168.25.60\n192.168.1.10\n192.168.140.81\n10.0.0.5\n192.168.203.198\n",
                encoding="utf-8",
            )
        # If user didn't pass --remove, use the example list from the lab.
        if not args.remove:
            args.remove = ["192.168.25.60", "192.168.140.81", "192.168.203.198"]

    if not args.remove:
        parser.error("Nothing to remove. Provide at least one --remove IP or use --demo.")

    updated = update_allowlist(args.input, args.remove, args.output)
    print(updated, end="")


if __name__ == "__main__":
    main()
