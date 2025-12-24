# bookbot

BookBot is a tiny command-line tool for analyzing plain-text books.

It reads a text file, counts total words, and computes character frequencies (letters only), then prints a sorted list of most-common letters.

## Features

- Read a book (plain .txt file) from disk
- Count total words
- Count characters (case-insensitive) and show a sorted list of letters by frequency

## Requirements

- Python 3.8+ (this project uses only the standard library)

## Quick start

From the project root (the folder that contains `main.py`):

```bash
# macOS / zsh
python3 main.py books/frankenstein.txt
```

Example output (truncated):

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
t: 12345
e: 11234
a: 10203
... (other letters)
============= END ===============
```

## Files

- `main.py` — program entrypoint and CLI handling
- `stats.py` — helper functions: reading files, counting words, counting characters, and sorting
- `books/` — sample book files used for testing (e.g. `frankenstein.txt`)

## Implementation notes

- Character counts are case-insensitive (letters are converted to lower-case).
- Non-letter characters are filtered out when producing the sorted letter frequency list.
- The README contains usage examples for running the script locally; you can pass any plain-text file path as the argument.

## Extending

- Add support for other statistics (top N words, sentence counts, reading time estimates).
- Add tests for `stats.py` (e.g. using `unittest` or `pytest`).

## Contributing

1. Fork the repository
2. Create a topic branch
3. Open a pull request with a clear description of your changes

## License

This project is unlicensed (add a LICENSE file if you want to apply an open-source license).

---

If anything in this README is unclear or you'd like a different example (e.g., how to run it from another folder or how to pipe input), tell me what you want and I can update it.