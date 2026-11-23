# Retake the journey screenshots

From this folder:

1. `python3 serve.py &` serves the repo on http://127.0.0.1:8765 (UTF-8, no password).
2. `node shot.js ted.json ../shots-png && node shot.js fedor.json ../shots-png` (make the folder first).
3. Convert each PNG to JPEG in `../shots/` (Ted) or `../shots-fedor/` (Fedor), 1600x1000.
4. `cd .. && python3 build.py && node print.js ted && python3 build.py fedor && node print.js fedor`.

Each plan step can click buttons and swap sample text (Gabriele becomes Ted; Fedor's meeting swaps the title, host and topic).
