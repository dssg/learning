#tmux
[@mdagost](https://github.com/mdagost)


These notes are based off of tmux version 1.8, so you'll need to upgrade from the default tmux on ubuntu.

ssh dssg@ec2-54-225-49-43.compute-1.amazonaws.com

ilovedata

##Why tmux?
Working on remote servers can suck.  What if you want to leave something running overnight but go home?  Do you hate having tons of open windows all connected to the same server?  Are you working with someone else on the same project (maybe pair programming) and you want to both be able to see the screen and type at the same time?

##Let’s start a tmux session

```
tmux -S /tmp/mdagost new-session -s mdagost
```

The -S flag tells us which "socket" file to write screen information too.  Not important to understand what that means, just remember the file.  The -s flag gives our new session a name.  You can leave off new-session, and you can leave off the -s, but they’re recommended.

You can see the socket file that is storing the screen information:

```
ls /tmp/mdagost
```

##All tmux commands start with a "leader"

The leader is normally ctrl-b, but let’s configure it to ctrl-a to make it more like screen and because it's easier to reach.  You can configure tmux with a .tmux.conf file in your home directory:

```
set -g prefix ^a
```

Now let's do something...

```
for f in {1..100}; do echo $f; sleep 1; done
```

##We can detach from our session...

```
ctrl-a d
```

##...and then re-attach
```
tmux -S /tmp/mdagost attach -t mdagost
```

The -t flag is the target session you want to attach to.

##We can see which sessions are already running
```
ps ax | grep '[n]ew-session -s'
```

And the cool thing is that anyone who can connect to the box can also attach to the session, see what's happening, and even control the input, but first you have to make it public by giving everyone read/write access to the socket.

```
chmod go+rw /tmp/mdagost
```

##Panes

```
ctrl-a % vertical split
ctrl-a “ horizontal split
```

Let's make this more convenient by adding this to .tmux.conf:

```
bind s split-window -v
bind v split-window -h
```

Then we can simply do this:

```
ctrl-a s vertical split
ctrl-a v horizontal split
```

```
ctrl-a q Show pane numbers (used to switch between panes)
ctrl-a q then number
ctrl-a o Switch to the next pane
ctrl-a arrow keys
```

##Windows
```
ctrl-a c Create new window
ctrl-a n Move to the next window
ctrl-a p Move to the previous window
ctrl-a , Rename the current window
```

##Help
```
ctrl-a ? List all keybindings
```

##Scrolling up
```
ctrl-a [ to scroll up and then escape
```


 
