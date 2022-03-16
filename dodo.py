def task_project1_setup():
    pass


def task_project1():
    return {
        "actions": [
            'echo "SELECT 1;" > actions.sql',
            'echo "SELECT 2;" >> actions.sql',
            'echo \'{"VACUUM": true}\' > config.json',
        ],
        # Always rerun this task
        "uptodate": [False],
    }