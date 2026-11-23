"""make.fun entry: Make the AI Judge Laugh - Office Jokes.

Writes the one-line joke entry to /output/entry.txt with no trailing newline.
"""

ENTRY = "I asked HR for a raise and they gave me a pizza party — so now I'm the highest-paid slice in the office."


def main() -> None:
    import os

    # Write the entry to the output directory so the judge can pick it up.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
