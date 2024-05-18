# Latter-day Texting Tool
## What Is This?

This tool is meant to be used by communications specialists in wards of 
the Church of Jesus Christ of Latter-day Saints. You can use this tool to easily
message the members of your ward without having to create large group text messages or 
set up accounts on other platforms.

## Requirements

**Operating System**: Mac OS

**Software Installed**: Shortcuts App for Mac OS, Google Chrome, Contacts App for Mac OS, Apple ID log in

## Usage Instructions

### Install the Application 

![CleanShot 2024-05-18 at 15 03 56](https://github.com/sethwbarton/latter-day-texting-tool/assets/33107324/a8ed35c1-4a35-47a0-b233-949c192de1ef)

From the Github repository, click on "Releases".

On the latest release, download the package for your CPU architecture. If you have a 
Mac running an x86 Intel CPU, choose the release titled `Latter-day.Texting.Tool.x86.zip`. If you have a 
Mac running an ARM64 Apple Silicon CPU, choose the release titled `Latter-day.Texting.Tool.arm64.zip`.

You can tell which type of CPU you are using by going to the Apple menu in the top left corner of your screen,
selecting "About This Mac", and looking at the "Chip" field.

When the download is complete, unzip the file by double-clicking on it. You should see an application appear where you 
unzipped the folder.

While you're here, you should also download the two shortcuts that are stored in the `Shortcuts` folder in this repository. These are what you will run to text everyone in the ward.

### Updating Ward Member Data

**NOTE: You Only Need to Do this When Your Contact List is Out of Date With Ward Records**

Right-click (or click with two fingers) on the application and select "Open". 
The first time you do this, you may see a warning about this being from an unidentified developer. You can 
safely click "open."

This will open a small window with a single button that says "Download Ward Member Data". Click this button.
This will open a browser window and prompt you to log into the Church's website. 

From here, you need to navigate to the "Member Directory" page on the Church's website. 
When the application receives the member list data, the browser window will close automatically and you will
have a generated CSV on your desktop.

### Sending Text Messages to The Elders Quorum

Import the generated CSV of contacts into your Mac OS contacts app. And create a smart list called "Elder's Quorum" by 
filtering for contacts with the Elders Quorum note. **You only need to do this if your contacts list is out of date with ward records.**

![CleanShot 2024-05-18 at 15 13 20](https://github.com/sethwbarton/latter-day-texting-tool/assets/33107324/c96f9ee4-5b15-4daf-afb1-b55785b5b830)

Once you have a smart list titled "Elder's Quorum" you can run the "Text Elder's Quorum" shortcut to send a message to everyone in the Elder's Quorum.
Alternatively, you can run the "Text Elder's Quorum with Attachement" shortcut to also send everyone an attachement such as a flyter or picture.

### Sending Text Messages to the Relief Society

Coming soon! Work on this project is ongoing. If you'd like to help speed it along, please read the contributing section below.

## How to Contribute

Read `CONTRIBUTING.md` to learn how to make contributions.
