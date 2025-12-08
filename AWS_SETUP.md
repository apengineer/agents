# AWS Configuration Setup

This document describes how to configure AWS credentials and Bedrock model access for the WealthPad AgentCore agent.

## Prerequisites

1. AWS Account with access to Amazon Bedrock
2. AWS CLI installed
3. Appropriate IAM permissions for Bedrock

## AWS Credentials Configuration

### Option 1: AWS CLI Configuration (Recommended)

```bash
aws configure
```

Enter your:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g., `us-east-1`)
- Default output format (e.g., `json`)

### Option 2: Environment Variables

Set the following environment variables:

```bash
export AWS_ACCESS_KEY_ID=your_access_key_id
export AWS_SECRET_ACCESS_KEY=your_secret_access_key
export AWS_DEFAULT_REGION=us-east-1
```

### Option 3: IAM Role (for EC2/ECS/Lambda)

If running on AWS infrastructure, attach an IAM role with appropriate Bedrock permissions.

## Bedrock Model Access

### Enable Claude 4 Sonnet Model

1. Navigate to Amazon Bedrock console
2. Go to "Model access" in the left sidebar
3. Click "Manage model access"
4. Enable access to: `Claude 4 Sonnet (us.anthropic.claude-sonnet-4-20250514-v1:0)`
5. Submit the request and wait for approval (usually instant)

### Required IAM Permissions

Your IAM user/role needs the following permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream"
            ],
            "Resource": "arn:aws:bedrock:*::foundation-model/us.anthropic.claude-sonnet-4-20250514-v1:0"
        }
    ]
}
```

## Verification

Test your configuration by running:

```bash
python agent.py
```

If configured correctly, the agent should respond to the test prompt.

## Troubleshooting

### "Access Denied" Error
- Verify IAM permissions include `bedrock:InvokeModel`
- Check that model access is enabled in Bedrock console

### "Model Not Found" Error
- Ensure you're using the correct region
- Verify the model ID matches exactly: `us.anthropic.claude-sonnet-4-20250514-v1:0`

### "Credentials Not Found" Error
- Run `aws configure` to set up credentials
- Or set environment variables as described above
