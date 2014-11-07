x=1

while x< 10
y=1
    while y < 10
         temp =x*y
         print "#{x}*#{y}=%2d;;;" % temp#格式化輸出
         y +=1   #y=y+1
     end 
     puts ""
   # puts x
   x = x +1 
end