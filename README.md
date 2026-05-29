# WebStart CLI

A lightweight Python command-line tool that instantly creates a frontend starter project with HTML, CSS, and JavaScript files named after the project itself.

The tool also automatically opens the generated project in Visual Studio Code.

---

# Features

* Creates project folder automatically
* Generates:

  * `projectName.html`
  * `projectName.css`
  * `projectName.js`
* Automatically links CSS and JS files inside HTML
* Opens generated project directly in VS Code
* Simple terminal workflow
* Saves frontend setup time

---

# Example

Running:

```bash
webstart portfolio
```

Creates:

```text
portfolio/
│
├── portfolio.html
├── portfolio.css
└── portfolio.js
```

Then automatically opens the project in VS Code.

---

# Tech Stack

* Python
* VS Code
* Command Prompt / Terminal

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/adityasantoshgupta223/webstart-cli.git
```

---

## 2. Move Into Project Folder

```bash
cd webstart-cli
```

---

# Requirements

## Python

Verify Python installation:

```bash
python --version
```

If Python is not installed, download it from:

[Python Official Website]

IMPORTANT:

During installation, enable:

```text
✔ Add Python to PATH
```

---

## Visual Studio Code

Verify VS Code installation:

```bash
code --version
```

If VS Code is not installed, download it from:

[Visual Studio Code Official Website]

---

# Enable VS Code Terminal Command

If the `code` command does not work:

1. Open VS Code
2. Press:

```text
Ctrl + Shift + P
```

3. Search:

```text
Shell Command: Install 'code' command in PATH
```

4. Restart terminal

---

# Add Environment Variable (Windows)

This allows you to run the command globally from any terminal.

---

## Step 1: Copy Project Folder Path

Example:

```text
C:\Users\YourName\webstart-cli
```

---

## Step 2: Open Environment Variables

1. Press:

```text
Windows + S
```

2. Search:

```text
Environment Variables
```

3. Open:

```text
Edit the system environment variables
```

4. Click:

```text
Environment Variables
```

---

## Step 3: Edit PATH Variable

Under:

```text
User variables
```

Select:

```text
Path
```

Then click:

```text
Edit → New
```

Paste your project folder path.

Example:

```text
C:\Users\YourName\webstart-cli
```

Click:

```text
OK
```

on all windows.

---

# Usage

Run:

```bash
webstart myProject
```

Example:

```bash
webstart landing-page
```

Generated structure:

```text
landing-page/
│
├── landing-page.html
├── landing-page.css
└── landing-page.js
```

The project automatically opens in VS Code after creation.

---

# HTML Template Linking

Generated HTML automatically includes:

```html
<link rel="stylesheet" href="projectName.css">
<script src="projectName.js"></script>
```

The project name is dynamically inserted during generation.

---

# Project Structure

```text
webstart-cli/
│
├── webstart.py
├── webstart.bat
├── template.txt
├── README.md
```

---

# Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss improvements.

---

# License

MIT License
>>>>>>> 485ae4f (Updated README.md)
