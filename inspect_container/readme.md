# Docker inspect container file printout

Description:
    Creates a file containing the inspect data of a particular container.

Why:
    For some reason powershell doesn't return the complete JSON printout. 
    CMD works.

## Usage:

```
python ic.py -n container_name
```

Requirements:
A python interpreter 3.6 or above is required due to this script's reliance on 
f - strings.