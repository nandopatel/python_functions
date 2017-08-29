from random import randint

acc1 = randint(1,10000)
acc2 = randint(1,10000)
txbal = randint(1,10000)
def authtx(acc1,acc2,txbal):
  if acc1 < txbal:
    print "You cannot send more than you have."
    print 
    print "You need {} to complete the transaction".format(txbal-acc1)
    
  else:
    acc2 += txbal
    print "acc1 --> {} --> acc2".format(txbal)
    print txbal, "was transferred from acc1 to acc2"
 

authtx(acc1,acc2,txbal)