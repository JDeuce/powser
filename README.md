#Powser#
![I'll make my own package manager with blackjack and hookers](http://i.imgur.com/lWoIzCc.png)

powser is a command line tool for downloading front-end dependencies using the [cdnjs reopsitory](https://cdnjs.com/).

Unlike [bowser](https://github.com/bower/bower/issues/368) this tool will eventually be meant
for production dependency management. It does not attempt to checkout full source trees,
it attempts to only fetch what is required for production.

For now, we defer to the [cdnjs project](https://github.com/cdnjs/cdnjs) to maintain both
the list of projects, and the list of files worth downloading. Additionally, their CDN
endpoints are used to fetch the files.

The goal is that developers can use powser to install packages quickly during development,
but save them in a production quality manner, suitable for tracking the entire powser_components
in a git repository.

The project is still in it's infancy, but I think it works quite well.

#Demo#
[![asciicast](https://asciinema.org/a/4fmiom5wwp3o8rzeoguaths0m.png)](https://asciinema.org/a/4fmiom5wwp3o8rzeoguaths0m)

#How to use#

## Installing powser ##

### Installing from pip ###
```
$ pip install powser
```

### Installing from source ###
```
python setup.py install
```

## Searching for packages ##

```
$ powser search jquery
jquery
jquery.pjax
jquery-mobile
jqueryui
jquery-cookie
jquery.transit
jquery.isotope
jquery-validate
jquery-handsontable
```
{{

## Showing package information ##

```
$ powser show backbone.js

backbone.js
        default: 1.2.3
versions:
+ 1.2.3
        - backbone-min.js
        - backbone-min.map
        - backbone.js
+ 1.2.2
        - backbone-min.js
        - backbone-min.map
        - backbone.js
```

## Installing a package ##

```
$ powser install jquery
Installing jquery version 2.2.0...

Downloading /jquery/2.2.0/jquery.js ... Done.
Downloading /jquery/2.2.0/jquery.min.js ... Done.
Downloading /jquery/2.2.0/jquery.min.map ... Done.

Successfully installed.
$ ls powser_components/jquery/2.2.0/
jquery.js  jquery.min.js  jquery.min.map
```

#Contributing#

Send ideas through github issues.

Send patches through pull requests.
Code should ideally:
  * Follow PEP8
  * Generate no pyflakes warnings


#TODO#

  * Allow specific package versions to be installed
  * Implement automated tests
  * Implement a manifest file (possibly powser.json) to track what's been installed
  * Implement clean, prune, refresh functionality from manifest.
  * Investigate automatic dependency management.
  * Possibility to use other CDNs for initial download.
  * [webassets](https://webassets.readthedocs.org/en/latest/) integration - automatically build compressed packs from downloaded files
    * Possibility to automatically switch between CDN hosted/local assets

#License#

Written by JDeuce
Released under the MIT License: http://www.opensource.org/licenses/mit-license.php
