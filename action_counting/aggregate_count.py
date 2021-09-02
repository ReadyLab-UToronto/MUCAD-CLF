from action_classification import action_classification
from typing import List


def count_design_space(reader: iter) -> List[int]:
    """
    Aggregate count of actions classified in design space.
    :param reader: the csv reader of the audit trail file.
    :return: a list of count of actions classified in design space.
            Output list items correspond to the following design space count:
            [sketching, 3D features, mating, visualizing, browsing, other organizing]
    """
    count = [0, 0, 0, 0, 0, 0]
    next(reader)
    for row in reader:
        """
        Each row has format: 
        ['Index', 'Event Time', 'Document', 'Tab', 'User', 'Description']
        Example: 
        ['1', '2021-08-21 19:12:19', 'Doc', 'N/A', 'x@x.com', 'Close document']
        """
        # Classify actions in design space
        design_space = action_classification.classify_design_space(row[5].strip())
        if design_space != -1:
            if design_space == -10:  # the special "Add or modify a sketch" action
                count[0] += 1
                count[1] -= 1
            else:
                count[design_space] += 1
    return count


def count_action_type(reader: iter) -> List[int]:
    """
    Aggregate count of actions classified in action type.
    :param reader: the csv reader of the audit trail file.
    :return: a list of count of actions classified in action type.
            Output list items correspond to the following action type count:
            [creating, editing, deleting, revising, viewing, others]
    """
    count = [0, 0, 0, 0, 0, 0]
    next(reader)
    for row in reader:
        """
        Each row has format: 
        ['Index', 'Event Time', 'Document', 'Tab', 'User', 'Description']
        Example: 
        ['1', '2021-08-21 19:12:19', 'Doc', 'N/A', 'x@x.com', 'Close document']
        """
        # Classify actions in action type
        action_type = action_classification.classify_action_type(row[5].strip())
        if action_type >= 0:
            count[action_type] += 1
    return count


def aggregate_count(reader: iter) -> List[List[int]]:
    """
    Aggregate count of actions classified using the design space classification and the
    action type classification method.
    :param reader: the csv reader of the audit trail file.
    :return: a nested list of count of actions classified using the design space and the
            action type classification methods.
            Output list items correspond to the following count:
            [[sketching, 3D features, mating, visualizing, browsing, other organizing],
             [creating, editing, deleting, revising, viewing, other]]
    """
    count = [[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]
    next(reader)
    for row in reader:
        """
        Each row has format: 
        ['Index', 'Event Time', 'Document', 'Tab', 'User', 'Description']
        Example: 
        ['1', '2021-08-21 19:12:19', 'Doc', 'N/A', 'x@x.com', 'Close document']
        """
        # Classify actions in design space
        design_space = action_classification.classify_design_space(row[5].strip())
        if design_space != -1:
            if design_space == -10:  # the special "Add or modify a sketch" action
                count[0][0] += 1
                count[0][1] -= 1
            else:
                count[0][design_space] += 1
        # Classify actions in action type
        action_type = action_classification.classify_action_type(row[5].strip())
        if action_type >= 0:
            count[1][action_type] += 1
    return count
