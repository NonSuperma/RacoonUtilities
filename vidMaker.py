import subprocess as sp
from Racoon import RacoonMediaTools as Ru
from Racoon import RacoonErrors as RuE


if __name__ == "__main__":
	imageInputPath = Ru.winFilePath("Album cover")
	soundInputPaths = Ru.winFilesPath("Audio files")
	outputPath = None
	try:
		vid = Ru(imageInputPath, soundInputPaths)
		vid.makeVideo(outputPath)
#		for path in soundInputPaths:
#			sp.run(f'del "{path}"', shell=True)
#		sp.run(f'del "{imageInputPath}"', shell=True)

	except RuE.RacoonUtilitiesMissingInputError:
		print("No input!")
		askExit()
	exit()
