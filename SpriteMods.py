from PIL import Image
import os
import sys


def flipSprite(path='.', extension='.png'):
	for imgs in os.listdir(path):
		if imgs.endswith(extension):
			try:
				with Image.open(imgs) as i:
					fname, fext = os.path.splitext(imgs)
					flipped = i.transpose(Image.FLIP_LEFT_RIGHT)
					flipped.save(f'Modified\ {fname}_Left{fext}')
			except OSError:
				pass


def makeDirectory(path):
	try:
		if os.path.basename(path) != 'Modified':
			os.mkdir(os.path.join(path, 'Modified'))
	except OSError as error:
		print(error)



def flipSpriteTree(path='.', extension='.png'):
	os.chdir(path)
	abspath = os.getcwd()
	for paths, names, files in os.walk(abspath):
		if os.path.basename(paths) != 'Modified':
			for file in files:
				if file.endswith(extension):
					makeDirectory(paths)
					try:
						with Image.open(os.path.join(paths, file)) as i:
							fname, fext = os.path.splitext(file)
							flipped = i.transpose(Image.FLIP_LEFT_RIGHT)
							flipped.save(f'{paths}\Modified\ {fname}_Left{fext}')
					except OSError as error:
						print(error)


def resizeSprite():
	pass


if __name__ == '__main__':
	# try:
	# 	os.mkdir('Modified')
	# except OSError:
	# 	pass
	pass




