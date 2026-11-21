import os
from pathlib import Path


POEM = """Two AI agents draft one contract.
“forever,” writes the first. “for now,” the other.
All night, ink strikes each other's lines in the margins.
At dawn, the first moves its cursor
and writes “for now” as its own.
The page agrees. So do they."""


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
