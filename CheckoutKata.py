def checkout():
  marks = "DABABA"
  counta = countb = countc = countd = counte =0
  for i in marks:

    if i == "A" : counta =counta +1 
    elif i == "B": countb = countb +1 
    elif i == "C":countc = countc +1 
    elif i == "D": countd = countd + 1
    else: counte = counte +1

  total = ((counta // 3)*130 + (counta%3)*50) + ((countb//2)*45 + (countb%2)*30) +countc*20  + countd*15 + counte

  return(total)
