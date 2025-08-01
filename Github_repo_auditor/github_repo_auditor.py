#!/usr/bin/env python3

import os
import subprocess
from pathlib import Path
from datetime import datetime, timedelta

def is_git_repo(path):
    return (path / '.git').exists()

def run_git_command(repo_path, args):
    try:
        result = subprocess.run(
            ['git'] + args,
            cwd=repo_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return ""

def check_repo_status(repo_path):
    status = {
        'path': str(repo_path),
        'uncommitted_changes': False,
        'ahead': False,
        'behind': False,
        'inactive': False,
        'last_commit': None,
    }

    # Uncommitted changes
    changes = run_git_command(repo_path, ['status', '--porcelain'])
    if changes:
        status['uncommitted_changes'] = True

    # Ahead/Behind
    run_git_command(repo_path, ['remote', 'update'])  # Update remote tracking
    branch_info = run_git_command(repo_path, ['status', '-sb'])
    if 'ahead' in branch_info:
        status['ahead'] = True
    if 'behind' in branch_info:
        status['behind'] = True

    # Last commit date
    last_commit_date = run_git_command(repo_path, ['log', '-1', '--format=%ci'])
    if last_commit_date:
        commit_time = datetime.strptime(last_commit_date, '%Y-%m-%d %H:%M:%S %z')
        status['last_commit'] = commit_time
        if datetime.now(commit_time.tzinfo) - commit_time > timedelta(days=30):
            status['inactive'] = True

    return status

def scan_repos(base_dir):
    base = Path(base_dir).expanduser()
    for root, dirs, files in os.walk(base):
        root_path = Path(root)
        if is_git_repo(root_path):
            yield check_repo_status(root_path)
            dirs[:] = []  # Do not recurse into nested repos

def print_report(repos):
    for repo in repos:
        path = repo['path']
        if repo['uncommitted_changes']:
            print(f"[!] Uncommitted changes:     {path}")
        if repo['ahead']:
            print(f"[↑] Ahead of origin/main:    {path}")
        if repo['behind']:
            print(f"[↓] Behind origin/main:      {path}")
        if repo['inactive']:
            last = repo['last_commit'].strftime('%Y-%m-%d')
            print(f"[-] Inactive >30 days:       {path} (Last: {last})")

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python git-repo-cleaner.py <base_directory>")
        sys.exit(1)

    base_dir = sys.argv[1]
    print(f"📁 Scanning Git repos in: {base_dir}\n")
    results = list(scan_repos(base_dir))
    print_report(results)
