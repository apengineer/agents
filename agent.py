"""
WealthPad AgentCore Runtime Entry Point
This module provides the entry point for the AgentCore Runtime deployment
"""

from financial_coach import create_financial_coach


def main():
    """
    Main entry point for local testing of the financial coach agent.
    """
    # Create the financial coach agent
    agent = create_financial_coach()
    
    # Test with a simple prompt
    test_message = "Hi! I just earned $5 from doing my chores. What should I do with it?"
    
    print("Testing WealthPad Financial Coach Agent")
    print("=" * 50)
    print(f"User: {test_message}")
    print("=" * 50)
    
    # Invoke the agent
    response = agent(test_message)
    
    print(f"Agent: {response}")
    print("=" * 50)


if __name__ == "__main__":
    main()
