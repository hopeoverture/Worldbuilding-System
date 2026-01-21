# Worlds

This directory contains your worldbuilding projects. Each world is a self-contained setting with its own entities organized by category.

## Structure

```
Worlds/
└── [World Name]/
    ├── World Overview.md      # Main world document
    ├── Characters/
    ├── Settlements/
    ├── Items/
    ├── Creatures/
    ├── Organizations/
    ├── Concepts/
    ├── History/
    └── Geography/
```

## Creating a New World

Use the `/create-world` command to generate a new world with the full folder structure.

## Entity Notes

Entity notes are created from templates in the `Templates/` folder. Each entity should:
- Be placed in the appropriate category folder within your world
- Use wikilinks `[[Entity Name]]` to connect to other entities in the same world
- Have its YAML `status` field updated as you develop it (draft → in-progress → complete)

## Cross-World References

If you need to reference entities across worlds, use the full path:
`[[World Name/Category/Entity Name]]`
