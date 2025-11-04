# NameForge

This Python script generates common **Active Directory (AD) style usernames** from a list of first and last names. It is useful for **pentesting, user enumeration, and wordlist generation** in enterprise environments.

- Input names should be in the format: ***Firstname*** ***Lastname***. 
- Lines with missing names are skipped automatically. <br> 

<br>

## Installation

Clone the repository:

```bash
git clone https://github.com/anjulameegalla/NameForge.git
cd NameForge
```

## Usage

```bash
python3 NameForge.py -u <input_file> [-o <output_file>]
```

### Arguments

- `-u` → Path to the input file containing names (**required**)
- `-o` → Path to the output file (**optional**, defaults to **stdout**)

<br>

### Contributing

Bugs and suggestions are welcome on [Issues](https://github.com/anjulameegalla/NameForge/issues)!  

[![Contact](https://img.shields.io/badge/Contact-2ea44f?style=for-the-badge)](https://anjula.live/)