# Bibbja

Read the Word of God from your terminal — Aqra l-Kelma tal-Mulej mit-terminal tiegħek.

Forked from [lukesmithxyz/kjv](https://github.com/lukesmithxyz/kjv) but with the source text replaced by with [the Maltese Catholic bible](https://malti.global.bible/).


## Usage

    usage: ./bibbja [flags] [reference...]

      -l      list books
      -W      no line wrap
      -h      show help

      Reference types:
          <Book>
              Individual book
          <Book>:<Chapter>
              Individual chapter of a book
          <Book>:<Chapter>:<Verse>[,<Verse>]...
              Individual verse(s) of a specific chapter of a book
          <Book>:<Chapter>-<Chapter>
              Range of chapters in a book
          <Book>:<Chapter>:<Verse>-<Verse>
              Range of verses in a book chapter
          <Book>:<Chapter>:<Verse>-<Chapter>:<Verse>
              Range of chapters and verses in a book

          /<Search>
              All verses that match a pattern
          <Book>/<Search>
              All verses in a book that match a pattern
          <Book>:<Chapter>/<Search>
              All verses in a chapter of a book that match a pattern

## Build

bibbja can be built by cloning the repository and then running make:

    git clone https://github.com/drmenguin/bibbja.git
    cd bibbja
    sudo make install

## License

Public domain
