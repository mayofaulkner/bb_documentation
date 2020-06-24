
# Copy the notebooks to a new directory
cp -r docs/notebooks docs/notebooks_processed

# Clean up any previous documentation
make docs/ clean

# Make the new documentation
make docs/ html

# Push to gh-pages
bash docs/scripts/gh_push.sh

# Clean up everything
rm -r docs/notebooks_processed
rm -rf gh-pages
rm -r docs/rst-notebooks

make docs/clean

rm -r docs/_build
