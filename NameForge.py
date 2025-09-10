#!/usr/bin/python3


import argparse
import sys

def generate_usernames(firstname: str, lastname: str) -> set:
    usernames = set()   
    separators = ["", ".", "-", "_"]

    for sep in separators:
        usernames.add(f"{firstname}{sep}{lastname}")
        usernames.add(f"{lastname}{sep}{firstname}")

        usernames.add(f"{firstname[0]}{sep}{lastname}")
        usernames.add(f"{lastname[0]}{sep}{firstname}")

        usernames.add(f"{firstname[:3]}{sep}{lastname[:3]}")
        usernames.add(f"{lastname[:3]}{sep}{firstname[:3]}")

    usernames.add(f"{firstname[0]}{lastname[0]}")
    usernames.add(f"{lastname[0]}{firstname[0]}")

    return usernames


def main():
    parser = argparse.ArgumentParser(description="NameForge AD Usernames Generator")
    parser.add_argument("-u", help="UserList Path", required=True)
    parser.add_argument("-o", help="Output Filename (optional, default=stdout)", required=False)
    args = parser.parse_args()

    try:
        with open(args.u, "r") as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"[-] Error: File {args.u} not found.")
        sys.exit(1)

    all_usernames = set()

    for line in lines:
        line = line.strip()
        if len(line.split()) < 2:
            continue

        firstname, lastname = line.split()[:2]
        firstname = firstname.lower()
        lastname = lastname.lower()

        all_usernames.update(generate_usernames(firstname, lastname))


    if args.o:
        with open(args.o, "w") as outfile:
            for username in sorted(all_usernames):
                outfile.write(username + "\n")
        print(f"[+] Usernames generated successfully! Saved to {args.o}")
    else:
        for username in sorted(all_usernames):
            print(username)


if __name__ == "__main__":
    main()
