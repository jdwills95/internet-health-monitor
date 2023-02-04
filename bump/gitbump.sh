#!/usr/bin/env bash
set -e

git fetch --tags # checkout action does not get these

# -v:refname is a version sort
oldv=$(git tag --sort=-v:refname --list "v[0-9]*" | head -n 1)

# if there is no version tag yet, let's start at v0.0.0
if [ -z "$oldv" ]; then
   echo "No existing version, starting at v0.0.0"
   oldv="v0.0.0"
fi

echo "oldv: $oldv"
newv="${oldv%.*}.$((${oldv##*.}+1))"
echo "newv: $newv"

git tag -a "$newv" -m "version $newv"
git push --follow-tags
