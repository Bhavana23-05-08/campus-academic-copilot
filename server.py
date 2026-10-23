try:
    # MCP SDK v2 syntax
    from mcp.server import MCPServer as FastMCP
except ImportError:
    # MCP SDK v1 fallback
    from mcp.server.fastmcp import FastMCP

# Initialize MCP Server for Alexa+ Agent Skills
mcp = FastMCP("CampusAcademicCopilot")

# Mock College Academic Database
SCHEDULE = [
    {"time": "09:00 AM", "subject": "Data Structures & Algorithms", "room": "Lab 204"},
    {"time": "11:15 AM", "subject": "Operating Systems", "room": "Seminar Hall B"},
    {"time": "02:00 PM", "subject": "Machine Learning Fundamentals", "room": "Lab 101"}
]

DEADLINES = [
    {"subject": "Machine Learning", "task": "Project Proposal Submission", "due_date": "2026-10-28"},
    {"subject": "DSA", "task": "LeetCode Practice Log", "due_date": "2026-10-30"}
]

QUIZ_BANK = {
    "python": [
        {"q": "What decorator registers an MCP tool in FastMCP?", "a": "@mcp.tool()"},
        {"q": "How does Alexa+ receive tool outputs?", "a": "As structured JSON and natural text"}
    ],
    "ai": [
        {"q": "What does MCP stand for?", "a": "Model Context Protocol"},
        {"q": "How does an agent determine which tool to trigger?", "a": "Via function descriptions, types, and LLM reasoning"}
    ]
}

@mcp.tool()
def get_daily_schedule() -> str:
    """Retrieve today's complete college lecture and lab schedule with classroom numbers."""
    result = "Here is your academic schedule for today:\n"
    for item in SCHEDULE:
        result += f"- {item['time']}: {item['subject']} in {item['room']}\n"
    return result

@mcp.tool()
def check_upcoming_deadlines() -> str:
    """Fetch pending project and assignment deadlines for the current semester."""
    result = "Pending deadlines:\n"
    for d in DEADLINES:
        result += f"- {d['subject']}: {d['task']} (Due: {d['due_date']})\n"
    return result

@mcp.tool()
def get_revision_quiz(topic: str) -> str:
    """Generate quick review flashcard questions for revision before internal exams.
    
    Args:
        topic: The subject topic to quiz on (e.g. 'python' or 'ai').
    """
    topic_key = topic.lower().strip()
    questions = QUIZ_BANK.get(topic_key)
    if not questions:
        return f"No questions available for '{topic}'. Try 'python' or 'ai'."
    
    output = f"Revision questions for {topic.title()}:\n"
    for i, item in enumerate(questions, 1):
        output += f"Q{i}: {item['q']} | Answer: {item['a']}\n"
    return output

if __name__ == "__main__":
    mcp.run(transport="stdio")