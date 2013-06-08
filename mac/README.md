# Pimp yo' Mac

## Spotlight replacements / complements

* [Alfred](http://www.alfredapp.com/)
  Fast, simple. There's lots I don't use, but the stuff I haven't learned yet doesn't bog the UI down or get in my way. Also, Command+Ctrl+C for clipboad history!
* [Quicksilver]
* Google's thing



## Text editors

* [Sublime Text 2](http://www.sublimetext.com/2) and/or [3](http://www.sublimetext.com/3).
  The arguments for Python 2 vs 3 pretty much all apply to this division.
* MacVim



## Command line

* [iTerm2](http://www.iterm2.com/), a.k.a. iTerm.
  Has nice things like tmux integration and lots more customizability than Terminal.app. Not a big change, though.
* [tmux](http://tmux.sourceforge.net/) / [screen](http://www.gnu.org/software/screen/).

## Commands (for Macs)

* `pbcopy` and `pbpaste`
* `open`

Other things that are BSD-specific or work differently on most Linuxes (e.g., `find` vs `find .`).



## Dotfiles & co.

These are the things that go in your home (`~`) directory, and which many command line tools will load automatically.

You really ought to make yourself a dotfiles repo on Github, and fill it with your `.bashrc`'s, `.bash_profile`'s, etc.
But, you shouldn't clone / copy someone else's dotfiles. You should add things to yours as needed.
You should understand every single line of your `.gitconfig`, `.bashrc`, etc.

Some files worth customizing:

    .bash_logout
    .bash_profile
    .bashrc
    .gemrc
    .gitconfig
    .gitignore_global
    .inputrc
    .screenrc
    .tmux.conf
    .vimrc

Much more can be said on these.

### Examples

* [chbrown](https://github.com/chbrown/dotfiles.git)
* [nathanleiby](https://github.com/nathanleiby/dotfiles)
* (add yours here)



## Handy libraries

* json
    - Node.js tool to handle json at the command line

    brew install node
    npm install json



## Other

* Fantastical
* Cobook
* Better touch tool

## Complementary iPhone apps

* Mailbox
* Prompt

# Contributors

Thanks to @nathanleiby for the prompt and categories.
