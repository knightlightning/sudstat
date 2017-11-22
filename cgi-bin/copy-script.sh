#/bin/bash

mv /usr/share/sudpass/$1 /usr/lib/cgi-bin/$1
dos2unix /usr/lib/cgi-bin/$1
chmod a+x /usr/lib/cgi-bin/$1

