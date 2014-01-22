# Lemme Fizz'Em!

The goal of this project was to automatically replace every champion's selection sound with the classic "Lemme At'em" of Fizz. It also works for any other champion's selection sound.

## [Download](https://github.com/scowalt/lemme-fizzem/releases)

### Usage

  - `main.exe Fizz` for the classic "Lemme At'em!"
  - `main.exe DrMundo` for "Mundo goes where he pleases"
  - `main.exe Chamption` for anyone else
  - `main.exe restore` will undo the changes made. **This must be done before switching champions**

#### Example Usage

	main.exe Fizz
	...
	main.exe restore
	...
	main.exe DrMundo

### How to Build

If you don't trust my shady executable and want to build the script yourself, here's how!

  1. Install Python 2.7.x
  2. Install pyinstaller
  3. Run `pyinstaller main.py` in the project directory, with the `--onefile` flag for a single executable

### Changelog

  - **v0.0.1** - Initial release