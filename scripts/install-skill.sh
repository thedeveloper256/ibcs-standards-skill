#!/usr/bin/env bash
set -euo pipefail

REPO="thedeveloper256/ibcs-standards-skill"
TARGET=".opencode/skills/ibcs-standards"
GLOBAL=0
FORCE=0

while [ "$#" -gt 0 ]; do
  case "$1" in
    --global)
      GLOBAL=1
      shift
      ;;
    --force)
      FORCE=1
      shift
      ;;
    --*)
      echo "Unknown option: $1" >&2
      exit 2
      ;;
    *)
      TARGET="$1"
      shift
      ;;
  esac
done

if [ "$GLOBAL" -eq 1 ]; then
  TARGET="$HOME/.config/opencode/skills/ibcs-standards"
fi

TMP="$(mktemp -d)"
cleanup() {
  rm -rf "$TMP"
}
trap cleanup EXIT

curl -fsSL "https://github.com/$REPO/archive/refs/heads/main.tar.gz" -o "$TMP/repo.tar.gz"
tar -xzf "$TMP/repo.tar.gz" -C "$TMP"

SOURCE_ROOT="$(find "$TMP" -maxdepth 1 -type d -name 'ibcs-standards-skill-*' | head -n 1)"
if [ -z "$SOURCE_ROOT" ]; then
  echo "The downloaded archive is empty." >&2
  exit 1
fi

SOURCE="$SOURCE_ROOT/.opencode/skills/ibcs-standards"
if [ ! -d "$SOURCE" ]; then
  echo "The skill folder was not found in the downloaded archive." >&2
  exit 1
fi

if [ -e "$TARGET" ]; then
  if [ "$FORCE" -eq 1 ]; then
    rm -rf "$TARGET"
  else
    echo "Target already exists: $TARGET. Re-run with --force to replace it." >&2
    exit 1
  fi
fi

mkdir -p "$(dirname "$TARGET")"
cp -R "$SOURCE" "$TARGET"
echo "Installed the IBCS skill to $TARGET"
