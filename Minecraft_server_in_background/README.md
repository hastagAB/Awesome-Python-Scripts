# Running a Minecraft server in the background

This program runs a script (which can be specified) in a subprocess with redirected output
(new output location can be specified) and periodically checks a file for a keyword (both
the name of the file to check and the keyword to check for can be specified)
and exits (stopping the subprocess via sending a command), if the contents of the file
include the keyword.

You probably want to run this script in background, e.g. calling it via './run.py &'
or via 'nohup ./run.py &'.

A sample invocation could look like this:

```bash
nohup ./run.py &
```
Now the specified script, e.g. a Minecraft server, is running in the background.

```bash
echo stop > command.txt
```
After a short delay, the script in the background will be stopped.
