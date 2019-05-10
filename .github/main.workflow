workflow "On Push" {
  on = "push"
  resolves = ["Run Python Tests"]
}

action "Run Python Tests" {
  uses = "docker://python"
  args = "python3 -m unittest discover -v --pattern *.py"
}
