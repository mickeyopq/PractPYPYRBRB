x = 2.0
puts "列出1/x + 1/y == 1,1~~100"
puts "我為了算分割營幕的比例寫的"
y = 2.0   #初值


while x <= 10 #條件==true，執行loop
    # while y <= 50 #條件==true，執行loop
        temp = 1 - 1.0/x
        y = 1/temp
        puts "x=#{x},y=#{y};;;;"
    # end
    x = x + 1
end

for num in (4..6)
    puts num
end