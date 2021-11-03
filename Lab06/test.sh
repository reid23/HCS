echo "Testing normal test, output file is outputData.txt:"
/opt/anaconda3/bin/python ISBN.py < testFiles.txt
echo ""
echo "Testing empty file:"
/opt/anaconda3/bin/python ISBN.py < testFilesEmpty.txt