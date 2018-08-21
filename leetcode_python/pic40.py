class t1:
    staticVar= 23
    def svarfuc(self):
        self.staticVar += 1
        print(self.staticVar)

print(t1.staticVar)
t1().svarfuc()
