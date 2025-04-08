# get_papers_list/filters.py

import re

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = ["university", "college", "institute", "school", "faculty", "department", "hospital"]
    non_academic_keywords = ["pharma", "biotech", "inc", "corp", "ltd", "gmbh", "s.a.", "co."]

    affiliation_lower = affiliation.lower()
    
    if any(word in affiliation_lower for word in academic_keywords):
        return False
    return any(word in affiliation_lower for word in non_academic_keywords)
