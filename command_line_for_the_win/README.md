# Commandline_for_win Project in A

## SFTP USAGE:

1. Opened my terminal on the local machine in the directory containing screenshots and the README file (using Ubuntu 22.04).

2. Used the following command to establish an SFTP connection to the sandbox environment:
sftp username@hostname
   (Replace `username` and `hostname` with the provided credentials from alx sandboxes page).

3. Typed "yes" for the confirmation prompt to proceed with the connection.

4. Pasted the password from alx web terminal page to authenticate the connection.

5. Navigated to the desired directory in the SFTP connection using the following command:
cd /root/alx-system_engineering-devops/command_line_for_the_win/

6. Uploaded everything from my local directory (since it only contained the desired files) using the following command:
put *

7. After the upload was complete, I checked for the presence of the files in the remote directory using the `ls` command.

