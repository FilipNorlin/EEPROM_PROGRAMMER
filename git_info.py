import subprocess
import sys


def run_git_command(command):
    """Run a git command and return its output."""
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True,
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error: {result.stderr.strip()}"
    except Exception as e:
        return f"Exception: {str(e)}"


def get_git_version():
    """Get the Git version."""
    return run_git_command("git --version")


def get_git_config(key):
    """Get a specific Git config value."""
    return run_git_command(f"git config --get {key}")


def get_global_git_configs():
    """Get all global Git configurations."""
    return run_git_command("git config --global --list")


def get_local_git_configs():
    """Get all local Git configurations (if in a repository)."""
    return run_git_command("git config --local --list")


def get_current_branch():
    """Get the current branch name."""
    return run_git_command("git branch --show-current")


def get_remote_url():
    """Get the remote URL of the repository."""
    return run_git_command("git remote get-url origin")


def get_last_commit():
    """Get the last commit details."""
    return run_git_command("git log -1 --pretty=format:'%H - %an, %ar : %s'")


def stage_changes():
    """Stage all changes for commit."""
    return run_git_command("git add .")


def commit_changes(message):
    """Commit the staged changes with a message."""
    return run_git_command(f'git commit -m "{message}"')


def push_changes():
    """Push the committed changes to the remote repository."""
    return run_git_command("git push")


def main():
    print("Git Version:")
    print(get_git_version())
    print()

    print("Global Git Configurations:")
    print(get_global_git_configs())
    print()

    print("Local Git Configurations:")
    print(get_local_git_configs())
    print()

    print("User Name:")
    print(get_git_config("user.name"))
    print()

    print("User Email:")
    print(get_git_config("user.email"))
    print()

    print("Current Branch:")
    print(get_current_branch())
    print()

    print("Remote URL:")
    print(get_remote_url())
    print()

    print("Last Commit:")
    print(get_last_commit())
    print()

    # Check for uncommitted changes
    uncommitted_changes = run_git_command("git status --porcelain")
    if uncommitted_changes:
        print("Uncommitted changes detected:")
        print(uncommitted_changes)

        # Stage, commit, and push changes
        stage_response = stage_changes()
        if "Error" not in stage_response:
            print("Changes staged successfully.")

            commit_message = input("Enter commit message: ")
            commit_response = commit_changes(commit_message)
            if "Error" not in commit_response:
                print("Changes committed successfully.")

                push_response = push_changes()
                if "Error" not in push_response:
                    print("Changes pushed to remote repository successfully.")
                else:
                    print(f"Failed to push changes: {push_response}")
            else:
                print(f"Failed to commit changes: {commit_response}")
        else:
            print(f"Failed to stage changes: {stage_response}")
    else:
        print("No uncommitted changes detected.")


if __name__ == "__main__":
    main()
