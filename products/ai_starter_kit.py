#!/usr/bin/env python3
"""
Generate a professional PDF lead magnet: AI Automation Starter Kit
FREE resource to capture emails for the nurture sequence
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
    spaceAfter=15,
    spaceBefore=25,
)
subheading_style = ParagraphStyle(
    "CustomSubHeading",
    parent=styles["Heading3"],
    fontSize=14,
    textColor=HexColor("#2d3748"),
    spaceAfter=10,
    spaceBefore=15,
)
body_style = ParagraphStyle(
    "CustomBody",
    parent=styles["BodyText"],
    fontSize=11,
    leading=18,
    alignment=TA_JUSTIFY,
    spaceAfter=12,
)
bullet_style = ParagraphStyle(
    "Bullet",
    parent=styles["BodyText"],
    fontSize=11,
    leading=18,
    alignment=TA_LEFT,
    spaceAfter=8,
)

output_path = "REDACTED_PATH/products/ai-starter-kit.pdf"
doc = SimpleDocTemplate(
    output_path, pagesize=LETTER, topMargin=0.75 * inch, bottomMargin=0.75 * inch
)
story = []

# COVER PAGE
story.append(Paragraph("AI Automation Starter Kit", title_style))
story.append(Spacer(1, 0.3 * inch))
story.append(
    Paragraph(
        "A Practical Guide to Getting Started with AI in Your Business",
        ParagraphStyle(
            "Subtitle",
            parent=styles["Normal"],
            fontSize=16,
            textColor=HexColor("#4a5568"),
            alignment=TA_CENTER,
        ),
    )
)
story.append(Spacer(1, 0.8 * inch))
story.append(
    Paragraph(
        "AgentFlow",
        ParagraphStyle(
            "Brand",
            parent=styles["Normal"],
            fontSize=24,
            textColor=HexColor("#3182ce"),
            alignment=TA_CENTER,
        ),
    )
)
story.append(Spacer(1, 0.3 * inch))
story.append(
    Paragraph(
        "Free Download — 2026 Edition",
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

# TABLE OF CONTENTS
story.append(Paragraph("What's Inside", heading_style))
story.append(Spacer(1, 0.2 * inch))
toc_items = [
    "What is AI Automation?",
    "3 Signs Your Business Needs AI",
    "Top 5 Free AI Tools You Can Use Today",
    "How to Calculate Your Automation ROI",
    "Common Mistakes When Implementing AI",
    "Next Steps",
]
for i, title in enumerate(toc_items, 1):
    story.append(Paragraph(f"{i}. {title}", body_style))
    story.append(Spacer(1, 0.1 * inch))
story.append(PageBreak())

# CHAPTER 1: What is AI Automation?
story.append(Paragraph("1. What is AI Automation?", heading_style))
story.append(
    Paragraph(
        "AI automation combines artificial intelligence with software tools to handle tasks that traditionally required human effort. Unlike simple automation (which follows fixed rules), AI automation can make decisions, learn from patterns, and adapt to new situations.",
        body_style,
    )
)
story.append(Spacer(1, 0.2 * inch))
story.append(
    Paragraph(
        "Think of it as adding a smart assistant to your team—one that never sleeps, never takes breaks, and gets better at its job over time.",
        body_style,
    )
)
story.append(Spacer(1, 0.3 * inch))
story.append(Paragraph("Key Differences:", subheading_style))
differences = [
    "Traditional automation follows exact rules; AI learns and adapts",
    "Traditional automation handles repetitive tasks; AI handles judgment calls",
    "Traditional automation needs manual updates; AI improves on its own",
]
for item in differences:
    story.append(Paragraph(f"• {item}", bullet_style))
story.append(Spacer(1, 0.2 * inch))
story.append(
    Paragraph(
        "The result? Your team focuses on high-value creative work while AI handles the busywork.",
        body_style,
    )
)
story.append(PageBreak())

# CHAPTER 2: 3 Signs Your Business Needs AI
story.append(Paragraph("2. 3 Signs Your Business Needs AI", heading_style))
story.append(
    Paragraph(
        "Not sure if AI is right for your business? Here are three clear indicators:",
        body_style,
    )
)
story.append(Spacer(1, 0.2 * inch))

story.append(
    Paragraph("Sign #1: You're Doing the Same Task Repeatedly", subheading_style)
)
story.append(
    Paragraph(
        "If you or your team spend hours on repetitive tasks—like sending follow-up emails, updating spreadsheets, or categorizing customer messages—AI can handle this in seconds.",
        body_style,
    )
)
story.append(Spacer(1, 0.1 * inch))
story.append(
    Paragraph(
        "<b>Quick win:</b> Track how much time you spend on one recurring task per week. If it's more than 2 hours, automation could save you 80% of that time.",
        body_style,
    )
)
story.append(Spacer(1, 0.3 * inch))

story.append(
    Paragraph(
        "Sign #2: You're Missing Opportunities Because You're Too Busy",
        subheading_style,
    )
)
story.append(
    Paragraph(
        "When your team is buried in operational work, they can't focus on growth. If you've ever thought 'if I only had more time, I could...'—that's AI's cue to step in.",
        body_style,
    )
)
story.append(Spacer(1, 0.1 * inch))
story.append(
    Paragraph(
        "<b>Quick win:</b> List the 3 things you've been putting off for weeks. These are prime candidates for AI automation.",
        body_style,
    )
)
story.append(Spacer(1, 0.3 * inch))

story.append(Paragraph("Sign #3: Your Customers Are Waiting", subheading_style))
story.append(
    Paragraph(
        "Slow response times drive customers away. If you're not replying to inquiries within a few hours, you're losing business. AI-powered responses can cut wait times to minutes.",
        body_style,
    )
)
story.append(Spacer(1, 0.1 * inch))
story.append(
    Paragraph(
        "<b>Quick win:</b> Check your average response time this week. If it's over 4 hours, AI can help you get it under 30 minutes.",
        body_style,
    )
)
story.append(PageBreak())

# CHAPTER 3: Top 5 Free AI Tools
story.append(Paragraph("3. Top 5 Free AI Tools You Can Use Today", heading_style))
story.append(
    Paragraph(
        "You don't need a big budget to start with AI. Here are five free tools that can immediately impact your business:",
        body_style,
    )
)
story.append(Spacer(1, 0.2 * inch))

tools = [
    (
        "ChatGPT (Free Tier)",
        "Great for drafting emails, generating content ideas, and answering customer questions. 10-15 million monthly users can't be wrong.",
    ),
    (
        "Google Bard / Gemini",
        "Excellent for research, summarizing documents, and pulling information from your files. Integrates well with Google Workspace.",
    ),
    (
        "Canva AI (Magic Write)",
        "Create social media posts, presentations, and marketing materials in minutes. No design skills needed.",
    ),
    (
        "Zapier Free Tier",
        "Connect your apps and automate workflows. The free tier includes 100 tasks per month—perfect for testing.",
    ),
    (
        "Notion AI",
        "Summarize meetings, draft documents, and organize notes. The free version gives you generous AI credits.",
    ),
]
for tool_name, description in tools:
    story.append(Paragraph(f"<b>{tool_name}</b>", bullet_style))
    story.append(Paragraph(description, body_style))
    story.append(Spacer(1, 0.15 * inch))

story.append(
    Paragraph(
        "<b>Pro tip:</b> Start with ONE tool. Master it, then add another. Trying to implement everything at once leads to nothing getting used.",
        body_style,
    )
)
story.append(PageBreak())

# CHAPTER 4: Calculate Your ROI
story.append(Paragraph("4. How to Calculate Your Automation ROI", heading_style))
story.append(
    Paragraph(
        "Before implementing any AI tool, calculate your potential return. Here's a simple framework:",
        body_style,
    )
)
story.append(Spacer(1, 0.2 * inch))

story.append(Paragraph("Step 1: Calculate Your Current Cost", subheading_style))
story.append(
    Paragraph(
        "<b>Time spent × hourly value = current cost</b><br/><br/>Example: 5 hours/week on email responses × $30/hour = $150/week",
        body_style,
    )
)
story.append(Spacer(1, 0.2 * inch))

story.append(Paragraph("Step 2: Estimate Time Saved", subheading_style))
story.append(
    Paragraph(
        "AI typically reduces time by 50-80% for tasks it handles.<br/><br/>Example: 5 hours → 1 hour saved = 4 hours recovered weekly",
        body_style,
    )
)
story.append(Spacer(1, 0.2 * inch))

story.append(Paragraph("Step 3: Calculate Annual Savings", subheading_style))
story.append(
    Paragraph(
        "4 hours × 50 weeks × $30/hour = <b>$6,000/year saved</b>",
        body_style,
    )
)
story.append(Spacer(1, 0.2 * inch))

story.append(Paragraph("Step 4: Factor in Implementation Costs", subheading_style))
story.append(
    Paragraph(
        "Include setup time, learning curve, and any paid tools needed.<br/><br/>Example: 10 hours setup × $30 = $300 one-time cost<br/>ROI = ($6,000 - $300) / $300 = 1,900% first year",
        body_style,
    )
)
story.append(Spacer(1, 0.3 * inch))
story.append(
    Paragraph(
        "<b>Remember:</b> Start with low-cost or free tools to minimize risk. Your first automation should pay for itself in under 3 months.",
        body_style,
    )
)
story.append(PageBreak())

# CHAPTER 5: Common Mistakes
story.append(Paragraph("5. Common Mistakes When Implementing AI", heading_style))
story.append(
    Paragraph(
        "Many businesses try AI and give up because of these pitfalls. Here's how to avoid them:",
        body_style,
    )
)
story.append(Spacer(1, 0.2 * inch))

mistakes = [
    (
        "Mistake #1: Trying to automate everything at once",
        "Start with ONE simple task. Getting one thing working builds confidence and teaches you the process.",
    ),
    (
        "Mistake #2: Expecting perfection immediately",
        "AI improves with feedback. Plan to spend time in the first few weeks training it to match your standards.",
    ),
    (
        "Mistake #3: Not defining clear success metrics",
        "Before starting, ask: 'How will I know this is working?' Set specific targets like 'reduce response time by 50%'.",
    ),
    (
        "Mistake #4: Ignoring the human element",
        "AI handles tasks, but humans still own relationships. Use AI for speed, but keep personal touch where it matters.",
    ),
    (
        "Mistake #5: Not starting because you're not technical",
        "Most AI tools today are designed for non-technical users. You don't need to code to benefit from AI.",
    ),
]
for title, description in mistakes:
    story.append(Paragraph(title, subheading_style))
    story.append(Paragraph(description, body_style))
    story.append(Spacer(1, 0.15 * inch))

story.append(
    Paragraph(
        "<b>Bottom line:</b> Perfect is the enemy of good. Start small, iterate, and improve.",
        body_style,
    )
)
story.append(PageBreak())

# CHAPTER 6: Next Steps
story.append(Paragraph("6. Next Steps", heading_style))
story.append(
    Paragraph(
        "You're now equipped with the basics. Here's how to take action starting today:",
        body_style,
    )
)
story.append(Spacer(1, 0.2 * inch))

steps = [
    "Pick ONE tool from Chapter 3 that matches your biggest time drain",
    "Spend 30 minutes this week setting it up for one specific task",
    "Track your time for one week before and after to measure impact",
    "Document what works so you can replicate it for other tasks",
    "Scale to a second task only after the first is running smoothly",
]
for i, step in enumerate(steps, 1):
    story.append(Paragraph(f"<b>{i}.</b> {step}", bullet_style))

story.append(Spacer(1, 0.4 * inch))
story.append(Paragraph("Ready for More?", subheading_style))
story.append(
    Paragraph(
        "If you want to go deeper into AI automation, check out our paid guide: <b>The Super-Agentic AI System Guide</b>—a comprehensive 30-page resource for building advanced autonomous systems.",
        body_style,
    )
)
story.append(Spacer(1, 0.2 * inch))
story.append(
    Paragraph(
        "Visit <b>agentflow.com</b> for more free resources and tools.",
        body_style,
    )
)
story.append(PageBreak())

# FINAL PAGE
story.append(Spacer(1, 1 * inch))
story.append(
    Paragraph(
        "AgentFlow",
        ParagraphStyle(
            "BrandFinal",
            parent=styles["Heading1"],
            fontSize=20,
            textColor=HexColor("#3182ce"),
            alignment=TA_CENTER,
        ),
    )
)
story.append(Spacer(1, 0.2 * inch))
story.append(
    Paragraph(
        "Building the future of autonomous business.",
        ParagraphStyle(
            "Tagline",
            parent=styles["Normal"],
            fontSize=12,
            textColor=HexColor("#718096"),
            alignment=TA_CENTER,
        ),
    )
)
story.append(Spacer(1, 0.5 * inch))
story.append(
    Paragraph(
        "© 2026 AgentFlow. All rights reserved.",
        ParagraphStyle(
            "Footer",
            parent=styles["Normal"],
            fontSize=9,
            textColor=HexColor("#a0aec0"),
            alignment=TA_CENTER,
        ),
    )
)

doc.build(story)
print(f"PDF generated successfully: {output_path}")
