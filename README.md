# Simple file merging utility
Helps to merge disparate but similar file trees into a single source of truth. The motivation for this utility
was the download ("takeout") of data from Google Drive. Google chunks the downloads into configurable-sized ZIP
files, so the user winds up with a bunch of roughly equal-sized chunks of their data. Each chunk is mapped to the
root of the user's Drive, and there are no guarantees made about how files are distributed between the chunks. 

So, for example, a user with a file tree that looks like the following could end up with File 1 and File 2 in
two separate chunks:
```
Drive
 | Documents
 |   | File 1
 |   | File 2
 | File 3
```

In this scenario, the user would likely want to reintegrate the file tree into one source of truth.

## Usage
The utility `merger.py` is designed to be run from the same directory as all of the unzipped chunks/downloads
from Google Drive. It will then move all the files from the component folders into a single "golden" file tree.

```bash
$ python3 merger.py
```

This command will take all folders with the prefix "Takeout" (the default for
[Google Takeout](https://takeout.google.com/)) in the current directory, and integrate their contents into one
or more folders in the current directory (likely called "Drive"), depending on their contents.

The utility accepts some optional command line arguments:

```bash
$ python3 merger.py -h
usage: merger.py [-h] [-r ROOT] [-p PREFIX] [-i IGNORE] [-o OUTPUT] [-d]

Drive Merger

options:
  -h, --help                  show this help message and exit
  -r ROOT, --root ROOT        Set input directory root relative to CWD (default: CWD)
  -p PREFIX, --prefix PREFIX  Set directory prefix to search for (default: Takeout)
  -i IGNORE, --ignore IGNORE  Set directory ignore keyword (default: done)
  -o OUTPUT, --output OUTPUT  Set output directory root (default: CWD)
  -d, --dryrun                Whether changes should not take effect (default: false)
                                Will simply print folders to parse if enabled
```

## Questions
Please [reach out](mailto:ezraeinhorn624@gmail.com) to
[me](https://linkedin.com/in/ezraeinhorn) directly with any questions,
comments, or concerns.

### Licensing Disclaimer
<p xmlns:dct="http://purl.org/dc/terms/" xmlns:vcard="http://www.w3.org/2001/vcard-rdf/3.0#">
  <a rel="license"
     href="http://creativecommons.org/publicdomain/zero/1.0/">
    <img src="https://licensebuttons.net/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
  </a>
  <br />
  To the extent possible under law,
  <a rel="dct:publisher"
     href="https://github.com/ezraeinhorn624/sqs">
    <span property="dct:title">I</span></a>
  have waived all copyright and related or neighboring rights to
  <span property="dct:title">file-tree-merger</span>.
This work is published from:
<span property="vcard:Country" datatype="dct:ISO3166"
      content="US" about="https://github.com/ezraeinhorn624/file-tree-merger">
  United States</span>.
</p>
