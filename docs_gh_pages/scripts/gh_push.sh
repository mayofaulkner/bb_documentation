# Script to push html doc files to gh pages

# Repo information
ORG=mayofaulkner
REPO=bb_documentation

# Clone the gh-pages branch to local documentation directory
git clone -b gh-pages "https://github.com/$ORG/$REPO.git" gh-pages
cd gh-pages

# Copy everything from output of build into gh-pages branch
cp -R ../_build/html/* ./

# Add and commit all changes
git add -A .
git commit -m "$1";

# Push the changes
git push -q origin gh-pages

# Leave gh-pages repo and delete
cd ../
rm -rf gh-pages





