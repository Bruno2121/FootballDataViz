
#!/usr/bin/env python
import sys

def write2file(page,filepath):
    #print to file
    with open(filepath, 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(page)