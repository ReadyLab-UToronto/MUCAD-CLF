def classify_design_space(action: str) -> int:
    """
    The returning index corresponds to the list stored in "count":
    [sketching, 3D features, mating, visualizing, browsing, other organizing]

    Formulas for each design space action:
        sketching = "Add or modify a sketch" + "Copy paste sketch"
        3D features = "Commit add or edit of part studio feature" + "Delete part studio feature"
                    - "Add or modify a sketch"
        mating = "Add assembly feature" + "Delete assembly feature" + "Add assembly instance"
                    + "Delete assembly instance"
        visualizing = "Start assembly drag" + "Animate action called"
        browsing = Opening a tab + Creating a tab + Deleting a tab + Renaming a tab
        other organizing = "Create version" + "Cancel Operation" + "Undo Redo Operation"
                    + "Merge branch" + "Branch workspace" + "Update version"

    :param action: the action to be classified
    :return: the index of the action type that this action is accounted for; if the action does not
            belong to any category, return -1

            Note:   "Add or modify a sketch" is special (+1 for sketching and -1 for 3D features),
                    return -10
    """
    # Creating a sketch is special as it affects both the sketching and the 3D features counts
    if action == "Add or modify a sketch":
        return -10
    # Sketching
    elif action == "Copy paste sketch":
        return 0
    # 3D features
    elif action in ["Commit add or edit of part studio feature",
                    "Delete part studio feature"]:
        return 1
    # Mating
    elif action in ["Add assembly feature", "Delete assembly feature", "Add assembly instance"
                    "Delete assembly instance"]:
        return 2
    # Visualizing
    elif action in ["Start assembly drag", "Animate action called"]:
        return 3
    # Browsing
    elif "Tab" in action and ("opened" in action or "created" in action or "deleted" in action or
                              "renamed" in action):
        return 4
    # Other organizing
    elif action in ["Create version", "Cancel Operation", "Undo Redo Operation", "Merge branch",
                    "Branch workspace", "Update version"]:
        return 5
    # Not classified (Optional: print out the unclassified actions)
    else:
        return -1


def classify_action_type(action: str) -> int:
    """
    The returning index corresponds to the list stored in "count":
    [creating, editing, deleting, revising, viewing, other]

    Formulas for each design space action:
        creating = "Add part studio feature" + "Add assembly feature" + "Add assembly instance"
                    + "Copy paste sketch"
        editing = "Start edit of part studio feature" + "Start edit of assembly feature"
                    + "Set mate values"
        deleting = "Delete part studio feature" + "Delete assembly feature"
                    + "Delete assembly instance"
        revising = "Cancel Operation" + "Undo Redo Operation"
        viewing = Opening a tab + "Animate action called"
        other = Creating a tab + Deleting a tab + "Create version" + Renaming a tab
                    + "Merge branch" + "Branch workspace" + "Update version"

    :param action: the action to be classified
    :return: the index of the action type that this action is accounted for; if the action does not
            belong to any category, return -1
    """
    # Creating
    if action in ["Add part studio feature", "Add assembly feature", "Add assembly instance",
                  "Copy paste sketch"]:
        return 0
    # Editing
    elif action in ["Start edit of part studio feature", "Start edit of assembly feature",
                    "Set mate values"]:
        return 1
    # Deleting
    elif action in ["Delete part studio feature", "Delete assembly feature",
                    "Delete assembly instance"]:
        return 2
    # Revising
    elif action in ["Cancel Operation", "Undo Redo Operation"]:
        return 3
    # Viewing
    elif action == "Animate action called" or ("Tab" in action and "opened" in action):
        return 4
    # Other
    elif action in ["Create version", "Merge branch", "Branch workspace", "Update version"] \
            or ("Tab" in action and
                ("created" in action or "deleted" in action or "renamed" in action)):
        return 5
    # Not classified (Optional: print out the unclassified actions)
    else:
        return -1
