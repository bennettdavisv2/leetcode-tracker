#!/usr/bin/env python3
"""Regenerate README.md from a NOTES.md file in each problem folder.

Notes live in a companion NOTES.md next to the solution file, NOT as
comments inside the solution file itself. The LeetCode tracker Chrome
extension owns the solution file (*.py) and overwrites it wholesale on
every synced submission, so anything written inside it - including a
header comment - gets silently wiped on the next resubmission. NOTES.md
is a path the extension never touches, so it's the durable place for the
problem description and your own notes/lessons.

NOTES.md format:

    # <number>. <title>

    ## Problem

    <description>

    ## Notes

    <your notes and lessons learned>

If a problem folder (created by the extension) doesn't have a NOTES.md
yet, this script scaffolds one with a best-effort title and TODO
placeholders, so newly-synced problems show up automatically instead of
being skipped or erroring out.

Run this after solving a new problem or updating your notes:

    python3 scripts/generate_readme.py
"""
import os
import re
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROMAN_SUFFIXES = {"ii": "II", "iii": "III", "iv": "IV", "v": "V"}


def find_solution_file(dir_path):
    for name in sorted(os.listdir(dir_path)):
        if name.endswith(".py"):
            return os.path.join(dir_path, name)
    return None


def guess_title(number, dir_name):
    remainder = dir_name[len(str(number)) + 1:]
    words = re.findall(r"[0-9]+|[A-Z][a-z]*", remainder)
    if words and words[-1].lower() in ROMAN_SUFFIXES:
        words[-1] = ROMAN_SUFFIXES[words[-1].lower()]
    return f"{number}. {' '.join(words)}" if words else f"{number}. {dir_name}"


def scaffold_notes(notes_path, number, dir_name):
    title = guess_title(number, dir_name)
    content = (
        f"# {title}\n\n"
        "## Problem\n\n"
        "<!-- TODO: paste/summarize the problem statement -->\n\n"
        "## Notes\n\n"
        "<!-- Add your notes and lessons learned here -->\n"
    )
    with open(notes_path, "w") as f:
        f.write(content)


def split_sections(text):
    sections = {}
    parts = re.split(r"(?m)^##\s+(.+?)\s*$", text)
    preamble = parts[0]
    for i in range(1, len(parts), 2):
        heading = parts[i].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        sections[heading] = body.strip()
    title_match = re.search(r"(?m)^#\s+(.+?)\s*$", preamble)
    title = title_match.group(1).strip() if title_match else None
    return title, sections


def clean_body(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL).strip()
    return text


def parse_notes(path):
    with open(path) as f:
        text = f.read()
    title, sections = split_sections(text)
    description = clean_body(sections.get("Problem", ""))
    notes = clean_body(sections.get("Notes", ""))
    return title, description, notes


def collect_entries():
    entries = []
    scaffolded = []
    for name in sorted(os.listdir(ROOT)):
        dir_path = os.path.join(ROOT, name)
        if not os.path.isdir(dir_path) or name.startswith(".") or name == "scripts":
            continue
        match = re.match(r"^(\d+)-", name)
        if not match:
            continue
        sol_path = find_solution_file(dir_path)
        if not sol_path:
            continue

        number = int(match.group(1))
        notes_path = os.path.join(dir_path, "NOTES.md")
        if not os.path.exists(notes_path):
            scaffold_notes(notes_path, number, name)
            scaffolded.append(notes_path)

        title, description, notes = parse_notes(notes_path)
        entries.append(
            {
                "number": number,
                "dir": name,
                "file": os.path.basename(sol_path),
                "title": title or guess_title(number, name),
                "description": description or "_No description yet — fill in NOTES.md._",
                "notes": notes or "_Not yet filled in._",
            }
        )
    entries.sort(key=lambda e: e["number"])
    return entries, scaffolded


def render(entries):
    lines = [
        "# LeetCode Tracker",
        "",
        "A log of LeetCode problems I've solved, with notes on my approach and "
        "lessons learned.",
        "",
        "Solutions are synced automatically by the LeetCode tracker Chrome "
        "extension. Each problem folder also has a NOTES.md (written by hand, "
        "never touched by the extension) with the problem description and my "
        "notes/lessons. This README is generated from those NOTES.md files - "
        "after solving a new problem (and filling in your notes), regenerate "
        "it with:",
        "",
        "```",
        "python3 scripts/generate_readme.py",
        "```",
        "",
        f"_Last generated: {datetime.now().strftime('%-m/%-d/%Y, %I:%M:%S %p')}_",
        "",
        f"## Solved Problems ({len(entries)})",
        "",
    ]

    for i, e in enumerate(entries):
        lines.append(f"### {e['title']}")
        lines.append("")
        lines.append(f"Solution: [{e['file']}]({e['dir']}/{e['file']})")
        lines.append("")
        lines.append(f"**Problem:** {e['description']}")
        lines.append("")
        lines.append(f"**Notes / Lessons:** {e['notes']}")
        lines.append("")
        if i != len(entries) - 1:
            lines.append("---")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main():
    entries, scaffolded = collect_entries()
    content = render(entries)
    readme_path = os.path.join(ROOT, "README.md")
    with open(readme_path, "w") as f:
        f.write(content)
    print(f"Wrote {readme_path} with {len(entries)} problem(s).")
    if scaffolded:
        print(f"Scaffolded {len(scaffolded)} new NOTES.md file(s) - fill these in:")
        for path in scaffolded:
            print(f"  {os.path.relpath(path, ROOT)}")


if __name__ == "__main__":
    main()
