"""CLI entry point for YT Agent."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ContentInstruction:
    """A human instruction that starts a YT Agent content run."""

    instruction: str


def create_instruction(instruction: str) -> ContentInstruction:
    """Create a validated content instruction."""
    cleaned = instruction.strip()
    if not cleaned:
        raise ValueError("Instruction must not be empty.")
    return ContentInstruction(instruction=cleaned)


def main() -> None:
    """Run the initial YT Agent foundation CLI."""
    print("YT Agent — YT-001 Agent Foundation")
    print("Content generation pipeline is ready for the next milestone.")


if __name__ == "__main__":
    main()
