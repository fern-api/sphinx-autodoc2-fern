---
layout: overview
slug: nemo-curator-stages-text-filters-heuristic-filter
---

# nemo_curator.stages.text.filters.heuristic_filter



## Module Contents

### Classes

| Name | Description |
|------|-------------|
| [`NonAlphaNumericFilter`](#nemo_curatorstagestextfiltersheuristic_filternonalphanumericfilter) | If more than 25% of the document is non-alphanumeric, then discard. Intended to be applied only to English text. Source: Adapted from Gopher (Rae et al., 2021) |
| [`SymbolsToWordsFilter`](#nemo_curatorstagestextfiltersheuristic_filtersymbolstowordsfilter) | Remove any document with a symbol-to-word ratio greater than 0.1 for either the hash symbol or the elipsis. Source: Gopher (Rae et al., 2021) |
| [`NumbersFilter`](#nemo_curatorstagestextfiltersheuristic_filternumbersfilter) | If more than 15% of the document contains numbers, then discard. |
| [`UrlsFilter`](#nemo_curatorstagestextfiltersheuristic_filterurlsfilter) | If more than 20% of the document is comprised of URLs, then discard. |
| [`BulletsFilter`](#nemo_curatorstagestextfiltersheuristic_filterbulletsfilter) | If more than 90% of the lines start with a bullet, then discard. Source: Gopher (Rae et al., 2021) |
| [`WhiteSpaceFilter`](#nemo_curatorstagestextfiltersheuristic_filterwhitespacefilter) | If the document contains a significant number of white space characters, then discard. |
| [`ParenthesesFilter`](#nemo_curatorstagestextfiltersheuristic_filterparenthesesfilter) | If more than 10% of the sentence is in parentheses, then discard. |
| [`LongWordFilter`](#nemo_curatorstagestextfiltersheuristic_filterlongwordfilter) | If the document contains a word longer than 1000 characters, then discard. NOTE: This seems to be catching things like minified `.js` files that don't have spaces anywhere. Source: C4 (Google) |
| [`WordCountFilter`](#nemo_curatorstagestextfiltersheuristic_filterwordcountfilter) | If a document contains a number of words not within a specified range, then discard. |
| [`BoilerPlateStringFilter`](#nemo_curatorstagestextfiltersheuristic_filterboilerplatestringfilter) | If more than 40% of paragraphs contain boilerplate strings, then discard. This includes things like "terms of use", "privacy policy", etc. Source: Adapted significantly from Google C4 processing. |
| [`MeanWordLengthFilter`](#nemo_curatorstagestextfiltersheuristic_filtermeanwordlengthfilter) | If the mean word length is not in a specified range, then discard. |
| [`RepeatedLinesFilter`](#nemo_curatorstagestextfiltersheuristic_filterrepeatedlinesfilter) | If the document shrinks by > 30% in terms of number of lines after removing duplicate lines, then discard. Source: Gopher (Rae et al., 2021) |
| [`RepeatedParagraphsFilter`](#nemo_curatorstagestextfiltersheuristic_filterrepeatedparagraphsfilter) | If the document shrinks by > 30% in terms of number of lines after removing duplicate paragraphs, then discard. Source: Gopher (Rae et al., 2021) |
| [`RepeatedLinesByCharFilter`](#nemo_curatorstagestextfiltersheuristic_filterrepeatedlinesbycharfilter) | If the document shrinks by > 20% in terms of number of lines after removing duplicate lines, then discard. Source: Gopher (Rae et al., 2021) |
| [`RepeatedParagraphsByCharFilter`](#nemo_curatorstagestextfiltersheuristic_filterrepeatedparagraphsbycharfilter) | If the document shrinks by > 10% in terms of number of lines after removing duplicate paragraphs, then discard. Source: Gopher (Rae et al., 2021) |
| [`RepeatingTopNGramsFilter`](#nemo_curatorstagestextfiltersheuristic_filterrepeatingtopngramsfilter) | If the document shrinks by > x% in terms of number of characters after removing the top n-grams, then discard. Source: Gopher (Rae et al., 2021) |
| [`RepeatingDuplicateNGramsFilter`](#nemo_curatorstagestextfiltersheuristic_filterrepeatingduplicatengramsfilter) | If the document shrinks by > x% in terms of number of characters after removing all duplicate n-grams, then discard. Source: Gopher (Rae et al., 2021) |
| [`PunctuationFilter`](#nemo_curatorstagestextfiltersheuristic_filterpunctuationfilter) | If more than 85% of the sentences do not end with a punctuation mark, then discard. Source: Google C4 processing |
| [`EllipsisFilter`](#nemo_curatorstagestextfiltersheuristic_filterellipsisfilter) | If more than 30% of the sentences end with an elipsis, then discard. Source: Google C4 processing |
| [`CommonEnglishWordsFilter`](#nemo_curatorstagestextfiltersheuristic_filtercommonenglishwordsfilter) | If the sentence contains at least 2 common English words, then keep it. NOTE: We purposefully check for the lowercase versions of those common words to remove documents with over-capitalization. |
| [`WordsWithoutAlphabetsFilter`](#nemo_curatorstagestextfiltersheuristic_filterwordswithoutalphabetsfilter) | 80% of words in a document must contain at least one alphabetic character. Source: Gopher (Rae et al., 2021) |
| [`PornographicUrlsFilter`](#nemo_curatorstagestextfiltersheuristic_filterpornographicurlsfilter) | Check if any of the URLs within the document point to pornography. |
| [`TokenCountFilter`](#nemo_curatorstagestextfiltersheuristic_filtertokencountfilter) | If the document contains more or less than a specified number of tokens, then discard. |
| [`SubstringFilter`](#nemo_curatorstagestextfiltersheuristic_filtersubstringfilter) | Keeps documents that contain a substring in a given position. Gives a score of 1 if the substring is found in the given position, otherwise 0. |
| [`HistogramFilter`](#nemo_curatorstagestextfiltersheuristic_filterhistogramfilter) | Histogram filter used by the NLLB paper (https://arxiv.org/pdf/2207.04672). See p30 for details. |

### API

```python
class nemo_curator.stages.text.filters.heuristic_filter.NonAlphaNumericFilter(max_non_alpha_numeric_to_text_ratio: float = 0.25)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If more than 25% of the document is non-alphanumeric, then discard.
Intended to be applied only to English text.
Source: Adapted from Gopher (Rae et al., 2021)

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.SymbolsToWordsFilter(max_symbol_to_word_ratio: float = 0.1, lang: str = 'en')
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

Remove any document with a symbol-to-word ratio greater than
0.1 for either the hash symbol or the elipsis.
Source: Gopher (Rae et al., 2021)

For Chinese and Japanese text, we use external libraries to split the text
because these languages are not separated by spaces. For all other languages,
such as English, we assume words are separated by spaces.

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.NumbersFilter(max_number_to_text_ratio: float = 0.15)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If more than 15% of the document contains numbers, then discard.

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.UrlsFilter(max_url_to_text_ratio: float = 0.2)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If more than 20% of the document is comprised of URLs, then discard.

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.BulletsFilter(max_bullet_lines_ratio: float = 0.9)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If more than 90% of the lines start with a bullet, then discard.
Source: Gopher (Rae et al., 2021)

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.WhiteSpaceFilter(max_white_space_ratio: float = 0.25)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If the document contains a significant number
of white space characters, then discard.

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.ParenthesesFilter(max_parentheses_ratio: float = 0.1)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If more than 10% of the sentence is in parentheses, then discard.

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.LongWordFilter(max_word_length: int = 1000, lang: str = 'en')
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If the document contains a word longer than 1000 characters, then discard.
NOTE: This seems to be catching things like minified `.js` files
that don't have spaces anywhere.
Source: C4 (Google)

For Chinese and Japanese text, we use external libraries to split the text
because these languages are not separated by spaces. For all other languages,
such as English, we assume words are separated by spaces.

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.WordCountFilter(min_words: int = 50, max_words: int = 100000, lang: str = 'en')
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If a document contains a number of words not
within a specified range, then discard.

For Chinese and Japanese text, we use external libraries to split the text
because these languages are not separated by spaces. For all other languages,
such as English, we assume words are separated by spaces.

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.BoilerPlateStringFilter(remove_if_at_top_or_bottom: bool = True, max_boilerplate_string_ratio: float = 0.4)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If more than 40% of paragraphs contain boilerplate strings, then discard.
This includes things like "terms of use", "privacy policy", etc.
Source: Adapted significantly from Google C4 processing.

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.MeanWordLengthFilter(min_mean_word_length: int = 3, max_mean_word_length: int = 10, lang: str = 'en')
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If the mean word length is not in a specified range, then discard.

For Chinese and Japanese text, we use external libraries to split the text
because these languages are not separated by spaces. For all other languages,
such as English, we assume words are separated by spaces.

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.RepeatedLinesFilter(max_repeated_line_fraction: float = 0.7)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If the document shrinks by > 30% in terms of number of lines after
removing duplicate lines, then discard.
Source: Gopher (Rae et al., 2021)

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.RepeatedParagraphsFilter(max_repeated_paragraphs_ratio: float = 0.7)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If the document shrinks by > 30% in terms of number of lines after
removing duplicate paragraphs, then discard.
Source: Gopher (Rae et al., 2021)

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.RepeatedLinesByCharFilter(max_repeated_lines_char_ratio: float = 0.8)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If the document shrinks by > 20% in terms of number of lines
after removing duplicate lines, then discard.
Source: Gopher (Rae et al., 2021)

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.RepeatedParagraphsByCharFilter(max_repeated_paragraphs_char_ratio: float = 0.8)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If the document shrinks by > 10% in terms of number of lines after
removing duplicate paragraphs, then discard.
Source: Gopher (Rae et al., 2021)

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.RepeatingTopNGramsFilter(n: int = 2, max_repeating_ngram_ratio: float = 0.2, lang: str = 'en')
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If the document shrinks by > x% in terms of number of characters after
removing the top n-grams, then discard.
Source: Gopher (Rae et al., 2021)

For Chinese and Japanese text, we use external libraries to split the text
because these languages are not separated by spaces. For all other languages,
such as English, we assume words are separated by spaces.

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.RepeatingDuplicateNGramsFilter(n: int = 2, max_repeating_duplicate_ngram_ratio: float = 0.2, lang: str = 'en')
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If the document shrinks by > x% in terms of number of characters
after removing all duplicate n-grams, then discard.
Source: Gopher (Rae et al., 2021)

For Chinese and Japanese text, we use external libraries to split the text
because these languages are not separated by spaces. For all other languages,
such as English, we assume words are separated by spaces.

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.PunctuationFilter(max_num_sentences_without_endmark_ratio: float = 0.85)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If more than 85% of the sentences do not end with a
punctuation mark, then discard.
Source: Google C4 processing

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.EllipsisFilter(max_num_lines_ending_with_ellipsis_ratio: float = 0.3)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If more than 30% of the sentences end with an elipsis, then discard.
Source: Google C4 processing

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.CommonEnglishWordsFilter(min_num_common_words: int = 2, stop_at_false: bool = True)
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If the sentence contains at least 2 common English words, then keep it.
NOTE: We purposefully check for the lowercase versions of those common words
to remove documents with over-capitalization.

For Chinese and Japanese text, we use external libraries to split the text
because these languages are not separated by spaces. For all other languages,
such as English, we assume words are separated by spaces.

```python
score_document(text: str) -> int
```


```python
keep_document(score: int) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.WordsWithoutAlphabetsFilter(min_words_with_alphabets: float = 0.8, lang: str = 'en')
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

80% of words in a document must contain at least one alphabetic character.
Source: Gopher (Rae et al., 2021)

For Chinese and Japanese text, we use external libraries to split the text
because these languages are not separated by spaces. For all other languages,
such as English, we assume words are separated by spaces.

```python
score_document(text: str) -> float
```


```python
keep_document(score: float) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.PornographicUrlsFilter
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

Check if any of the URLs within the document point to pornography.

```python
score_document(text: str) -> int
```


```python
keep_document(score: int) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.TokenCountFilter(tokenizer: transformers.AutoTokenizer | None = None, hf_model_name: str | None = None, hf_token: str | None = None, min_tokens: int = 0, max_tokens: int = float('inf'))
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

If the document contains more or less than a specified number of tokens, then discard.

### Initialization

**Parameters:**

- **tokenizer (AutoTokenizer | None)**: The pre-loaded tokenizer to use to count the tokens.
  If None, the tokenizer will be initialized from the hf_model_name.
- **hf_model_name (str | None)**: The name of the Hugging Face model to use to count the tokens.
  If None, the pre-loaded tokenizer must be provided via the tokenizer argument.
- **hf_token (str | None)**: The token to use to access the Hugging Face model, if needed.
- **min_tokens (int)**: The minimum number of tokens the document must contain.
  Set to 0 to disable the minimum token count filter.
- **max_tokens (int)**: The maximum number of tokens the document can contain.
  Set to infinity to disable the maximum token count filter.


```python
model_check_or_download() -> None
```


```python
load_tokenizer() -> None
```


```python
score_document(text: str) -> int
```


```python
keep_document(score: int) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.SubstringFilter(substring: str, position: typing.Literal[prefix, suffix, any])
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

Keeps documents that contain a substring in a given position.
Gives a score of 1 if the substring is found in the given position, otherwise 0.

### Initialization

**Parameters:**

- **substring (str)**: The substring to check for.
- **position (Literal["prefix", "suffix", "any"])**: The position of the substring.


```python
score_document(text: str) -> int
```


```python
keep_document(score: int) -> bool
```


```python
class nemo_curator.stages.text.filters.heuristic_filter.HistogramFilter(lang: str | None = 'en', threshold: float | None = 0.8, cache_dir: str | None = '', threshold_char: str | None = ']')
```

**Bases**: `nemo_curator.stages.text.filters.doc_filter.DocumentFilter`

Histogram filter used by the NLLB paper (https://arxiv.org/pdf/2207.04672). See p30 for details.

The high-level idea of histogram filter can be described as a cheap version of language ID.
Basically, it checks what ratio of characters in the data instance are included in the character historgrams collected from trusted data in the corresponding language.
If the ratio is too low, then there is a good chance that there is a language ID mismatch and the data instance should be discarded.

Written with reference to the original fairseq implementation at:
https://github.com/facebookresearch/fairseq/blob/main/examples/m2m_100/process_data/clean_histogram.py.

### Initialization

**Parameters:**

- **lang (str, optional)**: Expected language of the segment. This will decide which histogram will be loaded. Defaults to "en".
- **threshold (float, optional)**: Threshold for ratio of characters in the histogram. Defaults to 0.8.
- **cache_dir (str, optional)**: Cache dir download histogram files. Defaults to "".
- **threshold_char (str, optional)**: Formatter character of the histogram files. You should not change this unless you rebuilt your own histogram. Defaults to "]".


```python
_download_histograms() -> None
```

Download and process histograms from default repo.

**Raises:**

requests.exceptions.RequestException: If download fails.


```python
_read_hist() -> None
```

Load histogram files.


```python
score_document(text: str) -> float
```

Compute histogram token ratio of a text data instance according to the loaded histogram.

**Parameters:**

**Returns:**

float: Ratio of tokens included in the histogram.


```python
keep_document(score: float) -> bool
```

