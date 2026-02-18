# bac-games

A collection of Python scripts facilitating the production of various games for the **BlazeandCave** community. The majority of the games here relate to **BlazeandCave's Advancements Pack (BACAP)**, a datapack that adds 1200+ new advancements to Minecraft.

## Overview

This repository contains several scripts that utilize a local database of advancements (`bac-database/bacap.db`) to generate games or assist with puzzles.

### Key Features
*   **Datapack Reader**: Reads the datapack (and associated spreadsheet) and creates a comprehensive database of every advancement.
*   **Fill in the Blanks**: Creates fill in the blanks puzzles using BACAP advancement names. Output is pasted directly into Sporcle to create a new quiz.
*   **Skribbl Generator**: Generates a word list for Skribbl.io using BACAP advancement names. Output is pasted directly into word list. Allows for various queries and modifications for flexible gameplay.
*   **Crossword Helper**: A Regex-based search tool for finding Minecraft and BACAP-related terms.
*   **Connections Automator**: A script which automates data entry for "BACAP Connections" puzzles.

## Prerequisites

*   Python 3.x
*   The following Python packages:
    ```bash
    pip install numpy pyautogui keyboard pyperclip
    ```
*   A valid SQLite database file at `bac-database/bacap.db` containing an `advancements` table.
*   If you wish to create a new db file, you must attach a copy of BlazeandCave's Advancement Pack in   `bac-database/packs`.

## Usages

* Every script can be ran with Python 3.x. Use a Python interpreter or run from terminal as shown in the example below:

```bash
python blanks.py
```

## Directory Structure

*   `bac-database/`: Should contain the `bacap.db` SQLite database.
*   `Text/`: text files used by `cross.py` and `connections.py` (e.g., `cross.txt`, `mc.txt`, `advs.txt`).
*   `*.py`: The main game and utility scripts.

## Note
These scripts are tailored for a specific use case involving BlazeandCave's Advancements Pack. Ensure you have the necessary database and pack files for them to function as intended.
