"""
Script to check AWS credentials and Bedrock access configuration
"""

import boto3
from botocore.exceptions import NoCredentialsError, ClientError


def check_aws_credentials():
    """Check if AWS credentials are configured."""
    try:
        sts = boto3.client('sts')
        identity = sts.get_caller_identity()
        print("✓ AWS credentials are configured")
        print(f"  Account: {identity['Account']}")
        print(f"  User ARN: {identity['Arn']}")
        return True
    except NoCredentialsError:
        print("✗ AWS credentials not found")
        print("  Please run 'aws configure' or set environment variables")
        return False
    except Exception as e:
        print(f"✗ Error checking credentials: {e}")
        return False


def check_bedrock_access():
    """Check if Bedrock service is accessible."""
    try:
        bedrock = boto3.client('bedrock', region_name='us-east-1')
        print("✓ Bedrock service is accessible")
        return True
    except ClientError as e:
        print(f"✗ Error accessing Bedrock: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False


def main():
    """Run all checks."""
    print("Checking AWS Configuration for WealthPad")
    print("=" * 50)
    
    creds_ok = check_aws_credentials()
    print()
    
    if creds_ok:
        bedrock_ok = check_bedrock_access()
        print()
        
        if bedrock_ok:
            print("✓ All checks passed!")
            print("\nNext steps:")
            print("1. Enable Claude 4 Sonnet model access in Bedrock console")
            print("2. Run 'python agent.py' to test the financial coach")
        else:
            print("⚠ Bedrock access check failed")
            print("  Ensure your IAM user/role has bedrock:InvokeModel permission")
    else:
        print("⚠ Please configure AWS credentials first")
        print("  See AWS_SETUP.md for instructions")


if __name__ == "__main__":
    main()
