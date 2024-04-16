# MySQL Primary-Replica Configuration and Backup Automation

This repository contains the configuration files and backup automation script for setting up MySQL primary-replica servers and automating the generation of database backups.

## Project Overview

The project involved learning how to configure database servers in a primary-replica model using MySQL. The main objectives were to configure two servers provided by ALX in a MySQL primary-replica setup with a dummy database, and to write a Bash script to automate the generation of database backups.

## Tasks

### 1. 4-mysql_configuration_primary
   - Description: The MySQL my.conf configuration file used to set up the first server as a primary database server on the database tyrell_corp.
   - File: [Provide File Name]

### 2. 4-mysql_configuration_replica
   - Description: The MySQL my.conf configuration file used to set up the second server as the replica database server on the database tyrell_corp.
   - File: [Provide File Name]

### 3. 5-mysql_backup
   - Description: Bash script that generates a compressed tar.gz archive from a MySQL dump.
   - Usage: `./5-mysql_backup <MySQL root password>`
   - Functionality: Generates a dump containing all MySQL databases on the root server and names the resulting tar archive in the format day-month-year.tar.gz.

## Usage
To use the backup script, run the following command:


## Note
Please ensure that the necessary permissions and configurations are in place before running the scripts.

## Support
For any questions or assistance regarding this project, feel free to reach out.

Thank you for your interest in our MySQL primary-replica configuration and backup automation project!
