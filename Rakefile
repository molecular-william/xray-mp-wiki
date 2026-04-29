require 'jekyll'

# Post-build tasks
task :post_build do
  puts "Running post-build tasks..."
  
  # Generate random pages JSON
  system('python3 scripts/generate-random-pages.py')
  
  # Generate random.html
  system("cat > _site/random.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
<meta charset=\"utf-8\">
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
EOF")
  
  # Generate health report
  system('python3 scripts/generate-health.py')
  
  puts "Post-build tasks complete."
end

task :default => :build
