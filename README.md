This is a tool for creating the skeleton for a book.
It assumes that Pandoc and git is installed and available on the path.

## Creating a Book

Run `book new`.
It will ask you for the name
and whether you want to use version control (you should!).

## Publishing

There are three different output types: PDF, docx, and ePub.
All of them can be created by typing `book make [type]`.
If no type is given, PDF is assumed.

## Future

### Session Handling

The ability to handle writing sessions.
When a writing session is started, all work is saved at a regular interval,
and at the end of a session, all work is committed to version control.

### Wrappers Around git

Provide commands for some of the functionality provided by git e.g. `git log`.