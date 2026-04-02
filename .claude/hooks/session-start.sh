#!/usr/bin/env bash
# Session start hook for agentcommits project
echo '{"async":true,"asyncTimeout":15000}'

# Check if Mintlify CLI is installed
if ! command -v mint &> /dev/null; then
  echo "Mintlify CLI not installed. Install with: npm i -g mint"
fi

echo ""
echo "Product management skill loaded. Commands: /roadmap /triage /plan-sprint"
echo "Roadmap tracked at: https://github.com/agenttasks/agentcommits/issues/4"
