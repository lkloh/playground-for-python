'''
Given a string and a set of characters,
find the smallest substring containing all the characters.
Return empty string if not found.

String: 'abbbcca'
Alphabet: ['a', 'b', 'c']
Output: 'bcca'

String: 'aaaaabbbbbbcccccabcaaaaabbbbbbcccc'
Alphabet: ['a', 'b', 'c']
Output: 'abc'

String: 'abbbbbcccccffff'
Alphabet: ['a', 'b', 'c', 'f']
Output: ''
'''

def contains_all_alphabets(char_counts):
	for ch in char_counts:
		if char_counts[ch] == 0:
			return False
	return True


def get_shortest_substr(s, alphabet):
	char_counts = {}
	for ch in alphabet:
		char_counts[ch] = 0

	start = 0
	end = 0
	min_start = 0
	min_end = 0
	min_str_len = len(s) + 1
	while start <= end and end < len(s):
		end_ch = s[end]
		char_counts[end_ch] += 1
		if contains_all_alphabets(char_counts):
			# try to do better by incrementing start index
			if end - start + 1 < min_str_len:
				min_str_len = end - start + 1
				min_start = start
				min_end = end

			start_ch = s[start]
			if char_counts[start_ch] >= 2:
				char_counts[start_ch] -= 1
				start += 1
			else:
				end += 1
		else:
			end += 1

	return s[min_start:min_end+1] if min_str_len <= len(s) else ''




def get_shortest_substring(s, alphabet):
	char_counts = {}
	for ch in alphabet:
		char_counts[ch] = 0

	start = 0
	end = 0
	min_start = -1
	min_end = -1
	min_str_len = len(s) + 1 # impossibly large number
	while start <= end and start < len(s) and end < len(s):
		if contains_all_alphabets(char_counts): # substr contains all chars in alphabet
			# update min
			if end - start + 1 < min_str_len:
				min_str_len = end - start + 1
				min_start = start
				min_end = end
				# try to do better and shrink substr head by one char
				start_ch = s[start]
				if char_counts[start_ch] >= 2:
					char_counts[start_ch] -= 1
					start += 1
			else:
				end_ch = s[end]
				char_counts[end_ch] += 1
				end += 1
		else:
			# increment back pointer, lengthen substr
			end_ch = s[end]
			char_counts[end_ch] += 1
			end += 1

	return s[min_start:min_end] if min_str_len <= len(s) else ''

print get_shortest_substr('abbbcca', set(['a','b','c']))
print get_shortest_substr('abc', set(['a','b','c']))

