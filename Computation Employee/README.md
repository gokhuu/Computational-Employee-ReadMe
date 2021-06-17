# New Comptational Employee Setup and Processes

## Table of Contents
* [Introduction](#Introduction)
* [Getting Set up](#Getting-Set-up)
* [MGHPCC](#MGHPCC)
* [BIB](#BIB)
* [Advice](#Advice)

## Introduction
Hello!<br>
Welcome to the Lim/Chan lab.  This will be a short introduction to get you started on your computational work. I will go over a brief summary of the different aspects of what you are going to use here.<br>

#### Servers
In this lab we use two different servers: the Massachusetts Green High Performance Computing Center(MGHPCC) and the Bioinformatics and Intigrative Biology(BIB) server. <br>
The MGHPCC is the compute server that the lab uses. More information about the server can be found here: https://www.mghpcc.org/ <br>
The BIB server is purely used for storage.

#### Languages
Rigel and Elaine are most familiar with R and Perl; however, they have no preference in what languages you personally use to write you code.  Just a note, the MGHPCC server is on Python3.5 so if you are using python, just be aware that you may have version issues if you are using a more updated version.

## Getting Set up

### Setting up your accounts
#### MGHPCC
1. Fill out the account request form: https://www.umassrc.org/hpc/index.php
2. For windows: download putty or Ubuntu for windows, if you are using a Mac/Linux you can just SSH to the server
3. Read through the email for first time login instructions

#### BIB
1. Email arjan.vandervelde@umassmed.edu and michael.purcaro@umassmed.edu to have your BIB server account set up
2. Download Google Authenticator from App Store onto your phone, you will need it scan the QR code the send you

*See below depending on your OS*

__Directions for MAC/Linux__<br>
3. Create .ssh/config file
```bash
host ev001
        ProxyCommand=ssh -W %h:%p -l %r leap.wenglab.org
        ForwardX11 yes
        ForwardAgent yes
        ForwardX11Timeout 7d
        ServerAliveCountMax 3
        ServerAliveInterval 15
        GSSAPIAuthentication yes
        ControlMaster auto
```
*Note: wenglab is who Rigel and Elaine are renting the space from*

4. SSH into the server the first time to and you will be prompted to reset your password<br>
**Enter you password followed by the authenticator with no space inbetween. <br>
Type the authenticator with no dashes just the numbers**


__Directions for Windows__<br> 
3. You cannot use Putty for the BIB server. Download Ubuntu for windows from the Microsoft store
4. Create the .ssh directory
5. Create the .ssh/config file (same file as above)
6. SSH into the server the first time to and you will be prompted to reset your password<br>
**Enter you password followed by the authenticator with no space inbetween. <br>
Type the authenticator with no dashes just the numbers**

## MGHPCC
#### Introduction
As aforementioned, the MGHPCC cluster will be used for computing.  There are different queues to submit your job under: Short, Long, GPU, Interactive.  The short queue is for jobs less than 4 hours.  The long queue is are jobs up to 8 hours.  The GPU queue is for jobs that require GPU acceleration.  The interactive queue is unique in that it pulls up a terminal for you to run interactive scripts, but you can also use to run other things, I will go further into this below.

#### Data Storage
In your home directory, you are allowed 50gbs of space, do with it what you want.  I used it to store scripts.  The project data the Elaine/Rigel will give you will be under their project space: **/project/umw_elaine_lim** and **/project/umw_yingleong_chan**<br>

Those two directories will have their respective PI data that they are currently working on. If they ask you to look at something from an older project, it will be on the BIB server.

#### Submitting a job
If you don't want to bother with what I have to say: https://www.umassrc.org/wiki/index.php/Main_Page <br>
The MGHPCC has a wiki page that can answer some question about server usage and how to submit a job.
In you first email they will also provide examples on how to submit a job.

A sample job submission would look something like this
```bash
bsub -q long -n 2 -W 8:00 -R rusage[mem=2048] hostname 
```
bsub = the command to submit a job<br>
q = which queue are you using: short, long, GPU, interactive<br>
n = number of cores<br>
W = length of time you are allocating for you job<br>
R rusage = amount of memory allocated for the job<br>
hostname = insert job name or bash command

I created a bash script with all this and then just changed the hostname to whatever script I would run instead of just typing it out everytime.

If you job requires a module ie. Python3, R, etc. you must load those prior to submitting the job.
You can see what modules the cluster has:
```bash
module avail
```
or if you want to see what Python3 modules the cluster has:
```bash
module avail Python3
```
This way all the modules with Python3 in the name will be listed instead of all the module.  Use this method to search for needed modules.


#### File Transfer
FileZilla can be used to pull data from the cluster to work with on your local computer.
https://filezilla-project.org/download.php?type=client

#### Support
If you have any issues with the cluster you can email: hpcc-support@umassmed.edu

## BIB
#### Introduction
This server is used in the lab as long term data storage.  Elaine and Rigel's older project data will be stored on this server. I did not work with Rigel's older data, so I do not know the directory his old data is in.  Elaine's older data is in **/data/elim/**

#### File Transfer
Unlike the MGPHCC cluster, you cannot use FileZilla to move files on and off the server.  You must scp files.  Before you can scp you must first edit you config file.
```bash
        Controlpath /home/[whatever you user is]/.ssh/sockets/%r@%h:%p
        ControlPersist 15s
```
Add these two lines to the bottom of your config file.<br>
Make the directory .ssh/sockets.<br>

* For windows:
	- Open PowerShell
	- <code> scp -r user@ev001:/home/source/file_or_directory .</code>
	- The period will make the target directory your home folder
	
* For Mac/Linux:
	- Open Terminal
	- <code> scp -r user@ev001:/home/source/file_or_directory .</code>
	- The period will make the target directory your home folder
#### Support

## Advice