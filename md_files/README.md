# markdown-latex-math-render

A GitHub action to render latex math formulas in markdown files.

## How it works

This github action makes use of the [codecogs](https://latex.codecogs.com/) api to generate formula images.

Assume we have some formulas as follow
```
This is an equation: $$ d = \alpha * x + \beta * y $$

This is an equation: $ d = \alpha * x + \beta * y $

This is an equation:

$$
d = \alpha * x + \beta * y
$$
```

They will be converted to:
```
This is an equation: ![](https://latex.codecogs.com/svg.image?d%20=%20\alpha%20*%20x%20+%20\beta%20*%20y)

This is an equation: ![](https://latex.codecogs.com/svg.image?d%20=%20\alpha%20*%20x%20+%20\beta%20*%20y)

This is an equation:

![](https://latex.codecogs.com/svg.image?d%20=%20\alpha%20*%20x%20+%20\beta%20*%20y)
```

Result:

This is an equation: $ d = \alpha * x + \beta * y $

This is an equation: $$ d = \alpha * x + \beta * y $$

This is an equation:

$$
d = \alpha * x + \beta * y
$$

## Inputs

| Name | Description | Default |
| ---  | --- | --- |
| `markdown-files` | The input markdown files to be rendered. | `None` |
| `output-dir`    | The output directory | `.` |

## Usage

```yml
    uses: kinglittleq/markdown-latex-math-render@v0.1
    with:
        markdown-files: md_files/*.md  # or md_files/README.md
        output-dir: .

    # commit changes and push
    - name: Commit
    run: |
        git config --global user.name 'Github Action Bot'
        git config --global user.email 'bot@example.com'
        git add *.md
        git commit -m 'Render latex formulas'
        git push origin || echo "No changes to commit"
```

## License

[MIT](LICENSE)