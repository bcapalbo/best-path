def parse_origin_goal(goal):
    return goal.split('-')

def format_output(best_path):
    return ' - '.join(best_path)
