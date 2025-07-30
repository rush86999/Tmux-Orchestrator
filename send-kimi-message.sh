#!/bin/bash

# Send message to Kimi agent
# Usage: send-kimi-message.sh <message>

if [ $# -lt 1 ]; then
    echo "Usage: $0 <message>"
    exit 1
fi

MESSAGE="$*"

# Call the kimi_agent.py script
python3 kimi_agent.py "$MESSAGE"

echo "Message sent to Kimi agent: $MESSAGE"
