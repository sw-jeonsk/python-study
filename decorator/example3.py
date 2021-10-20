class Sentance:
    
    def __init__(self, function) -> None:
        self.function = function
       
    
    def __call__(self, *args, **kwds):
        self.function("김철수")
        print("이다.")
    

@Sentance
def silly(name="김철수"):
    print("%s 바보"%(name))


silly()
