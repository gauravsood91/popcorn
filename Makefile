CC = gcc
CFLAGS = -Wall
LDFLAGS = -ltdb

all: popcorn-server popcorn-dump

popcorn-server: popcorn-server.o
	$(CC) $(LDFLAGS) $< -o $@

popcorn-dump: popcorn-dump.o
	$(CC) $(LDFLAGS) $< -o $@

example:
	./popcorn-client > example.txt

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f *.o popcorn-server popcorn-dump example.txt popcorn.tar.bz2

dist:
	rm -f popcorn.tar.bz2
	tar cfj popcorn.tar.bz2 Makefile README popcorn-client popcorn-dump.c popcorn-rotate popcorn-server.c popcorn.conf popcorn.cron
