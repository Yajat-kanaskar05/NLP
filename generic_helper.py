import re

def extract_session_id(session_str: str):

    match = re.search(r"/sessions/(.*?)/contexts/" , session_str)

    if match:
        extracted_string = match.group(1)
        return extracted_string
    
    return ""

if __name__ == "__main__":
    print(extract_session_id("projects/first-agent-opba/agent/sessions/b88ff248-b608-48ce-7304-c3c8e86f167f/contexts/ongoing-tracking"))