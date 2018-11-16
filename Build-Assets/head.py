#!/usr/bin/env python

from sys import argv

lines = [
'  <head>',
'    <meta charset="utf-8">',
'    <title>Christmas List - Evan Keeton</title>',
'    <link rel="icon" href="/Images/Christmas-Gift.png" type="text/png">',
'  ',
'    <meta name="viewport" content="width=device-width, initial-scale=1">',
'    <link rel="stylesheet" href="/CSS/w3.css">',
'    <link rel="stylesheet" href="/CSS/Google-Lato.css">',
'    <link rel="stylesheet" href="/CSS/Google-Montserrat.css">',
'    <link rel="stylesheet" href="/CSS/CDNJS-Font-Awesome.css">',
'    <style>',
'      body,h1,h2,h3,h4,h5,h6 {font-family: "Lato", sans-serif}',
'      .w3-bar,h1,button {font-family: "Montserrat", sans-serif}',
'      .fa-anchor,.fa-coffee {font-size:200px}',
'    </style>',
'  </head>'
]

if len(argv) > 1:
    lines[2] = '    <title>{text}</title>'.format(text=argv[1])

print('\n'.join(lines))
