# python-shortcuts

🍏 + 🐍 = ❤️

**python-shortcuts** is a library to create [Siri Shortcuts](https://support.apple.com/en-ae/guide/shortcuts/welcome/ios) on your laptop with your favourite text editor.
It uses [toml](https://github.com/toml-lang/toml) to represent shortcuts.

The library is in a very early development state (PR welcome!), so it does not support all actions from Shortcuts app.

* [Tutorial](docs/tutorial.md)
* [How to add a new action](docs/new_action.md)
* [Supported actions](docs/actions.md)
* [Examples](examples/)
* [Changelog](docs/CHANGELOG.md)
* [Documentation](docs/)

## Why

I wanted to convert my shortcut to a file in human-readable format. :)

## How to use

### Requirements

This library requires `plutil` tool, which should be installed on MacOS by default.
On Linux, you should be able to use `plistutil` instead.

### Installation

```bash
pip install python-shortcuts
```

### Usage

### shortcut → toml

If you need to convert existing shortcut to a toml file, at first you need to export it.
Go into Shortcuts app, open the shortcut and share it. Choose "Share as file" and use this file with this library.

Convert `toml` file with shortcut description to a real shortcut file.
After you need to open the file with iOS Shortcuts app.

```bash
shortcuts examples/test.toml my_first_shortcut.shortcut
```

### toml → shortcut

Also, you can convert shortcut file to a `toml`:

```bash
shortcuts examples/test.shortcut test.toml
```

More examples of `toml` files you can find [here](examples/).
And [read the tutorial](docs/tutorial.md)! :)

## Development

### Tests

Run tests:

```bash
tox
```

### TODO

* ☐ Conditionals: if-else, menu
* ☐ Nested fields: dict/array/etc
* ☐ Support variables in every field which support them in Shortcuts app
* ☐ Workflow types: widget, etc.
* ☐ Describe all actions
* ☐ Support magic variables
* ☐ Support all current actions from Shortcuts app