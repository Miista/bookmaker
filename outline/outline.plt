set term pngcairo

set output "lol.png"

characters = system('ls | grep ".dat$" | sed "s/.dat//" | tr "\n" " "')
system("echo ".characters)

set yrange [0:*]

plot for [c in characters] \
    c.'.dat' using 3:4:xtic(1):ytic(2) with lines t c
