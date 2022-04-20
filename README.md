# adventuron-tools
Tools to help Adventuron Development

## Image Compression

https://pngquant.org/
To have the strip option on Ubuntu, install from source: 
https://github.com/kornelski/pngquant
(needs git to checkout and Rust's cargo to build).
Then use:
```pngquant --strip *.png --ext '.png' --force```

## Embed data as base64

You need Python3 to run it.
Run it with: 
```./embed path/to/game.txt path/to/game_embedded.txt```

The second argument is optional; if only the source file is specified, it will
append `_embed` to the given filename before saving. If you want to overwrite
the file, pass the same argument twice.

TODO: make it a real CLI tool.
