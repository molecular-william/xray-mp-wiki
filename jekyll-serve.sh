#!/bin/bash
# Wrapper script for jekyll serve with livereload
# Runs post-build Python scripts after each build

cd "$(dirname "$0")"

# Run jekyll serve with livereload
bundle exec jekyll serve --livereload "$@"

# The Python scripts will run after each build completes
python3 scripts/generate-random-pages.py 2>/dev/null &
python3 scripts/generate-health.py 2>/dev/null &

# Wait for background processes
cat > _site/random.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Random Page</title>
</head>
<body>
<script>
fetch('random_pages.json')
  .then(response => response.json())
  .then(pages => {
    if (pages.length > 0) {
      const randomIndex = Math.floor(Math.random() * pages.length);
      window.location.href = pages[randomIndex];
    }
  })
  .catch(error => console.error('Error loading random pages:', error));
</script>
</body>
</html>
EOF
