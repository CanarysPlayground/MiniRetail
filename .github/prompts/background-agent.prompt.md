---
name: background-agent
description: Describe when to use this prompt
---
You are a background agent.
Task:
Add a utility script that deletes posts older than 30 days.
Rules:

Do not touch API code
Create a standalone Python script
Reuse database connection
No scheduling logic required

Output:

backend/cleanup_old_posts.py


This demonstrates parallel/autonomous agent work without touching your API or UI files.

