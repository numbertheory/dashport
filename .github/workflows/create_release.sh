#!/usr/bin/env bash

last_tag=$(git tag --sort=committerdate -l | tail -2 | head -1)
current_tag=$(git describe --tags)
commits=$(git log $current_tag...$last_tag --oneline --pretty='format:%C(auto)%h %s')

echo $commits
