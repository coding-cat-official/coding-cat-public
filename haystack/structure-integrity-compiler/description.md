You're deep into building your own compiler for the LYNX programming language, a quirky systems language originally used for low-orbit drones. The spec is... eccentric. For instance:

- Curly braces `{}` define data scopes.
- Angle brackets `<>` sometimes denote generics, but not always.
- Parentheses `()` wrap conditionals, but can also appear in macros.
- Square brackets `[]` are used for both array access and annotations.

But before the compiler can even begin parsing any of that, it must do something humble and essential: **validate structure**.

This early "structure integrity" pass skips the contents and ignores types. Its job is to make sure any LYNX source file has cleanly matched control characters—especially those pesky round ones. The rest can come later: tokenization, ASTs, optimizations. But if a file doesn’t pass the structure check? No point continuing.

You’re implementing that first pass.

Notes from the compiler spec:
- It’s OK to have other text in the file.
- You're not required to handle braces `{}` or brackets `[]` yet.
- But if the `()` are unbalanced, compilation must fail.

You're not yet optimizing, parsing, or even interpreting.  
**Your job is just to make sure no program breaks your compiler before it even starts.**

