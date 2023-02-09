# letterboxd-dashboard

### Purpose
```letterboxd-dashboard``` uses data from your profile on Letterboxd — a film social media site where you can log and rate films — to create a dashboard on your rating patterns.

### Technologies Used
* python 3.11.1

### Setup/Installation Requirements
* Clone this repository.
* Navigate to the top level of the directory: ```letterboxd-dashboard/```.
* Install requirements with the command: ```pip -r requirements.txt```.

# How to Use ```letterboxd-dashboard```

### Letterboxd
[Letterboxd](https://letterboxd.com/) is a social platform for sharing your taste in film. To use ```letterboxd-dashboard```, one must have an active Letterboxd account, and at least 100 films rated. The more films you have rated in your Letterboxd account, the better the dashboard. First, you must retrieve the data from your Letterboxd account with the following steps:

1. Navigate to the ```IMPORT & EXPORT``` page under your [Letterboxd profile settings](https://letterboxd.com/settings/data/).
2. Select ```EXPORT YOUR DATA```. A pop up will appear to confirm. Select ```EXPORT YOUR DATA``` again.
3. A ```.zip``` file will download. Select it to unzip it.
4. Navigate into the unzipped folder.
5. Move the ```ratings.csv``` file into ```data``` directory at ```letterboxd-dashboard/data/``` in your cloned repository.

<i>If you don't have Letterboxd and would still like to check out ```letterboxd-dashboard```, navigate to the 
  ```letterboxd-dashboard/sample-data/``` directory. Inside, there is an example ```ratings.csv``` from my own Letterboxd account.
 Place it into the ```letterboxd-dashboard/data``` directory and continue through the instructions</i>. 

### Create Dashboard
1. Ensure you have navigated to the top level of the directory: ```letterboxd-dashboard/```.
2. Run the ```main.py``` file.
3. A dash webpage will open on your web browser containing the dashboard. Example attached below: ![(example attached)](https://github.com/yanezdavid/letterboxd-dashboard/blob/main/assets/dashboard-sample.png)

### Exit Program
If you would like to run the program again, enter ```command or ctrl + c``` to quit the dash app. Repeat the three steps outlined
in the ```Create Dashboard``` section above to create another dashboard.

### Errors & Exceptions
Custom error messages will be raised if certain conditions prevent ```letterboxd-dashboard``` from executing. If, after running ```main.py```, the program terminates, search in terminal for ```LetterboxdException``` error messages with general instructions on how to succesfully execute the program.

Some common failures to execute include:
1. Not having ```ratings.csv``` in the ```letterboxd/data/``` directory.
2. ```ratings.csv``` is empty, or has less than 100 films within in.

If you run into other errors, please create an issue so that I can improve your experience.

