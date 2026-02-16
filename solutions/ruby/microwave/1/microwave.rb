=begin
Write your code for the 'Microwave' exercise in this file. Make the tests in
`microwave_test.rb` pass.

To get started with TDD, see thrbe `README.md` file in your
`ruby/microwave` directory.
=end

class Microwave
    def initialize(timer)
        @minutes = (timer >= 100 ? (timer/100).floor : timer >= 60 ? (timer/60).floor : "00")
        @seconds = (timer >= 100 ? (timer % 100) : timer >= 60 ? (timer % 60) : timer)
        if @seconds >=60
          @minutes += 1
          @seconds -= 60
        end

    end
    def timer
      @minutes.to_s.rjust(2,"0") + ":" + @seconds.to_s.rjust(2,"0")
    end
end
