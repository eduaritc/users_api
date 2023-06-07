################ What's inside ################
- annalect.py: Python script with the solution.
- dockerfile: File which contains the instructions to create a docker image
- requirements.txt: File with the required libraries to the right execution of the
		    python script


################ About the python script ################
- All the code is included on the file annalect.py. 
- There are some comments to clarify the way I get the entries from the API
  and what I'd do to make it more flexible/scallable
- There are some comments at the end of this file
  where I dropped my thoughts about how to take this
  solution to AWS.

  
  ################ Creating  and executing the docker image ################
- And finally to create the docker image and run it, simply execute these two commands
  to create and execute docker image:
	- docker build -t annalect_challenge .
	- docker run annalect_challenge
	


