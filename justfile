# show this list
default:
    just --list

# does a version bump commit
bump-commit type: && create-tag
    poetry version {{type}}
    git commit -am "$(poetry version | awk '{print $2}' | xargs echo "bump to")"
    git push

# creates a new tag for the current version
create-tag:
    git fetch --tags
    poetry version | awk '{print $2}' | xargs git tag
    git push --tags

# update deps
update:
    nix flake update
    # the poetry devs dont allow this with normal update for some unknown reason
    poetry up --latest

# do a dep bump commit with tag and version
update-commit: update && create-tag
    poetry version patch
    git commit -am "bump deps"
    git push

# format
format:
    # TODO: treefmt?
    isort .
    black .
    alejandra .