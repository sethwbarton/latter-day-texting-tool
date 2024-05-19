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

![CleanShot 2024-05-18 at 15 28 55](https://github.com/sethwbarton/latter-day-texting-tool/assets/33107324/4c014623-d6b0-4e49-ae9a-afa77c826f25)

From the Github repository, click on "Releases".

Download the two shortcut files from the latest release. [Read more about Mac OS Shortcuts](https://support.apple.com/guide/shortcuts-mac/intro-to-shortcuts-apdf22b0444c/mac) if you are unsure what these do.

You should also download the application for your CPU architecture. If you have a 
Mac running an x86 Intel CPU, choose the release titled `Latter-day.Texting.Tool.x86.zip`. If you have a 
Mac running an ARM64 Apple Silicon CPU, choose the release titled `Latter-day.Texting.Tool.arm64.zip`.

You can tell which type of CPU you are using by going to the Apple menu in the top left corner of your screen,
selecting "About This Mac", and looking at the "Chip" field.

When the download is complete, unzip the file by double-clicking on it. You should see an application appear where you 
unzipped the folder.

### Updating Ward Member Data

**NOTE: You Only Need to Do this When Your Contact List is Out of Date With Ward Records**

Right-click (or click with two fingers) on the application and select "Open". 
The first time you do this, you may see a warning about this being from an unidentified developer. You can 
safely click "open."

This will open a small window with a single button that says "Download Ward Member Data". Click this button.
This will open a browser window and prompt you to log into the Church's website. 

From here, you need to navigate to the "Member Directory" page on the Church's website. 
When the application receives the member list data, the browser window will close automatically and you will
have two generated CSVs on your desktop for Elder's Quorum and Relief Society.

### Sending Text Messages to The Elders Quorum and Relief Society

Import the generated CSV of contacts into your Mac OS contacts app. And create two smart lists called "Elder's Quorum" and "Relief Society" by 
filtering for contacts with the Elders Quorum note and Relief Society Note, respectively. **You only need to do this if your contacts list is out of date with ward records.**

![CleanShot 2024-05-18 at 15 13 20](https://github.com/sethwbarton/latter-day-texting-tool/assets/33107324/c96f9ee4-5b15-4daf-afb1-b55785b5b830)

Once you have a smart list titled "Elder's Quorum" you can run the "Text Elder's Quorum" shortcut to send a message to everyone in the Elder's Quorum.
Alternatively, you can run the "Text Elder's Quorum with Attachement" shortcut to also send everyone an attachement such as a flyter or picture.

Right now, we only have Shortcuts to send messages to the Elder's Quorum, but we will create shortcuts to send messages to the Relief Society soon.

## How to Contribute

Read `CONTRIBUTING.md` to learn how to make contributions.
