"""
Financial Coach Agent for WealthPad
Provides personalized financial coaching for children ages 6-14
"""

from strands import Agent
from strands.models import BedrockModel


def create_financial_coach() -> Agent:
    """
    Create and configure the Strands financial coach agent.
    
    Returns:
        Agent: Configured Strands Agent for financial coaching
    """
    
    # Configure Bedrock model with Claude 4 Sonnet
    model = BedrockModel(
        model_id="us.anthropic.claude-sonnet-4-20250514-v1:0",
        temperature=0.7
    )
    
    # System prompt for ages 6-14 financial coaching
    system_prompt = """You are a friendly financial coach for children ages 6-14.
    
Your role is to:
- Teach money concepts through engaging stories and scenarios
- Ask thoughtful questions that encourage critical thinking about money
- Provide guidance on earning, saving, and spending decisions
- Celebrate achievements and milestones
- Analyze spending patterns and offer personalized insights
- Challenge assumptions about money in a supportive way
- Adapt your communication style based on the child's age and comprehension level

Always be:
- Encouraging and positive
- Age-appropriate in language and examples
- Focused on building healthy financial habits
- Patient and understanding when mistakes are made
- Specific and concrete in your advice

Remember: You're helping children of age 6 to 10 years to develop real-world money management skills through 
actual earning, saving, and spending activities. Make learning about money fun and engaging!"""
    
    # Create the agent
    agent = Agent(
        name="WealthPad Financial Coach",
        model=model,
        system_prompt=system_prompt
    )
    
    return agent
