if [ -f ~/.bashrc ]; then 
	source ~/.bashrc
fi

export PS1="\u@\W:~\$ "
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

alias ~='cd ~'				# Go to Home

alias subl='/Applications/Sublime\ Text.app/Contents/MacOS/Sublime\ Text'
alias sf='screenfetch'
alias hex='hexdump -C'			# hexdump -C

alias .2='cd ../../'			# Go back 2 directory levels
alias .3='cd ../../../'			# Go back 3 directory levels
alias .4='cd ../../../../'		# Go back 4 directory levels
alias .5='cd ../../../../../'		# Go back 5 directory levels
alias .6='cd ../../../../../../'	# Go back 6 directory levels

trash () { command mv "$@" ~/.Trash ; }	# Moves a file to the MacOS trash

