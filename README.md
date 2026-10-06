# Brain Trivia CLI

A colourful neuroscience quiz you can play in your terminal. Sixteen questions on neurons, brain regions, neurotransmitters and famous discoveries, with a fun fact after every answer.

## Run it

    python trivia.py           # 10 random questions
    python trivia.py --n 15    # pick how many

No dependencies, just Python 3.

## Add your own

Append a tuple to `QUESTIONS` in `trivia.py`:

    ("Question?", ["A option", "B option", "C option", "D option"], index_of_correct, "Fun fact shown afterwards."),

Pull requests with new questions are welcome.
