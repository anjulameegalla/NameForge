# NameForge

This Python script generates common **Active Directory (AD) style usernames** from a list of first and last names. It is useful for **pentesting, user enumeration, and wordlist generation** in enterprise environments.

> [!NOTE]
> Input names should be in the format: ***Firstname*** ***Lastname***. <br>
Lines with missing names are skipped automatically. <br>

---

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

- `u` → Path to the input file containing names (**required**)
- `o` → Path to the output file (**optional**, defaults to **stdout**)

---

## 📄 Example

### Input file (`users.txt`)

```
John Smith
```

### Run command

```bash
python3 NameForge.py -u users.txt -o usernames.txt
```

### Output file (`usernames.txt`)

```
johnsmith
john.smith
john-smith
john_smith
smithjohn
smith.john
smith-john
smith_john
jsmith
j.smith
j-smith
j_smith
sjohn
s.john
s-john
s_john
johsmi
joh.smi
joh-smi
joh_smi
smijoh
smi.joh
smi-joh
smi_joh
js
sj
```

---

### Note:

- Active Directory usernames are not case-sensitive
- Input names should be in the format: `Firstname Lastname`
- Lines with missing names are skipped automatically
- Results are de-duplicated and sorted alphabetically