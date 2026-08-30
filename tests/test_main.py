import pytest

from yt_agent.main import create_instruction


def test_create_instruction_strips_whitespace() -> None:
    result = create_instruction("  Build an AI agent Short  ")
    assert result.instruction == "Build an AI agent Short"


def test_create_instruction_rejects_empty_instruction() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        create_instruction("   ")
