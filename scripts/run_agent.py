#!/usr/bin/env python3
"""Lightweight markdown revision runner for the McCloskey Writing Agent.

Usage:
    python scripts/run_agent.py input.md output.md
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Optional

try:
    from openai import OpenAI
except ImportError as exc:  # pragma: no cover - import guard for runtime
    raise SystemExit(
        "The 'openai' package is required. Install it with: pip install openai"
    ) from exc


def load_prompt(prompt_path: Path) -> str:
    """Read the system prompt from disk."""
    return prompt_path.read_text(encoding="utf-8")


def load_markdown(input_path: Path) -> str:
    """Read the source markdown draft."""
    return input_path.read_text(encoding="utf-8")


def revise_markdown(system_prompt: str, draft_text: str, model: str = "gpt-4.1-mini") -> str:
    """Send the draft to the OpenAI API and return the revised markdown."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set.")

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model=model,
        input=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": draft_text,
            },
        ],
    )

    return response.output_text.strip()


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="Revise a markdown draft using the McCloskey writing prompt")
    parser.add_argument("input", help="Path to the source markdown file")
    parser.add_argument("output", help="Path where the revised markdown will be written")
    parser.add_argument(
        "--model",
        default="gpt-4.1-mini",
        help="OpenAI model to use (default: gpt-4.1-mini)",
    )
    return parser.parse_args()


def main() -> None:
    """Entry point for the CLI."""
    args = parse_args()

    project_root = Path(__file__).resolve().parents[1]
    prompt_path = project_root / "prompts" / "system_prompt.md"
    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    system_prompt = load_prompt(prompt_path)
    draft_text = load_markdown(input_path)
    revised_text = revise_markdown(system_prompt, draft_text, model=args.model)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(revised_text + "\n", encoding="utf-8")
    print(f"Revised markdown written to {output_path}")


if __name__ == "__main__":
    main()
