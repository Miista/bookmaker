PANDOC=/usr/local/bin/pandoc
PANDOC_OPTIONS=--smart --standalone

# The path to the stylesheet.
# Used when compiling as ebook.
STYLESHEET_PATH=layout/style.css

# The directory where chapters are saved.
CHAPTER_DIR=chapters

# The directory where character bios are saved.
PROFILE_DIR=profiles

# Chapters start with a numbered sequence (0,9)
# Followed by the name of the character (a,z)*
# Then the extension: .md
# Example: 02-name.md OR 23-name.md
CHAPTERS=$(shell find -f $(CHAPTER_DIR) -E . -iregex "$(CHAPTER_DIR)/([0-9]{1,2})([a-z0-9]|-)*(.md)")

TEMPLATE=./$(PROFILES_DIR)/Template.md

PROFILES=$(shell find -f $(PROFILE_DIR) -E . -iregex "$(PROFILE_DIR)/.*.md" | grep -v '.*Template.*')

# Set name of output to the name of the directory
TITLE := $(shell basename $(CURDIR))

# Targets #

pdf:
	$(PANDOC) $(PANDOC_OPTIONS) -o $(TITLE).pdf $(CHAPTERS)

ebook:
	$(PANDOC) $(PANDOC_OPTIONS) --epub-stylesheet=$(STYLESHEET_PATH) -o $(TITLE).epub $(CHAPTERS)

docx:
	@$(PANDOC) $(PANDOC_OPTIONS) -o $(TITLE).docx $(CHAPTERS)

bios:
	@echo $(PROFILES)
	$(PANDOC) $(PANDOC_OPTIONS) -o "character-bios-$(TITLE)".pdf $(PROFILES)
