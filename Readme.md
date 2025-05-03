1. To run this code (on Linex):

`./script.sh <input_file_path>`

2. To create docker file of this: 

`docker build -t <image_name> .`

3. To run this docker image:

`docker run --rm -v <file_path>:/app/input.txt <image_name> /app/input.txt`
