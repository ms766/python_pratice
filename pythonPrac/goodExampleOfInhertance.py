#!/usr/bin/env python3

# creation of cust exceptio
class InvaildOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise IndentationError("Stream already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise IndentationError("Stream already closed")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("reading data from a network")
