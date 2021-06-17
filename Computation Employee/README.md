# New Comptational Employee Setup and Processes

## Table of Contents
* [Introduction](#Introduction)
* [Getting Set up](#Getting-Set-up)
* [MGHPCC](#MGHPCC)
* [BIB](#BIB)

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

##### __Directions for MAC/Linux__
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


##### __Directions for Windows__ 
3. You cannot use Putty for the BIB server. Download Ubuntu for windows from the Microsoft store
4. Create the .ssh directory
5. Create the .ssh/config file (same file as above)
6. SSH into the server the first time to and you will be prompted to reset your password<br>
**Enter you password followed by the authenticator with no space inbetween. <br>
Type the authenticator with no dashes just the numbers**

## MGHPCC
#### Introduction
#### Storage
#### Submitting a job
#### File Transfer
#### Support

## BIB
#### Introduction
#### File Transfer
#### Support