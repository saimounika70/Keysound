# 🎹 Keyboard Sound Emulator

Turn your regular keyboard into a satisfying mechanical keyboard — for free!

This simple cross-platform Python app plays custom keypress sounds whenever you type. No need to spend thousands on a mechanical keyboard — just run this, and get clicky feedback right from your speakers.

## 📦 Features

- Custom sound profiles: `click`, `linear`, `tactile`, and more
- GUI to toggle sounds and switch profiles
- ESC key to stop the emulation
- Works on macOS, Windows, and Linux (tested on macOS)

## 📁 Folder Structure

keyboard-sound-emulator/
├── sounds/
│ ├── click.wav
│ ├── linear.wav
│ └── tactile.wav
├── main.py
├── requirements.txt
└── README.md


## 🛠 Installation

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/keyboard-sound-emulator.git
cd keyboard-sound-emulator
```

2. **Install dependencies**
   pip install -r requirements.txt

3. **Add your sound file**
   Place .wav files in the ```sounds/```folder. You can name them anything.

4. **Run the app**
   python main.py


---

🧠 Ideas for Future

System tray icon
Save last used sound profile
Hotkey toggle
Per-app profiles
Sound volume control
Cross-platform build (EXE, DMG)

----

📜 License

MIT License. Use it, fork it, improve it.

🤝 Contribute

Pull requests and suggestions welcome!



Made with ❤️ by Mounika


---

# 7️⃣ (Optional) GitHub Actions Workflow for CI

Create a folder `.github/workflows/` and inside it, create `python-app.yml` with this content to test your app on push:

```yaml
name: Python App CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run script (test run)
        run: python main.py --help || echo "Skipping GUI run in CI"

