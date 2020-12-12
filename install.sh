pip install -r requirements.txt
pyinstaller -F pyort.py
cd dist
sudo cp pyort /usr/bin/
cd ..
rm -r build dist pyort.spec
echo "Installation is complete!"
