#!/usr/bin/env bash

# Script to build home `index.sh`
# NOTE: *Overwrites* `index.html` file.
# Built purely from `Build-Assets/*` and `index.body.html`

echo '' > index.html                                                  # Clear index.html

echo '<!DOCTYPE html>' > index.html                                   # Declare HTML
echo '<html lang="en" dir="ltr">' >> index.html                       # Open html tag
../../Build-Assets/head.py "Ne Obliviscaris Collection" >> index.html # Write header

echo '' >> index.html                                                 # Newline for clarity
echo '  <body>' >> index.html                                         # Open body tag
../../Build-Assets/navbar.py >> index.html                            # Write 2018 navbar
echo '' >> index.html                                                 # Newline for clarity
cat index.body.html >> index.html                                     # Write main content - variable
echo '' >> index.html                                                 # Newline for clarity
../../Build-Assets/footer.py >> index.html                            # Write footer
echo '  </body>' >> index.html                                        # Close body tag
echo '' >> index.html                                                 # Newline for clarity

../../Build-Assets/script.py >> index.html                            # Write navbar
echo '</html>' >> index.html                                          # Close html tag
