from action_classification import action_classification
from typing import List, Dict


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


def aggregate_count(reader: iter, file_name: str, separate_users=False) -> Dict:
    """
    Aggregate count of actions classified using the design space classification and the
    action type classification method.
    :param reader: the csv reader of the audit trail file.
    :param file_name: the file name of the csv that is being analyzed.
    :param separate_users: if more than one user is found in one csv file, would their counts be
                            counted separately?
    :return: a dictionary of counts for the file/each user in the file (depending on
            if separate_users is selected); counts are stored a nested list of count
            of actions classified using the design space and the action type
            classification methods.

            List items in the output Dict correspond to the following count:
            [[sketching, 3D features, mating, visualizing, browsing, other organizing],
             [creating, editing, deleting, revising, viewing, other]]
    """
    empty_count = [[0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0]]
    next(reader)
    if not separate_users:
        count = empty_count
    else:
        count = {}
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
                if not separate_users:
                    count[0][0] += 1
                    count[0][1] -= 1
                else:
                    user = file_name + '/' + row[4].strip().split("@")[0]
                    if user not in count:
                        count[user] = empty_count
                    count[user][0][0] += 1
                    count[user][0][1] -= 1
            else:
                if not separate_users:
                    count[0][design_space] += 1
                else:
                    user = file_name + '/' + row[4].strip().split("@")[0]
                    if user not in count:
                        count[user] = empty_count
                    count[user][0][design_space] += 1
        # Classify actions in action type
        action_type = action_classification.classify_action_type(row[5].strip())
        if action_type >= 0:
            if not separate_users:
                count[1][action_type] += 1
            else:
                user = file_name + '/' + row[4].strip().split("@")[0]
                if user not in count:
                    count[user] = empty_count
                count[user][1][action_type] += 1
    if separate_users:
        return count
    else:
        return {file_name: count}
