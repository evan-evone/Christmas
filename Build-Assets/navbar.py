#!/usr/bin/env python

from sys import argv

lines = [
'    <div class="w3-top">',
'      <div class="w3-bar w3-light-green w3-card w3-left-align w3-large">',
'      <a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-padding-large w3-hover-white w3-large w3-light-green" href="javascript:void(0);" onclick="myFunction()" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>',
'      <a href="/" class="w3-bar-item w3-button w3-padding-large w3-hover-white">Home</a>',
'      <a href="/2018" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">2018</a>',
'      <a href="/2019" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">2019</a>',
'      <a href="https://github.com/evan-evone/Christmas" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white w3-right">View on GitHub</a>',
'      </div>',
'',
'      <!-- Navbar on small screens -->',
'      <div id="navDemo" class="w3-bar-block w3-white w3-hide w3-hide-large w3-hide-medium w3-large">',
'      <a href="/2018" class="w3-bar-item w3-button w3-padding-large">2018</a>',
'      <a href="/2019" class="w3-bar-item w3-button w3-padding-large">2019</a>',
'      </div>',
'    </div>',
]

if len(argv) > 1:
    if argv[1] == 'home':
        lines[3] = '      <a href="/" class="w3-bar-item w3-button w3-padding-large w3-white">Home</a>'
        lines[4] = '      <a href="/2018" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">2018</a>'
        lines[5] = '      <a href="/2019" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">2019</a>'
        lines[11] = '      <a href="/2018" class="w3-bar-item w3-button w3-padding-large w3-hover-white">2018</a>'
        lines[12] = '      <a href="/2019" class="w3-bar-item w3-button w3-padding-large w3-hover-white">2019</a>'
    if argv[1] == '2018':
        lines[3] = '      <a href="/" class="w3-bar-item w3-button w3-padding-large w3-hover-white">Home</a>'
        lines[4] = '      <a href="/2018" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-white">2018</a>'
        lines[5] = '      <a href="/2019" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">2019</a>'
        lines[11] = '      <a href="/2018" class="w3-bar-item w3-button w3-padding-large w3-white">2018</a>'
        lines[12] = '      <a href="/2019" class="w3-bar-item w3-button w3-padding-large">2019</a>'
    if argv[1] == '2019':
        lines[3] = '      <a href="/" class="w3-bar-item w3-button w3-padding-large w3-hover-white">Home</a>'
        lines[4] = '      <a href="/2018" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">2018</a>'
        lines[5] = '      <a href="/2018" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-white">2019</a>'
        lines[11] = '      <a href="/2018" class="w3-bar-item w3-button w3-padding-large">2018</a>'
        lines[12] = '      <a href="/2018" class="w3-bar-item w3-button w3-padding-large w3-white">2019</a>'

print('\n'.join(lines))
