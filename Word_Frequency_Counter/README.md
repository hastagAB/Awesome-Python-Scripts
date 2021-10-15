# Word Frequency Counter

## Description
A python script that counts word frequencies in a text.

The text is pre-processed beforehand to keep only the most informative words.
Top-10 most frequent words are shown to the user. The full output is saved in a file in the same directory as the input text file.

## Usage

```py
>>> python count_word_freq.py --filepath [filepath]
```

### Example

```py
>>> python count_word_freq.py --filepath test_file.txt
Top 10 most frequent words:
[('queen', 3), ('said', 3), ('fair', 3), ('mirror', 3), ('snow', 2), ('castle', 2), ('father', 2), ('stepmother', 2), ('upon', 1), ('time', 1)]

Saved the word frequencies to 'test_file_freq_dist.txt'
```

```
test_file.txt

Once upon a time, a princess named Snow White lived in a castle with her father, the King, and her stepmother, the Queen.  Her father had always said to his daughter that she must be fair to everyone at court.  Said he, "People come here to the castle when they have a problem.  They need the ruler to make a fair decision.  Nothing is more important than to be fair."

The Queen, Snow White's stepmother, knew how much this meant to her husband. At the first chance, she went to her magic mirror.  "Mirror, mirror, on the wall," said the Queen.  "Who is the fairest of them all?"

```

```
test_file_freq_dist.txt

('queen', 3)
('said', 3)
('fair', 3)
('mirror', 3)
('snow', 2)
('castle', 2)
('father', 2)
('stepmother', 2)
('upon', 1)
('time', 1)
('princess', 1)
('named', 1)
('white', 1)
('lived', 1)
('king', 1)
('always', 1)
('daughter', 1)
('must', 1)
('everyone', 1)
('court', 1)
('people', 1)
('come', 1)
('problem', 1)
('need', 1)
('ruler', 1)
('make', 1)
('decision', 1)
('nothing', 1)
('important', 1)
('whites', 1)
('knew', 1)
('much', 1)
('meant', 1)
('husband', 1)
('first', 1)
('chance', 1)
('went', 1)
('magic', 1)
('wall', 1)
('fairest', 1) 

```