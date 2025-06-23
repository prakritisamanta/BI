# Regular Expressions

## Regexes in Python and Their Uses

Imagine you have a string object s. Now suppose you need to write Python code to find out whether s contains the substring '123'. There are at least a couple ways to do this. 

```python
s = 'foo123bar'
'123' in s
# True

s = 'foo123bar'
s.find('123')
# 3

s.index('123')
# 3
```

In these examples, the matching is done by a straightforward character-by-character comparison. That will get the job done in many cases. But sometimes, the problem is more complicated than that.

For example, rather than searching for a fixed substring like '123', suppose you wanted to determine whether a string contains any three consecutive decimal digit characters, as in the strings 'foo123bar', 'foo456bar', '234baz', and 'qux678'.

Strict character comparisons won’t cut it here. This is where regexes in Python come to the rescue.


## First Regex Example

```python
import re
s = 'foo123bar'
re.search('123', s)
# <_sre.SRE_Match object; span=(3, 6), match='123'>

if re.search('123', s):
    print('Found a match.')
else:
    print('No match.')

# Found a match.
```
<br><br>


## Python Regex Metacharacters

The real power of regex matching in Python emerges when <regex> contains special characters called metacharacters. These have a unique meaning to the regex matching engine and vastly enhance the capability of the search.

Consider again the problem of how to determine whether a string contains any three consecutive decimal digit characters.

```python
>>> s = 'foo123bar'
>>> re.search('[0-9][0-9][0-9]', s)
<_sre.SRE_Match object; span=(3, 6), match='123'>

>>> re.search('[0-9][0-9][0-9]', 'foo456bar')
<_sre.SRE_Match object; span=(3, 6), match='456'>

>>> re.search('[0-9][0-9][0-9]', '234baz')
<_sre.SRE_Match object; span=(0, 3), match='234'>

>>> re.search('[0-9][0-9][0-9]', 'qux678')
<_sre.SRE_Match object; span=(3, 6), match='678'>

>>> print(re.search('[0-9][0-9][0-9]', '12foo34'))
None

>>> s = 'foo123bar'
>>> re.search('1.3', s)
<_sre.SRE_Match object; span=(3, 6), match='123'>

>>> s = 'foo13bar'
>>> print(re.search('1.3', s))
None
```

In the first example, the regex 1.3 matches '123' because the '1' and '3' match literally, and the . matches the '2'. 

 
## Metacharacters 

Metacharacters are characters with a special meaning

```python
Character(s)	Meaning
.	Matches any single character except newline
^	∙ Anchors a match at the start of a string
∙ Complements a character class
$	Anchors a match at the end of a string
*	Matches zero or more repetitions
+	Matches one or more repetitions
?	∙ Matches zero or one repetition
∙ Specifies the non-greedy versions of *, +, and ?
∙ Introduces a lookahead or lookbehind assertion
∙ Creates a named group
{}	Matches an explicitly specified number of repetitions
\	∙ Escapes a metacharacter of its special meaning
∙ Introduces a special character class
∙ Introduces a grouping backreference
[]	Specifies a character class
|	Designates alternation
()	Creates a group
:
#
=
!	Designate a specialized group
<>	Creates a named group
```

## Special Sequences

A special sequence is a \ followed by one of the characters in the list below, and has a special meaning.

```python
Character	Description
\A	Returns a match if the specified characters are at the beginning of the string
\b	Returns a match where the specified characters are at the beginning or at the end of a word
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
\d	Returns a match where the string contains digits (numbers from 0-9)
\D	Returns a match where the string DOES NOT contain digits
\s	Returns a match where the string contains a white space character
\S	Returns a match where the string DOES NOT contain a white space character
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
\W	Returns a match where the string DOES NOT contain any word characters
\Z	Returns a match if the specified characters are at the end of the string
```
<br>


## Metacharacters That Match a Single Character

### [] - Specifies a specific set of characters to match

```python
>>> re.search('ba[artz]', 'foobarqux')
<_sre.SRE_Match object; span=(3, 6), match='bar'>
>>> re.search('ba[artz]', 'foobazqux')
<_sre.SRE_Match object; span=(3, 6), match='baz'>


>>> re.search('[a-z]', 'FOObar')
<_sre.SRE_Match object; span=(3, 4), match='b'>


>>> re.search('[0-9][0-9]', 'foo123bar')
<_sre.SRE_Match object; span=(3, 5), match='12'>
>>>
>>> re.search('[0-9a-fA-f]', '--- a0 ---')
<_sre.SRE_Match object; span=(4, 5), match='a'>
>>>
>>> re.search('[^0-9]', '12345foo')
<_sre.SRE_Match object; span=(5, 6), match='f'>
Here, the match object indicates that the first character in the string that isn’t a digit is 'f'.
>>>
>>> re.search('[#:^]', 'foo^bar:baz#qux')
<_sre.SRE_Match object; span=(3, 4), match='^'>

>>>
>>> re.search('[-abc]', '123-456')
<_sre.SRE_Match object; span=(3, 4), match='-'>
>>> re.search('[abc-]', '123-456')
<_sre.SRE_Match object; span=(3, 4), match='-'>
>>> re.search('[ab\-c]', '123-456')
<_sre.SRE_Match object; span=(3, 4), match='-'>

>>>
>>> re.search('[]]', 'foo[1]')
<_sre.SRE_Match object; span=(5, 6), match=']'>
>>> re.search('[ab\]cd]', 'foo[1]')
<_sre.SRE_Match object; span=(5, 6), match=']'>
>>>
>>> re.search('[)*+|]', '123*456')
<_sre.SRE_Match object; span=(3, 4), match='*'>
>>> re.search('[)*+|]', '123+456')
<_sre.SRE_Match object; span=(3, 4), match='+'>
```

As you saw in the table above, * and + have special meanings in a regex in Python. They designate repetition, which you’ll learn more about shortly. But inside a character class, they lose their special meaning.


### dot (.) - Specifies a wildcard

The . metacharacter matches any single character except a newline:

```python
>>> re.search('foo.bar', 'fooxbar')
<_sre.SRE_Match object; span=(0, 7), match='fooxbar'>

>>> print(re.search('foo.bar', 'foobar'))
None
>>> print(re.search('foo.bar', 'foo\nbar'))
None
```


### \w \W - Match based on whether a character is a word character.

\w matches any alphanumeric word character. Word characters are uppercase and lowercase letters, digits, and the underscore (_) character, so \w is essentially shorthand for [a-zA-Z0-9_]:

```
>>> re.search('\w', '#(.a$@&')
<_sre.SRE_Match object; span=(3, 4), match='a'>
>>> re.search('[a-zA-Z0-9_]', '#(.a$@&')
<_sre.SRE_Match object; span=(3, 4), match='a'>
```

\W is the opposite. It matches any non-word character and is equivalent to [^a-zA-Z0-9_]:

```python
>>> re.search('\W', 'a_1*3Qb')
<_sre.SRE_Match object; span=(3, 4), match='*'>
>>> re.search('[^a-zA-Z0-9_]', 'a_1*3Qb')
<_sre.SRE_Match object; span=(3, 4), match='*'>
```


### \d \D - Match based on whether a character is a decimal digit

```python
>>> re.search('\d', 'abc4def')
<_sre.SRE_Match object; span=(3, 4), match='4'>

>>> re.search('\D', '234Q678')
<_sre.SRE_Match object; span=(3, 4), match='Q'>
```


### \s \S - Match based on whether a character represents whitespace

```python
>>> re.search('\s', 'foo\nbar baz')
<_sre.SRE_Match object; span=(3, 4), match='\n'>
# Note that, unlike the dot wildcard metacharacter, \s does match a newline character.

```python
>>> re.search('\S', '  \n foo  \n  ')
<_sre.SRE_Match object; span=(4, 5), match='f'>
```

The character class sequences \w, \W, \d, \D, \s, and \S can appear inside a square bracket character class as well:

```python
>>> re.search('[\d\w\s]', '---3---')
<_sre.SRE_Match object; span=(3, 4), match='3'>
>>> re.search('[\d\w\s]', '---a---')
<_sre.SRE_Match object; span=(3, 4), match='a'>
>>> re.search('[\d\w\s]', '--- ---')
<_sre.SRE_Match object; span=(3, 4), match=' '>
```
<br>

 
## Escaping Metacharacters

Occasionally, you’ll want to include a metacharacter in your regex, except you won’t want it to carry its special meaning. Instead, you’ll want it to represent itself as a literal character.

### backslash (\)

Removes the special meaning of a metacharacter.
As you’ve just seen, the backslash character can introduce special character classes like word, digit, and whitespace. A metacharacter preceded by a backslash loses its special meaning and matches the literal character instead. 

```python
 1>>> re.search('.', 'foo.bar')
 2<_sre.SRE_Match object; span=(0, 1), match='f'>
 3
 4>>> re.search('\.', 'foo.bar')
 5<_sre.SRE_Match object; span=(3, 4), match='.'>

>>>
>>> s = r'foo\bar'
>>> print(s)
foo\bar

>>>
>>> re.search(r'\\', s)
<_sre.SRE_Match object; span=(3, 4), match='\\'>
```

 
## Anchors

Anchors are zero-width matches. They don’t match any actual characters in the search string, and they don’t consume any of the search string during parsing. Instead, an anchor dictates a particular location in the search string where a match must occur.

### ^ \A - Anchor a match to the start of <string>

When the regex parser encounters ^ or \A, the parser’s current position must be at the beginning of the search string for it to find a match.

```python
>>> re.search('^foo', 'foobar')
<_sre.SRE_Match object; span=(0, 3), match='foo'>
>>> print(re.search('^foo', 'barfoo'))
None

>>>
>>> re.search('\Afoo', 'foobar')
<_sre.SRE_Match object; span=(0, 3), match='foo'>
>>> print(re.search('\Afoo', 'barfoo'))
None
```


### $ \Z - Anchor a match to the end of <string>

When the regex parser encounters $ or \Z, the parser’s current position must be at the end of the search string for it to find a match. Whatever precedes $ or \Z must constitute the end of the search string:

```python
>>> re.search('bar$', 'foobar')
<_sre.SRE_Match object; span=(3, 6), match='bar'>
>>> print(re.search('bar$', 'barfoo'))
None

>>> re.search('bar\Z', 'foobar')
<_sre.SRE_Match object; span=(3, 6), match='bar'>
>>> print(re.search('bar\Z', 'barfoo'))
None
>>>
>>> re.search('bar$', 'foobar\n')
<_sre.SRE_Match object; span=(3, 6), match='bar'>
```


### \b - Anchors a match to a word boundary

\b asserts that the regex parser’s current position must be at the beginning or end of a word. A word consists of a sequence of alphanumeric characters or underscores ([a-zA-Z0-9_]), the same as for the \w character class:

```python
 1>>> re.search(r'\bbar', 'foo bar')
 2<_sre.SRE_Match object; span=(4, 7), match='bar'>
 3>>> re.search(r'\bbar', 'foo.bar')
 4<_sre.SRE_Match object; span=(4, 7), match='bar'>
 5
 6>>> print(re.search(r'\bbar', 'foobar'))
 7None
 8
 9>>> re.search(r'foo\b', 'foo bar')
10<_sre.SRE_Match object; span=(0, 3), match='foo'>
11>>> re.search(r'foo\b', 'foo.bar')
12<_sre.SRE_Match object; span=(0, 3), match='foo'>
13
14>>> print(re.search(r'foo\b', 'foobar'))
15None

>>>
>>> re.search(r'\bbar\b', 'foo bar baz')
<_sre.SRE_Match object; span=(4, 7), match='bar'>
>>> re.search(r'\bbar\b', 'foo(bar)baz')
<_sre.SRE_Match object; span=(4, 7), match='bar'>

>>> print(re.search(r'\bbar\b', 'foobarbaz'))
None
```

### \B - Anchors a match to a location that isn’t a word boundary

\B does the opposite of \b. It asserts that the regex parser’s current position must not be at the start or end of a word:

```python
 1>>> print(re.search(r'\Bfoo\B', 'foo'))
 2None
 3>>> print(re.search(r'\Bfoo\B', '.foo.'))
 4None
 5
 6>>> re.search(r'\Bfoo\B', 'barfoobaz')
 7<_sre.SRE_Match object; span=(3, 6), match='foo'>
```
<br>

 
## Quantifiers

A quantifier metacharacter immediately follows a portion of a <regex> and indicates how many times that portion must occur for the match to succeed.


### * - Matches zero or more repetitions of the preceding regex

For example, a* matches zero or more 'a' characters. That means it would match an empty string, 'a', 'aa', 'aaa', and so on.

```python
 1>>> re.search('foo-*bar', 'foobar')                     # Zero dashes
 2<_sre.SRE_Match object; span=(0, 6), match='foobar'>
 3>>> re.search('foo-*bar', 'foo-bar')                    # One dash
 4<_sre.SRE_Match object; span=(0, 7), match='foo-bar'>
 5>>> re.search('foo-*bar', 'foo--bar')                   # Two dashes
 6<_sre.SRE_Match object; span=(0, 8), match='foo--bar'>

>>>
>>> re.search('foo.*bar', '# foo $qux@grault % bar #')
<_sre.SRE_Match object; span=(2, 23), match='foo $qux@grault % bar'>
```


### + - Matches one or more repetitions of the preceding regex

This is similar to *, but the quantified regex must occur at least once:

```python
 1>>> print(re.search('foo-+bar', 'foobar'))              # Zero dashes
 2None
 3>>> re.search('foo-+bar', 'foo-bar')                    # One dash
 4<_sre.SRE_Match object; span=(0, 7), match='foo-bar'>
 5>>> re.search('foo-+bar', 'foo--bar')                   # Two dashes
 6<_sre.SRE_Match object; span=(0, 8), match='foo--bar'>
```


### ? - Matches zero or one repetitions of the preceding regex

Again, this is similar to * and +, but in this case there’s only a match if the preceding regex occurs once or not at all:

```python
 1>>> re.search('foo-?bar', 'foobar')                     # Zero dashes
 2<_sre.SRE_Match object; span=(0, 6), match='foobar'>
 3>>> re.search('foo-?bar', 'foo-bar')                    # One dash
 4<_sre.SRE_Match object; span=(0, 7), match='foo-bar'>
 5>>> print(re.search('foo-?bar', 'foo--bar'))            # Two dashes
 6None

>>>
>>> re.match('foo[1-9]*bar', 'foobar')
<_sre.SRE_Match object; span=(0, 6), match='foobar'>
>>> re.match('foo[1-9]*bar', 'foo42bar')
<_sre.SRE_Match object; span=(0, 8), match='foo42bar'>

>>> print(re.match('foo[1-9]+bar', 'foobar'))
None
>>> re.match('foo[1-9]+bar', 'foo42bar')
<_sre.SRE_Match object; span=(0, 8), match='foo42bar'>

>>> re.match('foo[1-9]?bar', 'foobar')
<_sre.SRE_Match object; span=(0, 6), match='foobar'>
>>> print(re.match('foo[1-9]?bar', 'foo42bar'))
None
```

 
### *?, +?, ?? - The non-greedy (or lazy) versions of the *, +, and ? quantifiers

When used alone, the quantifier metacharacters *, +, and ? are all greedy, meaning they produce the longest possible match. Consider this example:

```python
>>> re.search('<.*>', '%<foo> <bar> <baz>%')
<_sre.SRE_Match object; span=(1, 18), match='<foo> <bar> <baz>'>
```

If you want the shortest possible match instead, then use the non-greedy metacharacter sequence *?:

```python
>>> re.search('<.*?>', '%<foo> <bar> <baz>%')
<_sre.SRE_Match object; span=(1, 6), match='<foo>'>

>>>
 1>>> re.search('<.+>', '%<foo> <bar> <baz>%')
 2<_sre.SRE_Match object; span=(1, 18), match='<foo> <bar> <baz>'>
 3>>> re.search('<.+?>', '%<foo> <bar> <baz>%')
 4<_sre.SRE_Match object; span=(1, 6), match='<foo>'>
 5
 6>>> re.search('ba?', 'baaaa')
 7<_sre.SRE_Match object; span=(0, 2), match='ba'>
 8>>> re.search('ba??', 'baaaa')
 9<_sre.SRE_Match object; span=(0, 1), match='b'>
```


### {m} - Matches exactly m repetitions of the preceding regex

This is similar to * or +, but it specifies exactly how many times the preceding regex must occur for a match to succeed:

```python
>>> print(re.search('x-{3}x', 'x--x'))                # Two dashes
None

>>> re.search('x-{3}x', 'x---x')                      # Three dashes
<_sre.SRE_Match object; span=(0, 5), match='x---x'>

>>> print(re.search('x-{3}x', 'x----x'))              # Four dashes
None
```
<br>


## re Module Functions

In addition to re.search(), the re module contains several other functions to help you perform regex-related tasks.
The available regex functions in the Python re module fall into the following three categories:

1.	Searching functions
2.	Substitution functions
3.	Utility functions

The following sections explain these functions in more detail.


## Searching Functions

Searching functions scan a search string for one or more matches of the specified regex:

```python
Function	Description
re.search()	Scans a string for a regex match
re.match()	Looks for a regex match at the beginning of a string
re.fullmatch()	Looks for a regex match on an entire string
re.findall()	Returns a list of all regex matches in a string
re.finditer()	Returns an iterator that yields regex matches from a string


>>>
>>> re.search(r'\d+', '123foobar')
<_sre.SRE_Match object; span=(0, 3), match='123'>
>>> re.search(r'\d+', 'foo123bar')
<_sre.SRE_Match object; span=(3, 6), match='123'>

>>> re.match(r'\d+', '123foobar')
<_sre.SRE_Match object; span=(0, 3), match='123'>
>>> print(re.match(r'\d+', 'foo123bar'))
None

>>>
 1>>> print(re.fullmatch(r'\d+', '123foo'))
 2None
 3>>> print(re.fullmatch(r'\d+', 'foo123'))
 4None
 5>>> print(re.fullmatch(r'\d+', 'foo123bar'))
 6None
 7>>> re.fullmatch(r'\d+', '123')
 8<_sre.SRE_Match object; span=(0, 3), match='123'>
 9
10>>> re.search(r'^\d+$', '123')
11<_sre.SRE_Match object; span=(0, 3), match='123'>

>>>
>>> re.findall(r'\w+', '...foo,,,,bar:%$baz//|')
['foo', 'bar', 'baz']
>>>
>>> re.findall(r'#(\w+)#', '#foo#.#bar#.#baz#')
['foo', 'bar', 'baz']
>>>
 1>>> re.findall(r'(\w+),(\w+)', 'foo,bar,baz,qux,quux,corge')
 2[('foo', 'bar'), ('baz', 'qux'), ('quux', 'corge')]
 3
 4>>> re.findall(r'(\w+),(\w+),(\w+)', 'foo,bar,baz,qux,quux,corge')
 5[('foo', 'bar', 'baz'), ('qux', 'quux', 'corge')]


>>>
>>> it = re.finditer(r'\w+', '...foo,,,,bar:%$baz//|')
>>> next(it)
<_sre.SRE_Match object; span=(3, 6), match='foo'>
>>> next(it)
<_sre.SRE_Match object; span=(10, 13), match='bar'>
>>> next(it)
<_sre.SRE_Match object; span=(16, 19), match='baz'>
```
<br>


## Substitution Functions

Substitution functions replace portions of a search string that match a specified regex:

```python
Function	Description
re.sub()	Scans a string for regex matches, replaces the matching portions of the string with the specified replacement string, and returns the result
re.subn()	Behaves just like re.sub() but also returns information regarding the number of substitutions made
```

Both re.sub() and re.subn() create a new string with the specified substitutions and return it. The original string remains unchanged. (Remember that strings are immutable in Python, so it wouldn’t be possible for these functions to modify the original string.)


### re.sub(<regex>, <repl>, <string>, count=0, flags=0)

Returns a new string that results from performing replacements on a search string

```python
 1>>> s = 'foo.123.bar.789.baz'
 2
 3>>> re.sub(r'\d+', '#', s)
 4'foo.#.bar.#.baz'
 5>>> re.sub('[a-z]+', '(*)', s)
 6'(*).123.(*).789.(*)'

>>>
>>> re.sub(r'(\w+),bar,baz,(\w+)',
...        r'\2,bar,baz,\1',
...        'foo,bar,baz,qux')
'qux,bar,baz,foo'

>>>
>>> re.sub(r'foo,(?P<w1>\w+),(?P<w2>\w+),qux',
...        r'foo,\g<w2>,\g<w1>,qux',
...        'foo,bar,baz,qux')
'foo,baz,bar,qux'

>>>
>>> re.sub(r'foo,(\w+),(\w+),qux',
...        r'foo,\g<2>,\g<1>,qux',
...        'foo,bar,baz,qux')
'foo,baz,bar,qux'
```


### re.subn(<regex>, <repl>, <string>, count=0, flags=0)

Returns a new string that results from performing replacements on a search string and also returns the number of substitutions made.

re.subn() is identical to re.sub(), except that re.subn() returns a two-tuple consisting of the modified string and the number of substitutions made:

```python
>>> re.subn(r'\w+', 'xxx', 'foo.bar.baz.qux')
('xxx.xxx.xxx.xxx', 4)
>>> re.subn(r'\w+', 'xxx', 'foo.bar.baz.qux', count=2)
('xxx.xxx.baz.qux', 2)

>>> def f(match_obj):
...     m = match_obj.group(0)
...     if m.isdigit():
...         return str(int(m) * 10)
...     else:
...         return m.upper()
...
>>> re.subn(r'\w+', f, 'foo.10.bar.20.baz.30')
('FOO.100.BAR.200.BAZ.300', 6)
```


## Utility Functions

These are functions that involve regex matching but don’t clearly fall into either of the categories described above.

```python
Function	Description
re.split()	Splits a string into substrings using a regex as a delimiter
re.escape()	Escapes characters in a regex
```


### re.split(<regex>, <string>, maxsplit=0, flags=0)

Splits a string into substrings.

The following example splits the specified string into substrings delimited by a comma (,), semicolon (;), or slash (/) character, surrounded by any amount of whitespace:

```python
>>> re.split('\s*[,;/]\s*', 'foo,bar  ;  baz / qux')
['foo', 'bar', 'baz', 'qux']
```


### re.escape(<regex>)

Escapes characters in a regex.

```python
 1>>> print(re.match('foo^bar(baz)|qux', 'foo^bar(baz)|qux'))
 2None
 3>>> re.match('foo\^bar\(baz\)\|qux', 'foo^bar(baz)|qux')
 4<_sre.SRE_Match object; span=(0, 16), match='foo^bar(baz)|qux'>
 5
 6>>> re.escape('foo^bar(baz)|qux') == 'foo\^bar\(baz\)\|qux'
 7True
 8>>> re.match(re.escape('foo^bar(baz)|qux'), 'foo^bar(baz)|qux')
 9<_sre.SRE_Match object; span=(0, 16), match='foo^bar(baz)|qux'
```

<br><br>
