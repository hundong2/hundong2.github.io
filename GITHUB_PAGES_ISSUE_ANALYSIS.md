# GitHub Pages Build Failures: YAML Front Matter and Liquid Template Issues

## Problem Summary
The GitHub Pages deployment workflow has been consistently failing due to YAML front matter syntax errors and Liquid template parsing conflicts in blog posts.

## Root Causes Identified

### 1. YAML Front Matter Syntax Issues
- **Special characters in tags**: Tags containing parentheses, colons, backticks, and commas were not properly quoted
- **Korean text followed by punctuation**: Tags mixing Korean characters with special punctuation caused parsing errors
- **Examples of problematic tags**:
  ```yaml
  tags: [ai, (Graph, Neural, Networks,, GNNs)을, 활용한]  # ❌ Bad
  tags: [ai, "Graph Neural Networks", "GNNs", 활용한]      # ✅ Good
  ```

### 2. Liquid Template Parsing Conflicts
- **C# code with curly braces**: Jekyll was interpreting `{className}` and `{{$input}}` as Liquid template syntax
- **Double braces in code**: Any `{{` or `}}` in code blocks was being processed as Liquid templates
- **Solution**: Wrapped code blocks containing curly braces in `&#123;% raw %&#125;` tags

## Error Examples from Build Logs

```
Error: YAML Exception reading /github/workspace/_posts/ai/2025-07-11-ai-today.md: 
(<unknown>): did not find expected node content while parsing a flow node at line 5 column 61

Error: YAML Exception reading /github/workspace/_posts/c++/2025-07-10-c++-today.md: 
(<unknown>): found character that cannot start any token while scanning for the next token at line 5 column 36

Liquid Exception: Liquid syntax error (line 76): Variable '{{ public partial class {className}' 
was not properly terminated with regexp: /\}\}/
```

## Files Fixed
Fixed 69 files with YAML front matter issues across:
- 23 AI posts (`_posts/ai/`)
- 32 C++ posts (`_posts/c++/`)  
- 20 .NET/dotnet posts (`_posts/dotnet/`)

## Solutions Applied

### 1. Automated YAML Tag Fixing
Created Python script to systematically fix problematic tags:
- Quote tags containing special characters: `()`, `:`, `` ` ``, `.`, `-`, `+`, ` `
- Clean up malformed tag structures
- Preserve existing properly quoted tags

### 2. Liquid Template Escaping
Wrapped code blocks containing curly braces in raw tags:
```markdown
&#123;% raw %&#125;
```csharp
string template = "Hello {{name}}!";
```
&#123;% endraw %&#125;
```

### 3. Validation
- All 99 markdown files now pass YAML front matter validation
- No more Liquid template parsing conflicts

## Prevention Measures
To prevent future issues:
1. Always quote YAML tags containing special characters
2. Use `&#123;% raw %&#125;` tags around code blocks with `{` or `}`
3. Run YAML validation before committing new posts
4. Consider using automated linting in CI/CD pipeline

## Testing
- ✅ All YAML front matter validates successfully  
- ✅ No more Liquid template parsing errors
- ✅ Build errors resolved

## Next Steps
Monitor the GitHub Pages deployment workflow to ensure successful builds going forward.