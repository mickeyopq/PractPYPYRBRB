class Kick
    def fq
        puts "fk~uuuuu"
    end
    def speak
        puts "喵~~~喵"
    end
end
class Cat < Kick #Class的第一個一定要用大寫
    def fq
        fail "i smootf"        
    end
end


a=Cat.new
a.speak
a.fq