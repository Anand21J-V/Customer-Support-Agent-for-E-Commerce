import os
from pathlib import Path

PROJECT_NAME = "ecom-support-agent"

STRUCTURE = {
    "app": {
        "main.py": "# Entry point\n\nif __name__ == '__main__':\n    print('Ecom Support Agent started')\n",
        "graph": {
            "__init__.py": "",
            "base_graph.py": "# Minimal LangGraph setup\n\n# Placeholder for graph definition\n"
        },
        "llm": {
            "__init__.py": "",
            "groq_client.py": "# Groq LLM wrapper\n\nclass GroqClient:\n    def __init__(self, api_key: str):\n        self.api_key = api_key\n\n    def invoke(self, prompt: str):\n        pass\n"
        },
        "state": {
            "__init__.py": "",
            "support_state.py": "# Support agent state (empty for now)\n"
        },
        "config": {
            "settings.py": "# App configuration\n\nimport os\n\nGROQ_API_KEY = os.getenv('GROQ_API_KEY')\n"
        }
    },
    "tests": {
        "test_phase1.py": "# Phase 1 tests\n\ndef test_placeholder():\n    assert True\n"
    },
    ".env": "GROQ_API_KEY=\n",
    ".gitignore": "__pycache__/\n.env\n.venv/\n",
    "requirements.txt": "langgraph\ngroq\npython-dotenv\n",
    "README.md": "# Ecom Support Agent\n\nLangGraph-based e-commerce support agent.\n"
}


def create_structure(base_path: Path, structure: dict):
    for name, content in structure.items():
        path = base_path / name

        if isinstance(content, dict):
            path.mkdir(parents=True, exist_ok=True)
            create_structure(path, content)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)


def main():
    root = Path(PROJECT_NAME)
    root.mkdir(exist_ok=True)
    create_structure(root, STRUCTURE)
    print(f"✅ Project '{PROJECT_NAME}' created successfully!")


if __name__ == "__main__":
    main()
