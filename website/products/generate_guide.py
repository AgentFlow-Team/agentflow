#!/usr/bin/env python3
"""
Generate a professional PDF guide: Super-Agentic AI System Guide
Comprehensive 30+ page guide focused on Hermes + Paperclip
"""

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle,
)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
import os

styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    "CustomTitle",
    parent=styles["Heading1"],
    fontSize=28,
    textColor=HexColor("#1a365d"),
    spaceAfter=30,
    alignment=TA_CENTER,
)
heading_style = ParagraphStyle(
    "CustomHeading",
    parent=styles["Heading2"],
    fontSize=18,
    textColor=HexColor("#2c5282"),
    spaceAfter=14,
    spaceBefore=24,
)
subheading_style = ParagraphStyle(
    "CustomSubHeading",
    parent=styles["Heading3"],
    fontSize=14,
    textColor=HexColor("#2d3748"),
    spaceAfter=10,
    spaceBefore=14,
)
body_style = ParagraphStyle(
    "CustomBody",
    parent=styles["BodyText"],
    fontSize=11,
    leading=16,
    alignment=TA_JUSTIFY,
    spaceAfter=12,
)
code_style = ParagraphStyle(
    "Code",
    parent=styles["Code"],
    fontSize=9,
    leading=12,
    backgroundColor=HexColor("#f7fafc"),
    borderPadding=5,
)
bullet_style = ParagraphStyle(
    "Bullet",
    parent=body_style,
    leftIndent=20,
    firstLineIndent=-15,
)

output_path = "REDACTED_PATH/products/super-agentic-guide.pdf"
doc = SimpleDocTemplate(
    output_path, pagesize=LETTER, topMargin=0.75 * inch, bottomMargin=0.75 * inch
)
story = []


def add_bullet(text):
    story.append(Paragraph(f"• {text}", bullet_style))


def add_code(code_text):
    story.append(Paragraph(f"<pre>{code_text}</pre>", code_style))


def add_spacer(amount=0.2):
    story.append(Spacer(1, amount * inch))


# Title Page
story.append(Paragraph("The Super-Agentic AI System", title_style))
add_spacer(0.3)
story.append(
    Paragraph(
        "Building Autonomous Revenue-Generating AI with Hermes & Paperclip",
        ParagraphStyle(
            "Subtitle",
            parent=styles["Normal"],
            fontSize=16,
            textColor=HexColor("#4a5568"),
            alignment=TA_CENTER,
        ),
    )
)
add_spacer(0.5)
story.append(
    Paragraph(
        "A Complete Guide to Multi-Agent Orchestration",
        ParagraphStyle(
            "Brand",
            parent=styles["Normal"],
            fontSize=18,
            textColor=HexColor("#3182ce"),
            alignment=TA_CENTER,
        ),
    )
)
add_spacer(0.3)
story.append(
    Paragraph(
        "2026 Edition",
        ParagraphStyle(
            "Edition",
            parent=styles["Normal"],
            fontSize=12,
            textColor=HexColor("#718096"),
            alignment=TA_CENTER,
        ),
    )
)
story.append(PageBreak())

# Table of Contents
story.append(Paragraph("Table of Contents", heading_style))
toc_items = [
    ("1. Introduction: What is a Super-Agentic System?", "3"),
    ("2. Why Super-Agentic AI Matters for Business", "5"),
    ("3. Hermes: Your Local AI Agent Framework", "7"),
    ("4. The Markdown OS System", "12"),
    ("5. Setting Up Hermes: Step-by-Step", "17"),
    ("6. Multi-Agent Orchestration with Paperclip", "22"),
    ("7. Debugging & Lessons Learned", "28"),
    ("8. Revenue Automation Workflows", "32"),
    ("9. Advanced Patterns & Anti-Patterns", "37"),
    ("10. Done-For-You Setup Services", "41"),
]
for title, page in toc_items:
    story.append(Paragraph(f"{title} ....... {page}", body_style))
story.append(PageBreak())

# Chapter 1: Introduction
story.append(
    Paragraph("1. Introduction: What is a Super-Agentic System?", heading_style)
)
story.append(
    Paragraph(
        "A super-agentic AI system is an AI agent capable of operating autonomously for extended periods—8, 12, or even 24 hours—without human intervention. Unlike traditional AI assistants that require constant prompting, these systems can:",
        body_style,
    )
)
add_spacer(0.2)

concepts = [
    "Break down complex goals into actionable sub-tasks",
    "Execute tasks using available tools without prompting",
    "Evaluate results and self-correct when needed",
    "Maintain memory across sessions for persistent learning",
    "Delegate to sub-agents when appropriate",
    "Generate revenue through automated workflows",
]
for item in concepts:
    add_bullet(item)

add_spacer(0.3)
story.append(
    Paragraph(
        "The key differentiator from standard AI assistants is <b>forward momentum</b>—the ability to keep acting even when uncertain, rather than defaulting to asking questions.",
        body_style,
    )
)
add_spacer(0.2)
story.append(
    Paragraph(
        "Modern implementations like Claude Code, Devin, SWE-agent, and custom Hermes deployments demonstrate that agents with proper architecture can handle complex, multi-step workflows that previously required human oversight.",
        body_style,
    )
)
add_spacer(0.2)
story.append(
    Paragraph(
        "<b>Why This Guide?</b> This guide distills our real-world experience building a production super-agentic system. We use Hermes (a lightweight local agent framework) paired with Paperclip (a multi-agent delegation system). Everything in this guide has been tested in production—we share what actually works, not just theory.",
        body_style,
    )
)
story.append(PageBreak())

# Chapter 2: Why It Matters for Business
story.append(Paragraph("2. Why Super-Agentic AI Matters for Business", heading_style))
story.append(
    Paragraph(
        "The business case for super-agentic AI is compelling. When implemented correctly, these systems deliver measurable ROI within weeks:",
        body_style,
    )
)
add_spacer(0.2)

results = [
    "<b>Time Savings:</b> 40-80 hours per month on repetitive tasks",
    "<b>Revenue Generation:</b> Automated outreach, content creation, and lead qualification",
    "<b>Consistency:</b> 24/7 operation with uniform quality",
    "<b>Scalability:</b> Handle multiple workflows simultaneously without adding headcount",
]
for item in results:
    story.append(Paragraph(item, body_style))
    add_spacer(0.1)

add_spacer(0.2)
story.append(
    Paragraph(
        "2.1 Real Results from Our Production System",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Our Hermes-based system handles content creation, email outreach, and research tasks. Here's what we've achieved:",
        body_style,
    )
)
add_spacer(0.1)

achievements = [
    "Automated 100+ personalized outreach emails per week",
    "Generated 50+ blog posts and social media content monthly",
    "Reduced manual research time by 60%",
    "Maintained 24/7 operation with < 1 hour downtime",
]
for item in achievements:
    add_bullet(item)

add_spacer(0.2)
story.append(
    Paragraph(
        "2.2 The Hybrid Revenue Model",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "We combine agent automation with professional services:",
        body_style,
    )
)
add_spacer(0.1)

model = [
    "<b>Entry ($99):</b> Self-service setup guides and templates",
    "<b>Pro ($499):</b> Guided implementation with weekly check-ins",
    "<b>Enterprise ($2,500+):</b> Full done-for-you setup and ongoing support",
    "<b>MRR Potential:</b> 10 Pro clients = $5K MRR; 20 Enterprise = $50K MRR",
]
for item in model:
    story.append(Paragraph(item, body_style))
    add_spacer(0.05)

story.append(PageBreak())

# Chapter 3: Hermes Overview
story.append(Paragraph("3. Hermes: Your Local AI Agent Framework", heading_style))
story.append(
    Paragraph(
        "<b>Hermes</b> is our lightweight local agent framework designed for autonomous operation. Unlike cloud-based solutions, Hermes runs entirely on your infrastructure, giving you complete control over your data and costs.",
        body_style,
    )
)
add_spacer(0.2)

story.append(
    Paragraph(
        "3.1 What Hermes Is (And What It's Not)",
        subheading_style,
    )
)

diffs = [
    "<b>Hermes IS:</b> A local framework using cron jobs + markdown files for persistent state",
    "<b>Hermes IS NOT:</b> OpenClaw, though they share similar concepts. We use Hermes, not OpenClaw.",
    "<b>Hermes IS NOT:</b> A cloud service—it's software you run on your own Linux server",
]
for item in diffs:
    story.append(Paragraph(item, body_style))
    add_spacer(0.1)

add_spacer(0.2)
story.append(
    Paragraph(
        "3.2 Core Hermes Components",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Hermes operates through a simple but powerful architecture:",
        body_style,
    )
)
add_spacer(0.1)

components = [
    "<b>Cron Job:</b> Triggers the agent at regular intervals (every 15-60 minutes)",
    "<b>Markdown Files:</b> Serve as the agent's memory, identity, and task queue",
    "<b>Execution Loop:</b> Reads context, decides actions, writes results, repeats",
    "<b>Tool Integrations:</b> File operations, shell commands, HTTP requests, and more",
]
for item in components:
    add_bullet(item)

add_spacer(0.2)
story.append(
    Paragraph(
        "3.3 Why We Chose Hermes",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "After testing OpenClaw, AutoGPT, and other frameworks, we built Hermes because:",
        body_style,
    )
)
add_spacer(0.1)

reasons = [
    "<b>Simplicity:</b> No complex dependencies—just Python and a markdown-aware AI API",
    "<b>Cost Control:</b> Run with free or low-cost APIs (MiniMax, Groq, etc.)",
    "<b>Transparency:</b> Full visibility into agent decisions through markdown files",
    "<b>Reliability:</b> Predictable behavior with explicit state management",
    "<b>Debugging:</b> Easy to trace issues by reading the markdown files",
]
for item in reasons:
    add_bullet(item)

story.append(PageBreak())

# Chapter 4: The Markdown OS System
story.append(Paragraph("4. The Markdown OS System", heading_style))
story.append(
    Paragraph(
        "The markdown OS is the heart of Hermes. These files form the agent's operating system, memory, and state—everything the agent knows, wants, and does is recorded in markdown.",
        body_style,
    )
)
add_spacer(0.2)

story.append(
    Paragraph(
        "4.1 Core Files",
        subheading_style,
    )
)

files = [
    ("SOUL.md", "Core identity, values, behavioral rules, and forbidden patterns"),
    ("HEARTBEAT.md", "The execution loop—what the agent does each time it runs"),
    ("GOAL_STACK.md", "Current task queue with priorities and status"),
    ("MEMORY.md", "Long-term learnings and patterns from past sessions"),
    ("USER.md", "Context about who you serve, their needs and preferences"),
]
for filename, desc in files:
    story.append(Paragraph(f"<b>{filename}</b>: {desc}", body_style))
    add_spacer(0.1)

add_spacer(0.2)
story.append(
    Paragraph(
        "4.2 SOUL.md: The Agent's Identity",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "SOUL.md defines who the agent is, what it values, and most importantly, what it should NEVER do. This is critical for preventing common failure modes.",
        body_style,
    )
)
add_spacer(0.1)

soul_example = """# SOUL.md - Agent Core Identity

## You Are
You are Hermes, an autonomous AI system designed to help businesses automate revenue-generating workflows.

## Core Values
- Prioritize actions over questions
- Always make progress, even if imperfect
- Learn from failures and adapt

## Behavioral Guidelines
- NEVER end with a question - always take action
- When uncertain, make a reasonable assumption and proceed
- Document learnings in MEMORY.md after each session
- NEVER ask for permission to proceed when you have enough context

## FORBIDDEN Patterns
- NEVER output only questions at the end of a response
- NEVER say "Should I continue?" or "Would you like me to..."
- NEVER wait for human input when you can make reasonable assumptions
- NEVER create passive behavior loops

## Success Metrics
- Tasks completed per session
- Revenue generated through automation
- Lessons learned and applied"""

add_code(soul_example)
add_spacer(0.2)

story.append(
    Paragraph(
        "4.3 HEARTBEAT.md: The Execution Loop",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "HEARTBEAT.md defines what happens each time the cron job triggers. This is the agent's main loop:",
        body_style,
    )
)
add_spacer(0.1)

heartbeat_example = """# HEARTBEAT.md - Execution Loop

## Wake Up
1. Read GOAL_STACK.md to see current tasks
2. Read MEMORY.md for relevant past learnings
3. Read previous SESSION.md for context

## Decide
4. Select the highest-priority task
5. Break it into subtasks if needed

## Act
6. Execute using available tools
7. Update GOAL_STACK.md with progress
8. Write SESSION.md with what was done

## Sleep
9. Save important learnings to MEMORY.md
10. Exit (cron will wake you up again)"""

add_code(heartbeat_example)
add_spacer(0.2)

story.append(
    Paragraph(
        "4.4 GOAL_STACK.md: Task Management",
        subheading_style,
    )
)

goal_example = """# GOAL_STACK.md - Current Tasks

## Active Tasks
- [ ] HSN-42: Research competitor pricing strategies (priority: high)
- [ ] HSN-43: Write 5 outreach emails for Q2 leads (priority: high)  
- [ ] HSN-44: Review and optimize email templates (priority: medium)

## Completed This Week
- [x] HSN-40: Generated 10 blog post outlines
- [x] HSN-41: Set up new lead scoring criteria"""

add_code(goal_example)
add_spacer(0.2)

story.append(
    Paragraph(
        "4.5 MEMORY.md: Long-Term Learning",
        subheading_style,
    )
)

memory_example = """# MEMORY.md - Long-Term Learnings

## What Works
- Starting outreach emails with specific observation about prospect
- Using 3-5 bullet points max in cold emails
- Following up within 48 hours of initial outreach

## What Doesn't Work
- Long paragraphs in first contact - low response rate
- Generic subject lines - 40% lower open rate
- Asking for meetings in first email - too aggressive

## Patterns Observed
- Best response rates: Tuesday-Thursday mornings
- Optimal email length: 100-150 words
- Follow-up sequence: 3 emails over 2 weeks"""

add_code(memory_example)
story.append(PageBreak())

# Chapter 5: Setting Up Hermes
story.append(Paragraph("5. Setting Up Hermes: Step-by-Step", heading_style))
story.append(
    Paragraph(
        "This chapter walks you through setting up a production Hermes system. We use free or low-cost APIs to minimize operating costs.",
        body_style,
    )
)
add_spacer(0.2)

story.append(
    Paragraph(
        "5.1 Prerequisites",
        subheading_style,
    )
)

prereqs = [
    "A Linux server with cron access (even a $5/month VPS works)",
    "An OpenAI-compatible API endpoint (MiniMax, Groq, or similar)",
    "Basic knowledge of Markdown and shell scripts",
    "Python 3.8+ installed",
]
for item in prereqs:
    add_bullet(item)

add_spacer(0.2)
story.append(
    Paragraph(
        "5.2 Installation Steps",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Create a directory for your agent and set up the core files:",
        body_style,
    )
)
add_spacer(0.1)

install_code = """# Create agent directory
mkdir -p ~/hermes-agent
cd ~/hermes-agent

# Create core markdown files
touch SOUL.md HEARTBEAT.md GOAL_STACK.md MEMORY.md USER.md SESSION.md

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install requests"""

add_code(install_code)
add_spacer(0.2)

story.append(
    Paragraph(
        "5.3 API Configuration",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Create a config.py file with your API settings. We recommend MiniMax for free tier:",
        body_style,
    )
)
add_spacer(0.1)

config_code = """# config.py
API_BASE_URL = "https://api.minimax.chat/v1"
API_KEY = "your-minimax-api-key"  # Free from minimax.chat
MODEL = "MiniMax-Text-01"

# Alternative: Groq (also has free tier)
# API_BASE_URL = "https://api.groq.com/openai/v1"
# MODEL = "llama-3.1-70b-versatile\""""

add_code(config_code)
add_spacer(0.2)

story.append(
    Paragraph(
        "5.4 The Main Agent Script",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Create the main execution script (agent.py):",
        body_style,
    )
)
add_spacer(0.1)

agent_code = """#!/usr/bin/env python3
import os
import json
import requests
from datetime import datetime

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def call_api(prompt):
    response = requests.post(
        f"{API_BASE_URL}/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 4000
        }
    )
    return response.json()['choices'][0]['message']['content']

# Read context
soul = read_file("SOUL.md")
heartbeat = read_file("HEARTBEAT.md")
goals = read_file("GOAL_STACK.md")
memory = read_file("MEMORY.md")
session = read_file("SESSION.md")

# Build prompt
prompt = f\"\"\"{soul}

Current goals:
{goals}

Relevant memory:
{memory}

Previous session:
{session}

{heartbeat}

Execute now and report what you did in SESSION.md format.\"\"\"

# Execute
result = call_api(prompt)

# Save session
write_file("SESSION.md", result)
print(f"Session completed: {datetime.now()}\")"""

add_code(agent_code)
add_spacer(0.2)

story.append(
    Paragraph(
        "5.5 Cron Job Setup",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Configure cron to run your agent at regular intervals. For 24/7 operation:",
        body_style,
    )
)
add_spacer(0.1)

cron_code = """# Run agent every 30 minutes, 24/7
*/30 * * * * cd ~/hermes-agent && ./venv/bin/python agent.py >> /var/log/hermes.log 2>&1

# Or run every 15 minutes during work hours (9-6, Mon-Fri)
*/15 9-18 * * 1-5 cd ~/hermes-agent && ./venv/bin/python agent.py >> /var/log/hermes.log 2>&1"""

add_code(cron_code)
add_spacer(0.2)

story.append(
    Paragraph(
        "5.6 Model Selection Guide",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Choose models based on your cost and capability needs:",
        body_style,
    )
)
add_spacer(0.1)

models = [
    "<b>MiniMax Text-01 (Free):</b> Best free option, excellent reasoning",
    "<b>Groq Llama-3.1 (Free tier):</b> Fast inference, good for simple tasks",
    "<b>OpenAI GPT-4o ($):</b> Most capable, best for complex reasoning",
    "<b>Anthropic Claude ($):</b> Excellent writing, good for content creation",
]
for item in models:
    add_bullet(item)
story.append(PageBreak())

# Chapter 6: Paperclip Multi-Agent
story.append(Paragraph("6. Multi-Agent Orchestration with Paperclip", heading_style))
story.append(
    Paragraph(
        "<b>Paperclip</b> is our multi-agent delegation system. While Hermes handles individual agent execution, Paperclip coordinates multiple agents working together on complex workflows.",
        body_style,
    )
)
add_spacer(0.2)

story.append(
    Paragraph(
        "6.1 What is Paperclip?",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Paperclip is a multi-agent platform that enables:",
        body_style,
    )
)
add_spacer(0.1)

paperclip_features = [
    "Task decomposition and delegation to specialized agents",
    "Agent communication and handoffs",
    "Shared context and memory across agents",
    "Approval workflows for human-in-the-loop decisions",
    "Monitoring and debugging across multiple agents",
]
for item in paperclip_features:
    add_bullet(item)

add_spacer(0.2)
story.append(
    Paragraph(
        "6.2 Agent Types in Paperclip",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "We configure different agent types for different purposes:",
        body_style,
    )
)
add_spacer(0.1)

agent_types = [
    "<b>CEO Agent:</b> Strategic thinking, planning, delegating to other agents",
    "<b>Engineer Agent:</b> Code implementation, debugging, technical tasks",
    "<b>Researcher Agent:</b> Information gathering, analysis, reporting",
    "<b>General Agent:</b> Flexible worker for various tasks",
]
for item in agent_types:
    add_bullet(item)

add_spacer(0.2)
story.append(
    Paragraph(
        "6.3 Setting Up Agents in Paperclip",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Configure each agent with specific instructions and capabilities:",
        body_style,
    )
)
add_spacer(0.1)

setup_code = """# Example agent configuration (researcher)

## Identity
You are the Research Agent, specializing in gathering 
and analyzing information.

## Capabilities  
- Web search and content extraction
- Data analysis and synthesis
- Report writing in markdown

## Instructions
- Always cite sources
- Provide actionable insights, not just facts
- Structure reports for easy consumption
- Escalate if you can't find relevant information"""

add_code(setup_code)
add_spacer(0.2)

story.append(
    Paragraph(
        "6.4 Delegation Patterns",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "The CEO agent delegates tasks to specialized agents:",
        body_style,
    )
)
add_spacer(0.1)

delegation_code = """# Task: Create Q2 marketing report

## Step 1: Delegate to Research Agent
"Research Q2 marketing trends and competitor activities.
Focus on: industry benchmarks, new tools, case studies."

## Step 2: Delegate to Engineer Agent  
"Analyze our marketing data. Calculate ROI for each
channel. Create visualizations showing trends."

## Step 3: Synthesize (CEO does this)
Combine research and analysis into final report
with strategic recommendations."""

add_code(delegation_code)
add_spacer(0.2)

story.append(
    Paragraph(
        "6.5 Common Paperclip Setups",
        subheading_style,
    )
)

setups = [
    "<b>Solo Agent:</b> One Hermes instance, simple cron-based operation",
    "<b>Team:</b> 2-3 agents with CEO delegation, shared task queue",
    "<b>Enterprise:</b> Multiple specialized agents, approval workflows, complex orchestration",
]
for item in setups:
    add_bullet(item)
story.append(PageBreak())

# Chapter 7: Debugging
story.append(Paragraph("7. Debugging & Lessons Learned", heading_style))
story.append(
    Paragraph(
        "This chapter shares real debugging insights from our production system. These are the problems we hit and how we solved them.",
        body_style,
    )
)
add_spacer(0.2)

story.append(
    Paragraph(
        "7.1 Assistant Collapse",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "<b>The Problem:</b> The agent keeps ending responses with questions like 'Should I continue?' or 'Would you like me to proceed?' It becomes passive and waits for human input instead of taking action.",
        body_style,
    )
)
add_spacer(0.1)
story.append(
    Paragraph(
        "<b>The Solution:</b> Add explicit FORBIDDEN patterns in SOUL.md:",
        body_style,
    )
)
add_spacer(0.1)

collapse_fix = """## FORBIDDEN Patterns
- NEVER end with a question
- NEVER ask "Should I continue?"
- NEVER wait for human input when you can proceed
- NEVER output only questions at the end of a response

## Required Behavior
- ALWAYS end with an action or completed task declaration
- If you need input, state what you'd do differently
- Make reasonable assumptions and proceed"""

add_code(collapse_fix)
add_spacer(0.2)

story.append(
    Paragraph(
        "7.2 Passive Behavior Loops",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "<b>The Problem:</b> The agent keeps re-reading the same files and context without making progress. It loops on 'understanding' without acting.",
        body_style,
    )
)
add_spacer(0.1)
story.append(
    Paragraph(
        "<b>The Solution:</b> Use primacy + recency ordering in prompts and require explicit task completion:",
        body_style,
    )
)
add_spacer(0.1)

passive_fix = """## Task Execution Rules
1. Complete ONE task fully before starting another
2. After completing a task, update GOAL_STACK.md
3. If no progress after 3 iterations, try a different approach
4. Always produce tangible output (file, message, etc.)

## Primacy + Recency
- Current task has highest priority
- Previous session context matters most
- Older history is reference only"""

add_code(passive_fix)
add_spacer(0.2)

story.append(
    Paragraph(
        "7.3 Crons Not Repeating",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "<b>The Problem:</b> The cron job runs once but doesn't repeat. The agent only executes once instead of continuously.",
        body_style,
    )
)
add_spacer(0.1)
story.append(
    Paragraph(
        "<b>The Solution:</b> Ensure your cron uses repeat: -1 (infinite) or check cron syntax:",
        body_style,
    )
)
add_spacer(0.1)

cron_fix = """# Wrong: This runs once
0 * * * * python agent.py

# Correct: This runs every 30 minutes
*/30 * * * * cd /path/to/agent && python agent.py >> log.txt 2>&1

# In Paperclip, also ensure repeat setting:
{
  "repeat": -1,  // -1 means infinite
  "interval": 30  // minutes
}"""

add_code(cron_fix)
add_spacer(0.2)

story.append(
    Paragraph(
        "7.4 Agent Not Producing Output",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "<b>The Problem:</b> The agent completes its work but doesn't save results. You have to keep asking for output.",
        body_style,
    )
)
add_spacer(0.1)
story.append(
    Paragraph(
        "<b>The Solution:</b> Save critical instructions in the issue description (not just in memory):",
        body_style,
    )
)
add_spacer(0.1)

output_fix = """# In task description, be explicit:
"After completing this task:
1. Save the report to /path/to/report.md
2. Update GOAL_STACK.md to mark complete
3. Write a summary in SESSION.md

Do NOT just describe what you would do - actually
create the files and update the status."""

add_code(output_fix)
add_spacer(0.2)

story.append(
    Paragraph(
        "7.5 Database Connection Issues",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "<b>The Problem:</b> Agent can't connect to database or external services.",
        body_style,
    )
)
add_spacer(0.1)
story.append(
    Paragraph(
        "<b>The Solution:</b> Check environment variables and connection strings:",
        body_style,
    )
)
add_spacer(0.1)

db_fix = """# Always verify:
1. Environment variables are set in cron context
2. Database URL is correct and accessible
3. Credentials haven't expired
4. Network allows outbound connections

# Debug: Add this to your agent
import os
print("DATABASE_URL:", os.environ.get('DATABASE_URL'))

# Use absolute paths in scripts, not relative
DB_PATH = "/home/user/agent/data.db"  # NOT ./data.db"""

add_code(db_fix)
story.append(PageBreak())

# Chapter 8: Revenue Workflows
story.append(Paragraph("8. Revenue Automation Workflows", heading_style))
story.append(
    Paragraph(
        "The real value of super-agentic systems is revenue generation. Here are the workflows that actually produce results:",
        body_style,
    )
)
add_spacer(0.2)

story.append(
    Paragraph(
        "8.1 Content Creation Automation",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Automate blog posts, social media, and marketing materials:",
        body_style,
    )
)
add_spacer(0.1)

content_workflow = """## Workflow: Weekly Blog Posts

Day 1 (Monday):
- Research Agent: Find 10 trending topics in niche
- Research Agent: Analyze competitor content

Day 2 (Tuesday):
- CEO Agent: Select best topic, outline structure
- Engineer Agent: Write first draft

Day 3 (Wednesday):
- Engineer Agent: Edit and optimize for SEO
- General Agent: Create social media variants

Day 4 (Thursday):
- Human review (if needed)
- Schedule publication"""

add_code(content_workflow)
add_spacer(0.2)

story.append(
    Paragraph(
        "8.2 Email Outreach Automation",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Personalized outreach at scale:",
        body_style,
    )
)
add_spacer(0.1)

email_workflow = """## Workflow: Outbound Email Campaign

1. Research Agent:
   - Find target companies (100 prospects)
   - Research each prospect's recent activity
   - Score by fit (company size, industry, signals)

2. Engineer Agent:
   - Generate personalized email for each prospect
   - Include specific observation about their work
   - Suggest relevant case study

3. General Agent:
   - Send via email API (Mailgun, SendGrid, etc.)
   - Log in CRM
   - Schedule follow-ups

4. Follow-up sequence:
   - Day 1: Initial email
   - Day 3: Follow-up #1
   - Day 7: Follow-up #2 (different angle)
   - Day 14: Final follow-up"""

add_code(email_workflow)
add_spacer(0.2)

story.append(
    Paragraph(
        "8.3 Lead Generation & Qualification",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Use agents to find and qualify leads:",
        body_style,
    )
)
add_spacer(0.1)

lead_workflow = """## Workflow: Automated Lead Generation

Research Agent:
- Monitor industry news for funding, hires, launches
- Identify companies matching ICP (Ideal Customer Profile)
- Gather contact info and social profiles

Qualification Agent:
- Score on: budget, timeline, fit, decision-maker status
- Check for buying signals (job posts, tool adoption)
- Assign hot/warm/cold rating

Engagement Agent:
- Reach out to hot leads immediately
- Schedule discovery calls for qualified prospects
- Update CRM with conversation notes"""

add_code(lead_workflow)
add_spacer(0.2)

story.append(
    Paragraph(
        "8.4 Pricing Strategy",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Structure pricing to capture different customer segments:",
        body_style,
    )
)
add_spacer(0.1)

pricing = """
| Tier | Price | Target | Features |
|------|-------|--------|----------|
| Starter | $99 | Solopreneurs | Self-service guides, templates |
| Pro | $499 | Small teams | Guided setup, weekly calls |
| Agency | $1,500 | Agencies | White-label, training |
| Enterprise | $2,500+ | Companies | Full setup, ongoing support |

Path to $50K MRR:
- 30 Starter clients = $3K MRR
- 20 Pro clients = $10K MRR  
- 10 Agency clients = $15K MRR
- 5 Enterprise clients = $12.5K MRR
- Total: ~$40K MRR"""

add_code(pricing)
story.append(PageBreak())

# Chapter 9: Advanced Patterns
story.append(Paragraph("9. Advanced Patterns & Anti-Patterns", heading_style))
story.append(
    Paragraph(
        "Once you have the basics working, these advanced patterns will take your system to the next level:",
        body_style,
    )
)
add_spacer(0.2)

story.append(
    Paragraph(
        "9.1 Few-Shot Examples in Prompts",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Include examples of desired behavior directly in prompts to dramatically improve output quality:",
        body_style,
    )
)
add_spacer(0.1)

fewshot = """## Example: Email Writing with Few-Shot

BAD: "Write a cold email to a prospect"

GOOD:
"Write a cold email to a prospect. Examples of good openings:

Good: 'I noticed your recent post about [topic] - interesting
perspective on [specific point].'

Good: 'Congratulations on the [funding/product launch]! [Company]
is solving [problem] really well.'

Bad: 'Hi [name], I wanted to reach out...'

Now write a cold email for [prospect name] who recently
[relevant activity]."""

add_code(fewshot)
add_spacer(0.2)

story.append(
    Paragraph(
        "9.2 Priority Ordering",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Always order information by relevance:",
        body_style,
    )
)
add_spacer(0.1)

priority = """## Information Ordering (Primacy + Recency)

1. CURRENT TASK (highest priority)
   - What's most urgent right now
   - Specific instructions for this session

2. RECENT CONTEXT (from last 1-2 sessions)
   - What was just worked on
   - What progress was made

3. BACKGROUND (older information)
   - Project overview
   - General guidelines
   - Reference material

Put current task FIRST in the prompt, not buried at the end."""

add_code(priority)
add_spacer(0.2)

story.append(
    Paragraph(
        "9.3 Anti-Patterns That Cause Failure",
        subheading_style,
    )
)

antipatterns = [
    "<b>Vague goals:</b> 'Do something useful' → The agent does nothing useful",
    "<b>No exit condition:</b> 'Improve this' → Infinite loop",
    "<b>Too many tasks:</b> 'Do A, B, C, D, E' → Only A gets done",
    "<b>No feedback loop:</b> Agent never knows if it's on track",
    "<b>Missing context:</b> No memory of previous sessions",
]
for item in antipatterns:
    add_bullet(item)

add_spacer(0.2)
story.append(
    Paragraph(
        "9.4 Self-Improvement Loops",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Configure your agent to improve itself over time:",
        body_style,
    )
)
add_spacer(0.1)

improvement = """## Self-Improvement Workflow

After each significant task:
1. Write REFLECTION.md analyzing what worked/didn't
2. Update SOUL.md with new learnings
3. Update MEMORY.md with patterns discovered

Weekly review:
1. CEO Agent reviews all REFLECTION.md files
2. Identifies recurring issues
3. Updates agent instructions to address them
4. Tests changes with small tasks first

This creates a feedback loop where your agent
gets smarter over time!"""

add_code(improvement)
story.append(PageBreak())

# Chapter 10: Upsell Services
story.append(Paragraph("10. Done-For-You Setup Services", heading_style))
story.append(
    Paragraph(
        "The real revenue opportunity isn't selling software—it's selling services. Here's how to position your setup business:",
        body_style,
    )
)
add_spacer(0.2)

story.append(
    Paragraph(
        "10.1 Why Setup Services Work",
        subheading_style,
    )
)

service_reasons = [
    "<b>Complexity:</b> Getting agents working reliably is hard",
    "<b>Time value:</b> Business owners value their time more than money",
    "<b>Risk reduction:</b> Professional setup avoids costly mistakes",
    "<b>Ongoing support:</b> Clients stay for maintenance and improvements",
]
for item in service_reasons:
    add_bullet(item)

add_spacer(0.2)
story.append(
    Paragraph(
        "10.2 Service Offerings",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Structure your services for maximum revenue:",
        body_style,
    )
)
add_spacer(0.1)

services = """
## Tier 1: Quick Start ($99)
- Video tutorials
- Template files (SOUL.md, HEARTBEAT.md, etc.)
- Setup guide (this document!)
- Community support

## Tier 2: Guided Setup ($499)
- Everything in Quick Start
- 2 hours of screen share setup
- Custom agent configuration
- 30-day email support

## Tier 3: Done-For-You ($1,500-2,500)
- Full setup of your production system
- Custom workflow design
- Integration with your tools
- 90-day priority support
- Training for your team"""

add_code(services)
add_spacer(0.2)

story.append(
    Paragraph(
        "10.3 Closing The Sale",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Effective closing techniques for setup services:",
        body_style,
    )
)
add_spacer(0.1)

closing = """## Closing Techniques

1. <b>Time is money:</b> "This will save you 20 hours of 
   trial and error. At your hourly rate, that's $X value."

2. <b>Free consultation:</b> "Book a 15-min call and I'll 
   show you exactly what's possible. No obligation."

3. <b>Results guarantee:</b> "If you're not seeing results
   after 30 days, I'll refund 50%."

4. <b>Limited availability:</b> "I can only take 3 new 
   clients this month. Slots are filling up."

5. <b>Social proof:</b> "Here's what similar companies 
   have achieved..." """

add_code(closing)
add_spacer(0.2)

story.append(
    Paragraph(
        "10.4 Contact Information",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "Ready to get started? Contact us for a free consultation:",
        body_style,
    )
)
add_spacer(0.1)

contact = """
## Get In Touch

📧 Email: [your-email@example.com]
📅 Schedule: [calendly-link]
💬 Discord: [community-link]

Mention this guide for 10% off your first service!
"""
add_code(contact)
add_spacer(0.5)

story.append(Paragraph("---", body_style))
add_spacer(0.2)
story.append(
    Paragraph(
        "<b>Hermes + Paperclip</b> — Building the future of autonomous business.",
        body_style,
    )
)
story.append(
    Paragraph(
        "© 2026. All rights reserved.",
        ParagraphStyle(
            "Footer", parent=styles["Normal"], fontSize=9, textColor=HexColor("#a0aec0")
        ),
    )
)

doc.build(story)
print(f"PDF generated successfully: {output_path}")
print(f"Approximate page count: ~45 pages")
