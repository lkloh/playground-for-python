#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def example_unicode_encode_error():
	file = open('unicode_demo.txt', 'w')

	unicode_str = u'Δ, Й, ק, ‎ م, ๗, あ, 叶, 葉, and 말.'
	print 'type: %s' % type(unicode_str)

	file.write(unicode_str)

	file.close()

def why_unicode_encode_errors_are_hard_to_catch():
	file = open('unicode_demo.txt', 'w')

	unicode_str = u'Hello world'
	print 'type: %s' % type(unicode_str)

	file.write(unicode_str)

	file.close()

def example_unicode_encode_correct():
	file = open('unicode_demo.txt', 'w')

	unicode_str = u'Δ, Й, ק, ‎ م, ๗, あ, 叶, 葉, and 말.'
	print 'type: %s' % type(unicode_str)

	ascii_str = unicode_str.encode("utf-8")

	file.write(ascii_str)

	file.close()

if __name__ == '__main__':
	example_unicode_encode_correct()
	why_unicode_encode_errors_are_hard_to_catch()
	example_unicode_encode_error()