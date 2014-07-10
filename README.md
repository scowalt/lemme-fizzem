# Lemme Fizz'Em!

The goal of this project was to automatically replace every champion's selection sound with the classic "Lemme At'em" of Fizz. It also works for any other champion's selection sound.

## [Download](https://github.com/scowalt/lemme-fizzem/releases)

### Usage

  - `fizzem.exe Fizz` for the classic "Lemme At'em!"
  - `fizzem.exe DrMundo` for "Mundo goes where he pleases"
  - `fizzem.exe Champion` for anyone else
  - `fizzem.exe restore` will undo the changes made. **This must be done before switching champions**

#### Example Usage

	fizzem.exe Fizz
	...
	fizzem.exe restore
	...
	fizzem.exe DrMundo

### How to Build

If you don't trust my shady executable and want to build the script yourself, here's how!

  1. Install Python 2.7.x
  2. Install pyinstaller
  3. Run `pyinstaller main.py` in the project directory, with the `--onefile` flag for a single executable

Of course, instead of building / using an executable, you could always just run the script directly

  1. Install Python 2.7.x
  2. Run `python main.py Fizz`

### Changelog

  - **v0.0.1** - Initial release
