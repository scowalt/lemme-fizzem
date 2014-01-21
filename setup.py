from cx_Freeze import setup, Executable

setup(
	name = "Lemme Fizz'em",
	version = "0.0.1",
	description = "More Fizz in your LoL",
	executables=[Executable("main.py")]
)