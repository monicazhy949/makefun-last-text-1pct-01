"""Last Text at One Percent — entry program.

Writes the phone's final text to /output/entry.txt.
"""

from pathlib import Path

ENTRY = "I'm at 1%, so one last confession: your 'five more minutes' was three hours. I counted. All 847 times. Tell my charger I loved her. Bye."


def main() -> None:
    print(ENTRY)
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
