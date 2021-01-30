def distance(kms):
        if kms <= 20:
            print("close")
        elif kms > 20 and kms<50:
            print("median")
        else:
            print("far")
distance(60) 