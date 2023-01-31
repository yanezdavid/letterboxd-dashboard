# letterboxd-dashboard

### Purpose
```letterboxd-dashboard``` uses data from a Letterboxd user's film ratings to create a dashboard to analyze their rating patterns.

### Technologies Used
* python 3.11.1

### Setup/Installation Requirements
* Clone this repository.
* Navigate to the top level of the directory: ```letterboxd-dashboard/```.
* Install requirements with ```pip -r requirements.txt```.

# How to Use letterboxd-dashboard

### Letterboxd
[Letterboxd](https://letterboxd.com/) is a social platform for sharing your taste in film. To use letterboxd-dashboard, one must have an active Letterboxd account, and at least 100 films rated. The more films you have rated in your Letterboxd account, the better the dashboard.

1. Navigate to the ```IMPORT & EXPORT``` page under your [Letterboxd profile settings](https://letterboxd.com/settings/data/).
2. Select ```EXPORT YOUR DATA```. A pop up will appear to confirm. Select ```EXPORT YOUR DATA``` again.
3. A ```.zip``` file will download. Select it to unzip it.
4. Navigate into the unzipped folder.
5. Move the ```ratings.csv``` file into ```data``` directory at ```letterboxd-dashboard/data``` in your cloned repository.
