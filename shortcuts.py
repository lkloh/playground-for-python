import unittest


def join_words_to_sentence_shortcut(words):
	return (' '.join(words) + '.') if words else ''

def join_words_to_sentence_primitive(words):
	if words:
		s = ''
		for i, word in enumerate(words):
			s += (word + '.') if (i == len(words)-1) else (word + ' ')
		return s
	else:
		return ''


class TestJoin(unittest.TestCase):
	def setUp(self):
		self.join_sentence_func = lambda *args: None

	def test_one_word_sentence(self):
		self.assertEqual('No.', self.join_sentence_func(['No']))

	def test_empty_sentence(self):
		self.assertEqual('', self.join_sentence_func([]))

	def test_short_sentence(self):
		words = ['Hello', 'world']
		self.assertEqual('Hello world.', self.join_sentence_func(words))

	def test_long_sentence(self):
		words = ['I', 'am', 'a', 'person', 'who', 'loves', 'long', 'words']
		self.assertEqual('I am a person who loves long words.', self.join_sentence_func(words))


class TestJoinPrimitive(TestJoin):
	def setUp(self):
		self.join_sentence_func = join_words_to_sentence_primitive


class TestJoinShortcut(TestJoin):
	def setUp(self):
		self.join_sentence_func = join_words_to_sentence_shortcut


if __name__ == '__main__':
	#unittest.main()
	suite_primitive = unittest.TestLoader().loadTestsFromTestCase(TestJoinPrimitive)
	suite_shortcut = unittest.TestLoader().loadTestsFromTestCase(TestJoinShortcut)
	all_tests = unittest.TestSuite([suite_primitive, suite_shortcut])
	unittest.TextTestRunner(verbosity=2).run(all_tests)

