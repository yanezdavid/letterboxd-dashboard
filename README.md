# letterboxd-dashboard

### Purpose
```letterboxd-dashboard``` uses data from a Letterboxd user's film ratings to create a dashboard on their rating patterns.

### Technologies Used
* python 3.11.1

### Setup/Installation Requirements
* Clone this repository.
* Navigate to the top level of the directory: ```letterboxd-dashboard/```.
* Install requirements with the command: ```pip -r requirements.txt```.

# How to Use letterboxd-dashboard

### Letterboxd
[Letterboxd](https://letterboxd.com/) is a social platform for sharing your taste in film. To use ```letterboxd-dashboard```, one must have an active Letterboxd account, and at least 100 films rated. The more films you have rated in your Letterboxd account, the better the dashboard. (If you are not a Letterboxd user but would like to use ```letterboxd-dashboard```, continue reading for special instruction.)

1. Navigate to the ```IMPORT & EXPORT``` page under your [Letterboxd profile settings](https://letterboxd.com/settings/data/).
2. Select ```EXPORT YOUR DATA```. A pop up will appear to confirm. Select ```EXPORT YOUR DATA``` again.
3. A ```.zip``` file will download. Select it to unzip it.
4. Navigate into the unzipped folder.
5. Move the ```ratings.csv``` file into ```data``` directory at ```letterboxd-dashboard/data``` in your cloned repository.

### Create Dashboard
1. Ensure you have navigated to the top level of the directory: ```letterboxd-dashboard/```.
2. Enter the command: ```python main.py``` to generate the dashboard.
3. Navigate to the ```letterboxd/visualizations``` directory.
4. Select ```dashboard.png``` to look at your dashboard.

### Errors & Exceptions
Custom errors will display if certain conditions prevent ```letterboxd-dashboard``` from executing. If, after running ```python main.py```, the prgram terminates, search in terminal for ```LetterboxdException``` error messages with general instructions on how to succesfully execute the program.