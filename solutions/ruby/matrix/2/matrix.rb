=begin
Write your code for the 'Matrix' exercise in this file. Make the tests in
`matrix_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/matrix` directory.
=end

class Matrix
  def initialize(matrix)
    @matrixRows = matrix.split("\n")
  end

  def rows
    @matrixRows.map do |row|
      row.split.map { |el| el.to_i }
    end
  end

  def columns
    self.rows.transpose
  end
end
