"""Build Jekyll publication data from a BibTeX bibliography."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BIB_PATH = ROOT / "_bibliography" / "publications.bib"
OUT_PATH = ROOT / "_data" / "publications.yml"
VENUE_FIELDS = ("journal", "booktitle", "conference", "series", "archiveprefix")


def read_entries(text: str) -> list[tuple[str, str, str]]:
    """Return BibTeX entries as tuples of entry type, key, and raw field body."""
    entries = []
    index = 0

    while True:
        start = text.find("@", index)
        if start == -1:
            break

        brace_start = text.find("{", start)
        if brace_start == -1:
            break

        entry_type = text[start + 1 : brace_start].strip().lower()
        depth = 0
        end = brace_start
        for end in range(brace_start, len(text)):
            char = text[end]
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    break

        entry_text = text[brace_start + 1 : end]
        comma = entry_text.find(",")
        if comma != -1:
            key = entry_text[:comma].strip()
            body = entry_text[comma + 1 :]
            entries.append((entry_type, key, body))

        index = end + 1

    return entries


def parse_fields(body: str) -> dict[str, str]:
    """Parse simple BibTeX fields without external dependencies."""
    fields = {}
    index = 0

    while index < len(body):
        match = re.search(r"([A-Za-z][A-Za-z0-9_-]*)\s*=", body[index:])
        if not match:
            break

        name = match.group(1).lower()
        value_start = index + match.end()
        while value_start < len(body) and body[value_start].isspace():
            value_start += 1

        if value_start >= len(body):
            break

        quote = body[value_start]
        if quote == "{":
            depth = 1
            value_end = value_start + 1
            while value_end < len(body) and depth > 0:
                char = body[value_end]
                if char == "{":
                    depth += 1
                elif char == "}":
                    depth -= 1
                value_end += 1
            value = body[value_start + 1 : value_end - 1]
        elif quote == '"':
            value_end = value_start + 1
            while value_end < len(body):
                if body[value_end] == '"' and body[value_end - 1] != "\\":
                    break
                value_end += 1
            value = body[value_start + 1 : value_end]
            value_end += 1
        else:
            value_end = value_start
            while value_end < len(body) and body[value_end] not in ",\n":
                value_end += 1
            value = body[value_start:value_end]

        fields[name] = clean_value(value)
        index = value_end + 1

    return fields


def clean_value(value: str) -> str:
    """Normalize whitespace and remove lightweight BibTeX wrapping braces."""
    value = value.replace("\n", " ")
    value = re.sub(r"\s+", " ", value).strip()
    value = value.replace("{", "").replace("}", "")
    return value


def format_authors(value: str) -> str:
    """Convert common BibTeX author names into a readable text string."""
    authors = []
    for author in value.split(" and "):
        author = author.strip()
        if "," in author:
            last, first = [part.strip() for part in author.split(",", 1)]
            author = f"{first} {last}".strip()
        authors.append(author)
    return ", ".join(authors)


def slugify(value: str) -> str:
    """Create a stable lowercase id from the BibTeX key."""
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return slug or "publication"


def yaml_quote(value: str) -> str:
    """Quote a scalar string for simple YAML output."""
    return "'" + value.replace("'", "''") + "'"


def build_publications() -> list[dict[str, str]]:
    """Build normalized publication records from the bibliography."""
    records = []
    for entry_type, key, body in read_entries(BIB_PATH.read_text(encoding="utf-8")):
        fields = parse_fields(body)
        venue = next((fields[field] for field in VENUE_FIELDS if fields.get(field)), "")
        year = fields.get("year", "")

        records.append(
            {
                "id": slugify(key),
                "title": fields.get("title", ""),
                "authors": format_authors(fields.get("author", "")),
                "venue": venue,
                "year": year,
                "doi": fields.get("doi", ""),
                "url": fields.get("url", ""),
                "type": entry_type,
                "bibtex_key": key,
            }
        )

    return sorted(records, key=lambda record: int(record["year"] or 0), reverse=True)


def write_yaml(records: list[dict[str, str]]) -> None:
    """Write publication records as dependency-free YAML."""
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fields = ("id", "title", "authors", "venue", "year", "doi", "url", "type", "bibtex_key")
    lines = []
    for record in records:
        lines.append(f"- id: {yaml_quote(record['id'])}")
        for field in fields[1:]:
            lines.append(f"  {field}: {yaml_quote(record[field])}")
        lines.append("")
    OUT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """Generate _data/publications.yml from _bibliography/publications.bib."""
    write_yaml(build_publications())


if __name__ == "__main__":
    main()
