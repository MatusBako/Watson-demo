#!/usr/bin/python3
import sys
from os.path import realpath
from watson_developer_cloud import SpeechToTextV1

class NumberMapper:
	map = {
		'plus':'+',
		'oh':'0',
		'zero':'0',
		'one':'1',
		'two':'2',
		'three':'3',
		'four':'4',
		'five':'5',
		'six':'6',
		'seven':'7',
		'eight':'8',
		'nine':'9'
	}


	@classmethod
	def map_numbers(cls, words):
		out = []
		for word in words.split(" "):
			try:
				if word != '%HESITATION':
					out.append(cls.map[word]) 
			except KeyError as e:
				out.append(word)
		return " ".join(out)


def get_input_file():
	if len(sys.argv) > 2:
		raise Exception("Only one argument is allowed.")
	elif len(sys.argv) == 2:
		return realpath(sys.argv[1])
	
	print("Enter input file in .mp3 format as first argument.")
	exit(1)


def main():
	input_file = get_input_file()

	speech_to_text = SpeechToTextV1(
		username='0fa6dead-1f66-4673-a878-ba4c97b4e54e',
		password='j13XC5liAqUQ',
		x_watson_learning_opt_out=False
	)

	with open(input_file,'rb') as audio_file:
		response = speech_to_text.recognize(
			audio_file, content_type='audio/mpeg', timestamps=True,
			word_confidence=True)

		words = response["results"][0]["alternatives"][0]["transcript"]
		print(NumberMapper.map_numbers(words))


if __name__ == '__main__':
	main()