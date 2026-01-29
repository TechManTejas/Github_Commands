with open('output.txt', 'w') as out:
	out.write("Hello, Git and DVC!\n")
	out.write("This is a feature branch change.\n")
	# Read and print contents of data/data.txt
	with open('data/data.txt', 'r') as f:
		data = f.read()
		out.write("Contents of data/data.txt:\n")
		out.write(data + "\n")
