pip install -r requirements.txt
pyinstaller -F pyort.py
cd dist
sudo cp pyort /usr/bin/
echo "Cleaning cache!"
cd ..
rm -r build dist pyort.spec
cd ..
rm -r pyort
echo "Installation is complete!"
