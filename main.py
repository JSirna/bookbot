from stats import get_num_words, print_report
import sys

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
	return file_contents

def main():
	if (len(sys.argv) == 2):
		print(f'Found {get_num_words(get_book_text(sys.argv[1]))} total words')
		print_report(get_book_text(sys.argv[1]))
	else:
		print('Usage: python3 main.py <path_to_book>')
		sys.exit(1)

main()
