# Extract tar dir
import tarfile

tar = tarfile.open("spark-3.2.2-bin-hadoop3.2.tgz")
tar.extractall()
tar.close()