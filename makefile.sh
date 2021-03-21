#!/bin/sh

# $1 contest_directory
# $2 contest_name

cd ./$1

if [ -d ./$2/a ]
then
    touch ./$2/a/a.py
fi
if [ -d ./$2/b ]
then
    touch ./$2/b/b.py
fi
if [ -d ./$2/c ]
then
    touch ./$2/c/c.py
fi
if [ -d ./$2/d ]
then
    touch ./$2/d/d.py
fi
if [ -d ./$2/e ]
then
    touch ./$2/e/e.py
fi
if [ -d ./$2/f ]
then
    touch ./$2/f/f.py
fi
if [ -d ./$2/g ]
then
    touch ./$2/g/g.py
fi
if [ -d ./$2/h ]
then
    touch ./$2/h/h.py
fi
if [ -d ./$2/i ]
then
    touch ./$2/i/i.py
fi
if [ -d ./$2/j ]
then
    touch ./$2/j/j.py
fi
if [ -d ./$2/k ]
then
    touch ./$2/k/k.py
fi
if [ -d ./$2/l ]
then
    touch ./$2/l/l.py
fi
if [ -d ./$2/m ]
then
    touch ./$2/m/m.py
fi
if [ -d ./$2/n ]
then
    touch ./$2/n/n.py
fi
if [ -d ./$2/o ]
then
    touch ./$2/o/o.py
fi

cd ../