class CompTarget(object):
    def override(self):
        print("Target overrid()")
    
    def implicit(self):
        print("target override()")
    
    def altered(self):
        print("target altered()")

class Owner(object):
    def __init__(self):
        self.comptarget = CompTarget()

    def implicit(self):
        self.comptarget.implicit()
    
    def override(self):
        print("owner override()")
    
    def altered(self):
        print("owner before target alterd()")
        self.comptarget.altered()
        print("owner after target altered()")


owner = Owner()
owner.implicit()
owner.override()
owner.altered()