=begin
Write your code for the 'Resistor Color Duo' exercise in this file. Make the tests in
`resistor_color_duo_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/resistor-color-duo` directory.
=end

class ResistorColorDuo
    def self.value(colors)
        res = 0
        for i in 0..1
            case colors[i]
            when "black"
                res+=0*(10**(1-i))
            when "brown"
                res+=1*(10**(1-i))
            when "red"
                res+=2*(10**(1-i))
            when "orange"
                res+=3*(10**(1-i))
            when "yellow"
                res+=4*(10**(1-i))
            when "green"
                res+=5*(10**(1-i))
            when "blue"
                res+=6*(10**(1-i))
            when "violet"
                res+=7*(10**(1-i))
            when "grey"
                res+=8*(10**(1-i))
            when "white"
                res+=9*(10**(1-i))
            end
        end
        res
    end
end