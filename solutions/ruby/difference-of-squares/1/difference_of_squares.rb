=begin
Write your code for the 'Difference Of Squares' exercise in this file. Make the tests in
`difference_of_squares_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/difference-of-squares` directory.
=end

class Squares
  attr_reader :square_of_sum, :sum_of_squares, :difference

  def initialize(number)
    @square_of_sum = (1..number).to_a.reduce(0, :+) ** 2
    @sum_of_squares = (1..number).to_a.map { |i| i ** 2 }.reduce(0, :+)
    @difference = @square_of_sum - @sum_of_squares
  end
end
