from pathlib import Path

fileName = "dummy.txt"

# Deletes the file; won't crash if the file does not exist
Path(fileName).unlink(missing_ok=True)
