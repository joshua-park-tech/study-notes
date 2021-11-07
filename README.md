# study-notes
Created by @Joshua and @limiteddays

## Introduction
We used @appjar as our library to make this study notes. For loading files, we used the TXT file. 
To save the information of the images, dates and years that was created and also notes and subnotes. 

Currently, you can write and edit the textboxes on each page and if you run out of pages, you can create new ones. 
This application was created to manage our notes for example, the ones that were not able to create. 

## Features

![image](https://github.com/joshua-park-tech/study-notes/blob/main/appJar/github_related/1.png)

The login page is to greet the person and the notebook is inside. 

![image](https://github.com/joshua-park-tech/study-notes/blob/main/appJar/github_related/Screenshot%202021-11-07%20153035.png)

You can put in images, write things and share your work with others with a fancy username.
The notes are located on the top, where you can chose between math, science, geography and more.

On the bottom of the screen, we have NEXT and PREVIOUS button to go through different pages.
Create page will create a next page, but due to the limitation of APPJAR, we need to refresh the entire page, 
hence takes around 5~6 second depends on the processor of the computer. 


## Save files
The save file of the system is created with TXT. Below is the structure of our TXT savefile.

'''
1635650466.444111;.;Year;.;Month;.;Date;.;Your Description here;.;Your Side Note here;.;noimg.png;.;math

1635651265.334358;.;Year;.;Month;.;Date;.;Your Description here;.;Your Side Note here;.;noimg.png;.;math

1635651379.620838;.;Year;.;Month;.;Date;.;Your Description here;.;Your Side Note here;.;noimg.png;.;math

1635655915.3472261;.;Year;.;Month;.;Date;.;Your Description here;.;Your Side Note here;.;noimg.png;.;math

'''
The save files will save the current time in a second as a ID, save the year, month, date, description, sidenote, and image. 


## Problems
Due to the architecture of Appjar, the save button currently doesn't work. 
- The appjar cannot recognise where you are
- When we try to get the TXT file, appjar just loops it

Also, the packaging didn't work on MacOS due to appjar but it does operate. However, it does operate on Windows and Linux.
