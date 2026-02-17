=begin
Write your code for the 'Triangle' exercise in this file. Make the tests in
`triangle_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/triangle` directory.
=end

class Triangle
  def initialize(sizes)
    @sizes = sizes
  end

  def sizes
    @sizes
  end

  def triangle?
    sizes[0] + sizes[1] > sizes[2] && sizes[1] + sizes[2] > sizes[0] && sizes[0] + sizes[2] > sizes[1]
  end

  def equilateral?
    triangle? && sizes[0] == sizes[1] && sizes[1] == sizes[2]
  end

  def isosceles?
    triangle? && (sizes[0] == sizes[1] || sizes[1] == sizes[2] || sizes[0] == sizes[2])
  end

  def scalene?
    triangle? && sizes[0] != sizes[1] && sizes[1] != sizes[2] && sizes[0] != sizes[2]
  end
end
