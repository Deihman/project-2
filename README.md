# UO CS330 project 2 - Calvin Stewart #

Author:     Calvin Stewart

Contact:    clownvant@icloud.com
        or
            cstewar2@uoregon.edu

Project 2 is a simple file server using docker and Flask. Set it up using the following command in the project directory. `myimage` can be replaced with your preferred name.

```
docker build -f Dockerfile -t myimage .
```

To run the image, use the following command, replacing `myimage` with the name of your image and replacing 5001 with a different port if desired.

```
docker run -d -p 5001:5000
```

You will then be able to access the server through your localhost network, where it will return the specified file in the URL or an error where appropriate.
