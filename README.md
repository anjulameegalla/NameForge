# NameForge

```
     __                       ___                                  
  ╱╲ ╲ ╲__ _ _ __ ___   ___  ╱ __╲__  _ __ __ _  ___   _ __  _   _ 
 ╱  ╲╱ ╱ _` │ '_ ` _ ╲ ╱ _ ╲╱ _╲╱ _ ╲│ '__╱ _` │╱ _ ╲ │ '_ ╲│ │ │ │
╱ ╱╲  ╱ (_│ │ │ │ │ │ │  __╱ ╱ │ (_) │ │ │ (_│ │  __╱_│ │_) │ │_│ │
╲_╲ ╲╱ ╲__,_│_│ │_│ │_│╲___╲╱   ╲___╱│_│  ╲__, │╲___(_) .__╱ ╲__, │
                                          │___╱       │_│    │___╱ 

```
This Python script generates common **Active Directory (AD) style usernames** from a list of first and last names. It is useful for **pentesting, user enumeration, and wordlist generation** in enterprise environments.

- Input names should be in the format: ***Firstname*** ***Lastname*** 
- Duplicate names are removed
- Lines with missing names are skipped automatically. 

<br> 

### Prerequisites

- Python 3.6+ (recommended)


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
- On Windows, use `python` if `python3` is not available.


### Arguments

- `-u` → Path to the input file containing names (**required**)
- `-o` → Path to the output file (**optional**, defaults to **stdout**)

<br>

See [**examples/**](examples/) for usage examples.



