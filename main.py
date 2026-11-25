"""The Dog Ate My Homework: Funniest Excuse.

One line, under 200 characters, of the excuse a dog gives after
being caught eating the homework, written to /output/entry.txt.

The dog speaks in its own voice, with a dog's priorities and none
of a person's embarrassment: it smelled like bacon, it tasted like
victory, and the whole thing is the human's fault for leaving it
next to the bowl at nose height. The twist is dog logic -- the
homework was, by placement, food -- and it lands in a single line
with no setup and nothing that needs a second line to make sense.
"""

import os

SENSE = "It smelled like bacon, it tasted like victory,"
DEFENCE = "and honestly, if you'd wanted it saved,"
BLAME = "you wouldn't have left it next to my bowl at nose height."

MAX_CHARS = 200
MIN_CHARS = 1


def compose(sense: str, defence: str, blame: str) -> str:
    """Join the excuse's three beats into one line."""
    parts = [sense.strip(), defence.strip(), blame.strip()]
    line = " ".join(parts)
    return line


def check_excuse(line: str) -> str:
    """Gate the excuse the way the sealed scorer does.

    /output/entry.txt must be UTF-8 text of 1 to 200 characters, and
    the brief asks for one line.
    """
    assert MIN_CHARS <= len(line) <= MAX_CHARS, f"excuse is {len(line)} chars"
    assert line == line.strip(), "no stray whitespace around the excuse"
    assert "\n" not in line, "the excuse must stay on one line"
    return line


def excuse_notes(line: str) -> dict:
    """Per-bounty excuse check: the dog's voice, dog logic, one line.

    The judge picks the excuse that earns the bigger laugh, so the
    entry must be the dog's own explanation after being caught eating
    the homework -- in the dog's voice, with a dog's priorities
    (smell, taste, the bowl at nose height) and none of a person's
    embarrassment. The twist has to be dog logic: the homework was
    food by placement.
    """
    lowered = line.lower()
    assert "bacon" in lowered, "the excuse must open on the dog's senses"
    assert "bowl" in lowered, "the blame must be placed at nose height"
    assert "sorry" not in lowered, "a dog shows no embarrassment"
    assert "homework" in lowered or "it" in lowered, "the excuse must be about the homework"
    words = line.split()
    return {"words": len(words), "chars": len(line), "lines": 1}


def main() -> None:
    line = check_excuse(compose(SENSE, DEFENCE, BLAME))
    notes = excuse_notes(line)
    assert notes["lines"] == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
