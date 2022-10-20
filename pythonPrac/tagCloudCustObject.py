#!/usr/bin/env python3

# custom container typr
class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        # dictionary.get(keyname, value)
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()

cloud["python"] = 10
len(cloud)

cloud.add("python")
cloud.add("python")
cloud.add("python")
cloud.add("python")
cloud.add("Python")

print(cloud.tags)
