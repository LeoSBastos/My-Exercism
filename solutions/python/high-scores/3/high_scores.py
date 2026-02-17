"""
High Scores
"""

def latest(scores):
    """
    Latest
    """
    return scores[-1]

def personal_best(scores):
    """
    Personal best    
    """
    return max(scores)

def personal_top_three(scores):
    """
    Personal top three    
    """
    return sorted(scores, reverse=True)[:3]

def latest_after_top_three(scores):
    """
    latest after Personal top three
    """
    return latest(personal_top_three(scores))

def scores_after_top_three(scores):
    """
    Scores
    """
    return scores
    