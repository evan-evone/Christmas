# Christmas
## A GitHub repository for storing Christmas Lists.

This repository was inspired by my family's Christmas List collective, in which we shared
a Google Sheets file and all entered in our Christmas Wishes. However, nerd that I am, my
Christmas list quickly became too complex to simply enter in a Google Sheets cell; I wanted
more complex grouping capabilities in order to make "gift packages" that would contain
multiple gifts under a single link. Thus, I decided to switch to GitHub pages, which would
allow me to create HTML pages for each of these "packages" I had in mind.

### Building

```
$ ./build.sh
```

- Runs of `./index.sh` in every directory.

---

```
$ ./index.sh
```

- Simple, brute-force script to build `index.html` in every necessary directory.
- **Overwrites** `index.html` in each directory.
    - Most resources come from `/Build-Assets/*`---unchanging HTML snippets that must be
      identical for all `index.html` files.
    - Variable content file called `index.body.html`
