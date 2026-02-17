=begin
Write your code for the 'Sum Of Multiples' exercise in this file. Make the tests in
`sum_of_multiples_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/sum-of-multiples` directory.
=end

class SumOfMultiples
  def initialize(*numbers)
    @numbers = numbers
  end

  def to(limit)
    mult = Array.new
    if @numbers[0] == 0 or @numbers == []
      return 0
    end
    for x in 1..(limit - 1)
      for f in @numbers
        if x % f == 0
          if !mult.include?(x)
            mult.push(x)
          end
        end
      end
    end
    if mult.length == 0
      0
    else
      mult.reduce(0, :+)
    end
  end
end
