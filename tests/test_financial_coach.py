"""
Tests for the financial coach agent
"""

import pytest
from financial_coach import create_financial_coach


def test_create_financial_coach():
    """Test that the financial coach agent can be created successfully."""
    agent = create_financial_coach()
    
    assert agent is not None
    assert agent.name == "WealthPad Financial Coach"


def test_agent_has_system_prompt():
    """Test that the agent is configured with a system prompt."""
    agent = create_financial_coach()
    
    assert agent.system_prompt is not None
    assert len(agent.system_prompt) > 0
    assert "financial coach" in agent.system_prompt.lower()
