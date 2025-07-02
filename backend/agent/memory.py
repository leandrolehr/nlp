# agent/memory.py
from typing import Dict, List

class ConversationMemory:
    def __init__(self):
        self.sessions: Dict[str, List[Dict]] = {}

    def add_message(self, session_id: str, role: str, message: str):
        if session_id not in self.sessions:
            self.sessions[session_id] = []
        self.sessions[session_id].append({"role": role, "message": message})

    def get_history(self, session_id: str) -> List[Dict]:
        return self.sessions.get(session_id, [])

    def clear_session(self, session_id: str):
        if session_id in self.sessions:
            del self.sessions[session_id]
