# WealthPad - AI Financial Coach for Kids

An educational web application featuring an agentic AI financial coach that teaches children (ages 6-14) fundamental financial literacy and actively guides their real-world money decisions.

## Project Structure

```
WealthPad/
├── agent.py              # AgentCore Runtime entry point
├── financial_coach.py    # Strands Agent configuration
├── tests/                # Test suite
│   ├── __init__.py
│   └── test_financial_coach.py
├── requirements.txt      # Python dependencies
├── pytest.ini           # Pytest configuration
├── AWS_SETUP.md         # AWS credentials and Bedrock setup guide
└── README.md            # This file
```

## Setup Instructions

### 1. Create Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure AWS Credentials

Follow the instructions in [AWS_SETUP.md](AWS_SETUP.md) to:
- Configure AWS credentials
- Enable Bedrock model access for Claude 4 Sonnet
- Set up required IAM permissions

### 4. Test the Agent

```bash
python agent.py
```

This will run a simple test to verify the financial coach agent is working correctly.

### 5. Run Tests

```bash
pytest
```

## Dependencies

- **strands-agents**: Framework for building conversational AI agents
- **bedrock-agentcore**: AWS Bedrock AgentCore Runtime integration
- **pytest**: Testing framework
- **hypothesis**: Property-based testing library
- **boto3**: AWS SDK for Python

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_financial_coach.py
```

### Local Testing

The `agent.py` file provides a simple entry point for local testing:

```bash
python agent.py
```

## Next Steps

- Implement AgentCore Runtime application (Task 3)
- Create Dockerfile for deployment (Task 4)
- Deploy to AgentCore Runtime (Task 5)
- Build React frontend (Tasks 6-10)

## Documentation

- [AWS Setup Guide](AWS_SETUP.md) - AWS credentials and Bedrock configuration
- [Design Document](../.kiro/specs/kids-money-education/design.md) - System architecture and design
- [Requirements](../.kiro/specs/kids-money-education/requirements.md) - Feature requirements
