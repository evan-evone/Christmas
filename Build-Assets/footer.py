#!/usr/bin/env python

import os

date_str = os.popen('date "+%d %b %Y"').read().strip()

lines = [
'    <div class="w3-container w3-black w3-center w3-opacity w3-padding-16">',
'      <h1 class="w3-margin w3-xlarge">',
'        &#x1F384; Merry Christmas! &#x1F384;',
'      </h1>',
'      <p>Powered by',
'        <a href="https://www.w3schools.com/w3css/w3css_templates.asp" target="_blank">',
'          Start Page',
'        </a>.<br />',
'        Built on ' + date_str + '.',
'      </p>',
'    </div>',
]

print('\n'.join(lines))
