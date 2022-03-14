# LSP-prisma

![LICENSE](https://img.shields.io/badge/LICENSE-MIT-green?style=for-the-badge) ![Sublime Text](https://img.shields.io/badge/ST-Build%204126+-orange?style=for-the-badge&logo=sublime-text) ![Tag](https://img.shields.io/github/v/tag/Sublime-Instincts/LSP-prisma?style=for-the-badge&logo=github&sort=semver)

`LSP-prisma` is a LSP helper package for the [Prisma Language Server](https://github.com/prisma/language-tools/tree/main/packages/language-server). `LSP-prisma` on it's own doesn't do anything. It acts as a glue between the `LSP` package and the [Prisma Language Server](https://github.com/prisma/language-tools/tree/main/packages/language-server). It takes care of downloading, configuring & updating the language server for you so that you don't have to do it manually.

## Features

Everything that the [Prisma Language Server](https://github.com/prisma/language-tools/tree/main/packages/language-server) supports, which includes

- Linting for your prisma schema files to show possible issue(s) & error(s).
- Intelligent auto completions.
- `Goto Definition` for models & enums.
- Formatting of your schema files using `prisma fmt`.

Read the [Documentation]() section to understand how to use these features from ST.

## Installation

#### Package Control

Make sure that you have the [LSP](https://packagecontrol.io/packages/LSP) package installed before installing `LSP-prisma` (since `LSP` is the client package implementing the LSP protocol and is needed by `LSP-prisma` in order to work).

This package is not available on Package Control. Once you have `LSP` installed, use the following instructions.

Use `Package Control: Add Repository` from the command palette. Copy the github url (without the `.git` at the end) and enter it into the input panel that pops up at the bottom when you select `Package Control: Add Repository`. Now use `Package Control: Install Package` and search for `LSP-prisma` and install it.

## Documentation

### How to use this package ?



## Reporting issues.

This package is just a wrapper around the [Prisma Language Tools](https://github.com/prisma/language-tools/tree/main/packages/language-server). If you face any issues, you can verify to see if the same thing happens in VS Code. If it does, it's an issue with the language tools and an issue shoulb be filed with them.

Please follow the issue template that has been setup while reporting any bug(s) (So as to stay as organised as possible).

## Acknowledgements.

This package won't exist without [LSP](https://packagecontrol.io/packages/LSP) & the [Prisma Language Tools](https://github.com/prisma/language-tools/tree/main/packages/language-server), so huge thanks to them for making working with prisma schema files easier !

## License
The MIT License (MIT)

Copyright 2022 &copy; Ashwin Shenoy

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
